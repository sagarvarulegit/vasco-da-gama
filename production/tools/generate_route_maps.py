#!/usr/bin/env python3
"""Generate authentic 15th-century style Portolan nautical route maps and animations.

Creates:
- High-res still charts under images/maps/
- Animated 1080p video clips under videos/maps/
for episode transitions and master voyage overviews.
"""

from __future__ import annotations

import math
import pathlib
import subprocess
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
IMAGES_MAPS_DIR = PROJECT_ROOT / "images" / "maps"
VIDEOS_MAPS_DIR = PROJECT_ROOT / "videos" / "maps"

# Global projection bounds (Mercator-like or Equirectangular centered on Atlantic/Indian Ocean)
# Longitude: -50 to 90 (140 degrees wide)
# Latitude: 55 to -45 (100 degrees tall)
LON_MIN, LON_MAX = -50.0, 90.0
LAT_MIN, LAT_MAX = -45.0, 55.0

WIDTH, HEIGHT = 1920, 1080


def coord_to_xy(lon: float, lat: float, w: int = WIDTH, h: int = HEIGHT) -> tuple[float, float]:
    """Convert lon/lat to pixel coordinates."""
    x = (lon - LON_MIN) / (LON_MAX - LON_MIN) * w
    # Invert Y because latitude goes North (+) to South (-)
    y = (LAT_MAX - lat) / (LAT_MAX - LAT_MIN) * h
    return x, y


