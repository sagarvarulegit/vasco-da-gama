"""Generate a still image with the Gemini image model.

Uses GEMINI_API_KEY from the environment. This deliberately targets the
Gemini API image models (for example gemini-2.5-flash-image), not the Vertex
Imagen `:predict` endpoint, which requires different authentication.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request


API_URL = "https://generativelanguage.googleapis.com/v1beta/interactions"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--prompt", help="Prompt text")
    source.add_argument("--prompt-file", type=pathlib.Path, help="UTF-8 prompt file")
    parser.add_argument("--output", required=True, type=pathlib.Path, help="PNG output path")
    parser.add_argument(
        "--model",
        default=os.environ.get("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image"),
        help="Gemini image model (default: GEMINI_IMAGE_MODEL or gemini-2.5-flash-image)",
    )
    return parser.parse_args()


def extract_image(response: dict) -> bytes | None:
    output = response.get("output_image")
    if isinstance(output, dict) and output.get("data"):
        return base64.b64decode(output["data"])

    for step in response.get("steps", []):
        for block in step.get("content", []) if isinstance(step, dict) else []:
            if isinstance(block, dict) and block.get("type") == "image" and block.get("data"):
                return base64.b64decode(block["data"])
    return None


def main() -> int:
    args = parse_args()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY is not set.", file=sys.stderr)
        return 2

    prompt = args.prompt if args.prompt is not None else args.prompt_file.read_text(encoding="utf-8")
    payload = {"model": args.model, "input": prompt}
    request = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"x-goog-api-key": api_key, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        print(f"Gemini API HTTP {error.code}: {detail}", file=sys.stderr)
        return 1
    except urllib.error.URLError as error:
        print(f"Gemini API connection failed: {error.reason}", file=sys.stderr)
        return 1

    image_bytes = extract_image(body)
    if image_bytes is None:
        print("Gemini returned no image. Full response:", file=sys.stderr)
        print(json.dumps(body, indent=2)[:8000], file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(image_bytes)
    print(f"Saved {args.output} ({len(image_bytes)} bytes) using {args.model}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
