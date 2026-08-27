# Gemini image generation

The project key is a working Gemini API key. The previous Imagen path was
incorrect for this key: the available API model registry exposes Gemini image
models through `generateContent`, not a Vertex Imagen `:predict` request.

Use the local wrapper from the repository root:

```powershell
python production/tools/gemini_image_generate.py `
  --prompt-file prompts/CH01-EP02-image-prompts.md `
  --output images/CH01-EP02-S01-gemini-v1.png
```

The default model is `gemini-2.5-flash-image`. Override it with
`--model` or `GEMINI_IMAGE_MODEL` after confirming that model is enabled for
the key. `GEMINI_API_KEY` is read only from the environment and is never
written to a file.

The smoke test output at `images/gemini-api-smoke-test.png` verifies that the
key, endpoint, response decoding, and PNG writing path work end to end. It is
not a canonical chapter frame.