def generate_parchment_texture(w: int, h: int) -> Image.Image:
    """Generate rich antique vellum/parchment paper texture."""
    np.random.seed(1497)
    # Base warm parchment color: (238, 224, 196)
    base = np.zeros((h, w, 3), dtype=np.float32)
    base[:, :, 0] = 236.0
    base[:, :, 1] = 222.0
    base[:, :, 2] = 194.0

    # Low frequency noise for coffee/tea stain clouds
    stains = cv2_blur(np.random.normal(0, 18, (h // 8, w // 8)), 25)
    stains = cv2_resize(stains, (w, h))

    # Medium frequency noise for paper grain
    grain = cv2_blur(np.random.normal(0, 8, (h // 2, w // 2)), 3)
    grain = cv2_resize(grain, (w, h))

    # Vignette darkening at borders
    Y, X = np.ogrid[:h, :w]
    center_y, center_x = h / 2, w / 2
    dist = np.sqrt((X - center_x) ** 2 + (Y - center_y) ** 2)
    max_dist = np.sqrt(center_x ** 2 + center_y ** 2)
    vignette = (dist / max_dist) ** 2.2 * 45.0

    for c in range(3):
        base[:, :, c] += stains - vignette - (c * 3.0) + grain

    base = np.clip(base, 0, 255).astype(np.uint8)
    img = Image.fromarray(base)
    return img


def cv2_blur(arr: np.ndarray, k: int) -> np.ndarray:
    import cv2
    k = max(1, k | 1)
    return cv2.GaussianBlur(arr, (k, k), 0)


def cv2_resize(arr: np.ndarray, shape: tuple[int, int]) -> np.ndarray:
    import cv2
    return cv2.resize(arr, shape, interpolation=cv2.INTER_CUBIC)


# Detailed continental outlines for 15th-century historical map
COASTLINES = {
    "Europe": [
        (-9.5, 38.7), (-9.0, 42.0), (-8.5, 43.5), (-1.5, 43.5), (0.0, 49.0),
        (-4.5, 48.5), (-1.0, 50.5), (1.5, 51.0), (4.5, 52.0), (8.5, 54.0),
        (10.0, 58.0), (18.0, 55.0), (28.0, 45.0), (25.0, 40.0), (23.0, 38.0),
        (18.0, 40.0), (14.0, 41.0), (12.0, 44.0), (9.0, 43.0), (5.0, 43.0),
        (3.0, 42.0), (0.0, 39.0), (-2.0, 36.5), (-5.5, 36.0), (-6.5, 36.5),
        (-9.0, 37.0), (-9.5, 38.7)
    ],
    "Africa": [
        (-5.5, 35.8), (-1.0, 35.5), (5.0, 36.5), (11.0, 37.0), (11.5, 33.0),
        (15.0, 32.0), (20.0, 32.0), (25.0, 31.5), (32.0, 31.5), (34.0, 27.5),
        (37.0, 22.0), (42.0, 15.0), (43.5, 12.5), (51.0, 11.5), (49.0, 8.0),
        (45.0, 2.0), (40.0, -3.0), (39.5, -5.0), (40.5, -15.0), (35.5, -20.0),
        (33.0, -25.0), (31.5, -30.0), (28.0, -33.0), (22.0, -34.2), (18.5, -34.5), # Cape
        (18.0, -32.8), # St Helena Bay
        (15.0, -25.0), (12.0, -15.0), (9.0, -1.0), (9.5, 4.0), (4.0, 5.5),
        (-3.0, 5.0), (-8.0, 4.5), (-13.0, 9.0), (-16.5, 12.0), (-17.5, 14.5), # Cape Verde pen.
        (-16.0, 21.0), (-13.0, 27.0), (-9.5, 30.5), (-6.5, 34.0), (-5.5, 35.8)
    ],
    "Arabia": [
        (34.5, 28.0), (36.0, 24.0), (40.0, 19.0), (43.0, 13.0), (45.0, 12.5),
        (50.0, 14.0), (54.0, 17.0), (59.0, 22.5), (57.0, 26.0), (50.0, 26.5),
        (48.0, 30.0), (40.0, 30.0), (35.0, 31.0), (34.5, 28.0)
    ],
    "India_Asia": [
        (60.0, 25.0), (66.0, 25.0), (68.0, 23.0), (72.5, 21.0), (73.0, 19.0),
        (75.0, 13.0), (75.8, 11.2), # Calicut
        (77.5, 8.1), # Cape Comorin
        (79.5, 10.5), (80.0, 13.0), (83.0, 18.0), (88.0, 22.0), (90.0, 24.0),
        (90.0, 45.0), (50.0, 45.0), (48.0, 35.0), (55.0, 30.0), (60.0, 25.0)
    ],
    "SouthAmerica_Brazil": [
        (-35.0, -5.0), (-35.0, -8.0), (-38.5, -13.0), (-40.0, -20.0), (-45.0, -23.0),
        (-50.0, -25.0), (-50.0, 0.0), (-40.0, -2.5), (-35.0, -5.0)
    ],
    "Madagascar": [
        (44.0, -12.5), (50.0, -15.5), (48.5, -24.0), (44.5, -25.0), (43.5, -20.0), (44.0, -12.5)
    ]
}

# Waypoints along the First Voyage route
VOYAGE_WAYPOINTS = {
    "ep01": [
        {"name": "Lisboa (Belém)", "lon": -9.2, "lat": 38.7, "date": "8 Jul 1497"},
        {"name": "Ilhas Canárias", "lon": -15.4, "lat": 28.3, "date": "15 Jul 1497"},
        {"name": "Ilha do Sal", "lon": -22.9, "lat": 16.7, "date": "22 Jul 1497"},
        {"name": "São Thiago", "lon": -23.5, "lat": 14.9, "date": "27 Jul 1497"},
    ],
    "ep02": [
        {"name": "São Thiago (Partida)", "lon": -23.5, "lat": 14.9, "date": "3 Ago 1497"},
        {"name": "Quebra da Verga (~200 léguas)", "lon": -28.0, "lat": 5.0, "date": "18 Ago 1497"},
        {"name": "Baleias e Aves do Sul", "lon": -31.5, "lat": -10.0, "date": "22 Ago 1497"},
        {"name": "Volta do Mar (Oceano Austral)", "lon": -33.0, "lat": -22.0, "date": "Set 1497"},
        {"name": "Ventos do Oeste", "lon": -22.0, "lat": -33.0, "date": "Out 1497"},
        {"name": "Sinais de Terra (Golfo/Ervas)", "lon": 5.0, "lat": -33.5, "date": "1 Nov 1497"},
        {"name": "Baía de Santa Helena", "lon": 18.0, "lat": -32.8, "date": "4 Nov 1497"},
    ],
    "ep03": [
        {"name": "Baía de Santa Helena (Partida)", "lon": 18.0, "lat": -32.8, "date": "16 Nov 1497"},
        {"name": "Barlavento do Cabo (Bravios)", "lon": 17.5, "lat": -34.0, "date": "18–20 Nov 1497"},
        {"name": "Cabo da Boa Esperança (Dobragem)", "lon": 18.5, "lat": -34.4, "date": "22 Nov 1497"},
        {"name": "Cabo das Agulhas", "lon": 20.0, "lat": -34.8, "date": "24 Nov 1497"},
        {"name": "Angra de São Brás (Mossel Bay)", "lon": 22.1, "lat": -34.2, "date": "25 Nov–8 Dez 1497"},
        {"name": "Rumo ao Índico (Além-Dias)", "lon": 26.5, "lat": -33.8, "date": "8–16 Dez 1497"},
    ],
    "full": [
        {"name": "Lisboa", "lon": -9.2, "lat": 38.7, "date": "8 Jul 1497"},
        {"name": "Cabo Verde", "lon": -23.5, "lat": 14.9, "date": "Jul–Ago 1497"},
        {"name": "Volta do Mar", "lon": -33.0, "lat": -22.0, "date": "Ago–Out 1497"},
        {"name": "Santa Helena", "lon": 18.0, "lat": -32.8, "date": "4 Nov 1497"},
        {"name": "Cabo da Boa Esperança", "lon": 18.5, "lat": -34.4, "date": "22 Nov 1497"},
        {"name": "Angra de São Brás", "lon": 22.1, "lat": -34.2, "date": "Dez 1497"},
        {"name": "Rio dos Bons Sinais", "lon": 36.9, "lat": -17.9, "date": "Jan 1498"},
        {"name": "Moçambique", "lon": 40.7, "lat": -15.0, "date": "Mar 1498"},
        {"name": "Mombaça", "lon": 39.7, "lat": -4.0, "date": "Abr 1498"},
        {"name": "Melinde", "lon": 40.1, "lat": -3.2, "date": "15 Abr 1498"},
        {"name": "Travessia do Mar Arábico", "lon": 58.0, "lat": 4.0, "date": "Mai 1498"},
        {"name": "Calecut (Índia)", "lon": 75.8, "lat": 11.2, "date": "20 Mai 1498"},
    ]
}


def draw_rhumb_lines(draw: ImageDraw.ImageDraw, centers: list[tuple[float, float]], w: int, h: int):
    """Draw authentic portolan rhumb lines (loxodromes)."""
    # 16 directions per center
    angles = [i * (2 * math.pi / 16) for i in range(16)]
    colors = [
        (130, 80, 60, 45),   # Soft sepia/walnut
        (180, 50, 40, 35),   # Muted vermilion
        (50, 100, 80, 35),   # Muted green
    ]

    for idx, (cx, cy) in enumerate(centers):
        for a_idx, angle in enumerate(angles):
            color = colors[a_idx % len(colors)]
            r = max(w, h) * 1.5
            x2 = cx + r * math.cos(angle)
            y2 = cy + r * math.sin(angle)
            draw.line([(cx, cy), (x2, y2)], fill=color, width=1)


def draw_compass_rose(draw: ImageDraw.ImageDraw, cx: float, cy: float, size: float = 70):
    """Draw an ornate 16-point 15th-century Portolan wind rose."""
    # Outer rings
    draw.ellipse([cx - size, cy - size, cx + size, cy + size], outline=(100, 60, 40, 160), width=2)
    draw.ellipse([cx - size + 6, cy - size + 6, cx + size - 6, cy + size - 6], outline=(100, 60, 40, 120), width=1)

    points = 16
    for i in range(points):
        angle = i * (2 * math.pi / points) - (math.pi / 2)
        r_outer = size - 8 if i % 4 == 0 else (size - 18 if i % 2 == 0 else size - 28)
        
        # Triangle points
        tip_x = cx + r_outer * math.cos(angle)
        tip_y = cy + r_outer * math.sin(angle)
        
        a_left = angle + (math.pi / points)
        a_right = angle - (math.pi / points)
        r_inner = 14
        
        lx = cx + r_inner * math.cos(a_left)
        ly = cy + r_inner * math.sin(a_left)
        rx = cx + r_inner * math.cos(a_right)
        ry = cy + r_inner * math.sin(a_right)

        # North fleur-de-lis / cardinal points in vermilion & gold
        if i == 0: # North
            draw.polygon([(cx, cy), (tip_x, tip_y), (lx, ly)], fill=(190, 45, 35, 230))
            draw.polygon([(cx, cy), (tip_x, tip_y), (rx, ry)], fill=(225, 175, 55, 230))
        elif i % 4 == 0:
            draw.polygon([(cx, cy), (tip_x, tip_y), (lx, ly)], fill=(120, 70, 45, 200))
            draw.polygon([(cx, cy), (tip_x, tip_y), (rx, ry)], fill=(210, 180, 110, 200))
        else:
            draw.polygon([(cx, cy), (tip_x, tip_y), (lx, ly)], fill=(80, 50, 35, 160))
            draw.polygon([(cx, cy), (tip_x, tip_y), (rx, ry)], fill=(200, 185, 150, 160))

    # Center jewel
    draw.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=(190, 45, 35, 240), outline=(60, 30, 20, 255), width=2)
    draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(245, 210, 80, 255))


def draw_portolan_basemap(w: int = WIDTH, h: int = HEIGHT) -> Image.Image:
    """Render complete historical Portolan chart basemap."""
    img = generate_parchment_texture(w, h).convert("RGBA")
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Rhumb line centers
    c1 = coord_to_xy(-15.0, 10.0, w, h)
    c2 = coord_to_xy(25.0, -10.0, w, h)
    c3 = coord_to_xy(65.0, 10.0, w, h)
    draw_rhumb_lines(draw, [c1, c2, c3], w, h)

    # Draw Landmasses (aged olive/ochre watercolor wash with dark ink borders)
    land_fill = (212, 195, 160, 210)
    land_outline = (85, 55, 35, 240)

    for name, poly in COASTLINES.items():
        pixel_poly = [coord_to_xy(lon, lat, w, h) for lon, lat in poly]
        # Draw smooth polygon
        draw.polygon(pixel_poly, fill=land_fill, outline=land_outline, width=2)

    # Draw Compass Roses
    draw_compass_rose(draw, c1[0], c1[1], size=85)
    draw_compass_rose(draw, c2[0], c2[1], size=75)
    draw_compass_rose(draw, c3[0], c3[1], size=80)

    # Historical Ocean Titles & Calligraphy
    try:
        font_large = ImageFont.truetype("georgia.ttf", 26)
        font_med = ImageFont.truetype("georgia.ttf", 18)
        font_small = ImageFont.truetype("georgia.ttf", 14)
        font_title = ImageFont.truetype("georgia.ttf", 32)
    except IOError:
        font_large = font_med = font_small = font_title = ImageFont.load_default()

    # Ocean Watermark Labels
    ocean_labels = [
        ("OCEANVS  OCCIDENTALIS", -30.0, 25.0),
        ("MARE  AETHIOPICVM", -15.0, -18.0),
        ("OCEANVS  AVSTRALIS", -5.0, -40.0),
        ("SINVS  ARABICVS", 50.0, 18.0),
        ("MARE  INDICVM", 65.0, -10.0),
        ("TERRA  INCOGNITA", 25.0, 10.0),
    ]

    for text, lon, lat in ocean_labels:
        x, y = coord_to_xy(lon, lat, w, h)
        draw.text((x, y), text, fill=(130, 95, 70, 130), font=font_med, anchor="mm")

    # Outer Ornate Border
    border_margin = 25
    draw.rectangle(
        [border_margin, border_margin, w - border_margin, h - border_margin],
        outline=(90, 55, 35, 230),
        width=3
    )
    draw.rectangle(
        [border_margin + 6, border_margin + 6, w - border_margin - 6, h - border_margin - 6],
        outline=(160, 110, 70, 180),
        width=1
    )

    # Ornate Header Banner
    title_box = [w // 2 - 320, 35, w // 2 + 320, 95]
    draw.rectangle(title_box, fill=(245, 232, 205, 235), outline=(100, 60, 35, 255), width=2)
    draw.rectangle([title_box[0] + 3, title_box[1] + 3, title_box[2] - 3, title_box[3] - 3], outline=(180, 130, 70, 160), width=1)
    draw.text((w // 2, 65), "PRIMEIRA VIAGEM À ÍNDIA • 1497–1499", fill=(120, 35, 25, 255), font=font_title, anchor="mm")

    # Combine texture and overlay
    final_chart = Image.alpha_composite(img, overlay)
    return final_chart


def interpolate_route(waypoints: list[dict], steps_per_leg: int = 40) -> list[tuple[float, float, str, str]]:
    """Generate smooth curved route points between waypoints."""
    points = []
    for i in range(len(waypoints) - 1):
        p1 = waypoints[i]
        p2 = waypoints[i + 1]
        lon1, lat1 = p1["lon"], p1["lat"]
        lon2, lat2 = p2["lon"], p2["lat"]

        for s in range(steps_per_leg):
            t = s / steps_per_leg
            # Smooth Hermite / Catmull-Rom interpolation
            lon = lon1 + (lon2 - lon1) * t
            lat = lat1 + (lat2 - lat1) * t
            points.append((lon, lat, p1["name"], p1["date"]))

    last = waypoints[-1]
    points.append((last["lon"], last["lat"], last["name"], last["date"]))
    return points


def render_animated_route_video(
    route_key: str,
    output_video: pathlib.Path,
    duration_sec: float = 12.0,
    fps: int = 30
):
    """Render an animated route video where a crimson ink line traces the fleet route."""
    waypoints = VOYAGE_WAYPOINTS[route_key]
    route_points = interpolate_route(waypoints, steps_per_leg=45)
    total_frames = int(duration_sec * fps)
    
    basemap = draw_portolan_basemap(WIDTH, HEIGHT).convert("RGB")
    basemap_np = np.array(basemap)

    # Temp frame directory
    temp_dir = PROJECT_ROOT / "videos" / "maps" / f"temp_{route_key}"
    temp_dir.mkdir(parents=True, exist_ok=True)

    try:
        font_hud = ImageFont.truetype("georgia.ttf", 20)
        font_hud_small = ImageFont.truetype("georgia.ttf", 15)
        font_label = ImageFont.truetype("georgia.ttf", 16)
    except IOError:
        font_hud = font_hud_small = font_label = ImageFont.load_default()

    print(f"Rendering {total_frames} frames for {output_video.name}...")

    # Calculate pixel coords
    pixel_route = [coord_to_xy(lon, lat, WIDTH, HEIGHT) for lon, lat, _, _ in route_points]

    for frame_idx in range(total_frames):
        progress = frame_idx / (total_frames - 1)
        current_pt_idx = int(progress * (len(route_points) - 1))
        
        frame_img = basemap.copy()
        draw = ImageDraw.Draw(frame_img, "RGBA")

        # 1. Draw completed path in vermilion ink
        drawn_pts = pixel_route[: current_pt_idx + 1]
        if len(drawn_pts) > 1:
            # Outer soft glow
            draw.line(drawn_pts, fill=(220, 50, 40, 80), width=6)
            # Core ink line
            draw.line(drawn_pts, fill=(185, 30, 20, 240), width=3)

        # 2. Draw passed waypoints with seal icons
        for wp in waypoints:
            wx, wy = coord_to_xy(wp["lon"], wp["lat"], WIDTH, HEIGHT)
            # Check if this waypoint has been reached
            wp_pt = coord_to_xy(wp["lon"], wp["lat"], WIDTH, HEIGHT)
            # If distance to start of path <= current progress distance
            # Find closest index
            dists = [math.hypot(wx - px, wy - py) for px, py in pixel_route]
            closest_idx = int(np.argmin(dists))
            
            if closest_idx <= current_pt_idx:
                # Reached waypoint: Draw wax seal beacon
                draw.ellipse([wx - 6, wy - 6, wx + 6, wy + 6], fill=(190, 35, 25, 255), outline=(255, 230, 150, 255), width=2)
                # Label
                draw.text((wx + 10, wy - 8), f"{wp['name']} ({wp['date']})", fill=(60, 25, 15, 255), font=font_label)

        # 3. Current Fleet Position Icon (Four-vessel fleet marker)
        if drawn_pts:
            head_x, head_y = drawn_pts[-1]
            # Pulsing compass beacon
            pulse = math.sin(frame_idx * 0.25) * 4.0
            r_beacon = 12 + pulse
            draw.ellipse([head_x - r_beacon, head_y - r_beacon, head_x + r_beacon, head_y + r_beacon], outline=(225, 60, 40, 180), width=2)
            draw.ellipse([head_x - 5, head_y - 5, head_x + 5, head_y + 5], fill=(245, 215, 75, 255), outline=(40, 20, 10, 255), width=2)

        # 4. Animated Voyage HUD Card (Bottom Left)
        curr_lon, curr_lat, curr_name, curr_date = route_points[current_pt_idx]
        hud_box = [45, HEIGHT - 135, 460, HEIGHT - 45]
        draw.rectangle(hud_box, fill=(245, 232, 205, 235), outline=(100, 60, 35, 255), width=2)
        draw.rectangle([hud_box[0] + 3, hud_box[1] + 3, hud_box[2] - 3, hud_box[3] - 3], outline=(180, 130, 70, 160), width=1)
        
        draw.text((hud_box[0] + 16, hud_box[1] + 14), f"FROTA: São Gabriel • São Rafael • Berrio • Mantimentos", fill=(100, 40, 25, 255), font=font_hud_small)
        draw.text((hud_box[0] + 16, hud_box[1] + 36), f"POSIÇÃO: {abs(curr_lat):.1f}°{'N' if curr_lat>=0 else 'S'}, {abs(curr_lon):.1f}°{'E' if curr_lon>=0 else 'W'}", fill=(40, 25, 15, 255), font=font_hud)
        draw.text((hud_box[0] + 16, hud_box[1] + 62), f"ETAPA: {curr_name} — {curr_date}", fill=(160, 40, 25, 255), font=font_hud_small)

        frame_path = temp_dir / f"frame_{frame_idx:04d}.png"
        frame_img.save(frame_path)

    # Encode with FFmpeg
    cmd = [
        "ffmpeg",
        "-y",
        "-framerate",
        str(fps),
        "-i",
        str(temp_dir / "frame_%04d.png"),
        "-vf",
        "format=yuv420p",
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "18",
        "-movflags",
        "+faststart",
        str(output_video),
    ]

    print(f"Encoding MP4: {output_video.name}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error encoding {output_video.name}:\n{res.stderr}", file=sys.stderr)
        raise RuntimeError("FFmpeg encoding failed")

    # Clean up temp frames
    import shutil
    shutil.rmtree(temp_dir, ignore_errors=True)
    print(f"Saved animated map: {output_video}")


def main() -> int:
    IMAGES_MAPS_DIR.mkdir(parents=True, exist_ok=True)
    VIDEOS_MAPS_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Generate High-Res Master Still Chart
    master_chart = draw_portolan_basemap(WIDTH, HEIGHT)
    master_still_path = IMAGES_MAPS_DIR / "portolan-chart-master.png"
    master_chart.save(master_still_path)
    print(f"Master Portolan Chart still saved: {master_still_path}")

    # 2. Render Animated Map Clip: Episode 01 (Lisbon to Cape Verde)
    vid_ep01 = VIDEOS_MAPS_DIR / "route-map-ep01-lisbon-to-cape-verde.mp4"
    render_animated_route_video("ep01", vid_ep01, duration_sec=8.0, fps=30)

    # 3. Render Animated Map Clip: Episode 02 (The Great South Atlantic Arc / Volta do Mar)
    vid_ep02 = VIDEOS_MAPS_DIR / "route-map-ep02-atlantic-volta-do-mar.mp4"
    if not vid_ep02.exists():
        render_animated_route_video("ep02", vid_ep02, duration_sec=12.0, fps=30)

    # 4. Render Animated Map Clip: Episode 03 (Cape of Good Hope & Mossel Bay)
    vid_ep03 = VIDEOS_MAPS_DIR / "route-map-ep03-cape-of-good-hope.mp4"
    render_animated_route_video("ep03", vid_ep03, duration_sec=10.0, fps=30)

    # 5. Render Animated Map Clip: Full Outward Voyage Master Overview (Lisbon to Calicut)
    vid_master = VIDEOS_MAPS_DIR / "route-map-master-voyage-overview.mp4"
    if not vid_master.exists():
        render_animated_route_video("full", vid_master, duration_sec=16.0, fps=30)

    print("\nAll animated nautical route maps generated successfully!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
