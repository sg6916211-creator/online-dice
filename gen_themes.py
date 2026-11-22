from PIL import Image, ImageDraw
import math

# theme -> (dark/primary color, light color) for a themed background
THEMES = {
    "blue":        ((0, 110, 230),   (241, 249, 255)),
    "sab-blue":    ((0, 120, 230),   (230, 245, 255)),
    "green":       ((0, 128, 0),     (224, 255, 224)),
    "sab-green":   ((0, 140, 40),    (220, 255, 220)),
    "red":         ((178, 34, 34),   (255, 224, 224)),
    "sab-red":     ((180, 20, 20),   (255, 214, 214)),
    "pink":        ((238, 90, 238),  (255, 224, 255)),
    "bw":          ((60, 60, 60),    (225, 225, 225)),
    "sab-black":   ((18, 18, 24),    (90, 90, 100)),
    "sab-heaven":  ((120, 190, 240), (255, 255, 255)),
    "sab-hell":    ((150, 20, 10),   (255, 160, 60)),
    "sab-underwater": ((0, 90, 140), (120, 220, 255)),
    "bronze":      ((140, 90, 50),   (255, 228, 190)),
    "silver":      ((110, 110, 120), (235, 235, 240)),
    "gold":        ((180, 140, 40),  (255, 245, 190)),
}

S = 512  # tile size

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))

def make_theme(name, c_dark, c_light):
    img = Image.new("RGB", (S, S))
    px = img.load()
    cx, cy = S*0.7, S*0.2   # light source top-right-ish
    for y in range(S):
        for x in range(S):
            # diagonal gradient dark -> light
            t = (x + y) / (2 * S)
            base = lerp(c_dark, c_light, t)
            # radial glow near the light corner
            d = math.sqrt((x - cx)**2 + (y - cy)**2) / S
            glow = max(0.0, 1.0 - d*1.4)
            col = lerp(base, (255, 255, 255), glow * 0.55)
            px[x, y] = col
    img.save(f"images/theme-{name}.png", "PNG")
    print(f"theme-{name}.png done")

for name, (d, l) in THEMES.items():
    make_theme(name, d, l)
