from PIL import Image, ImageDraw
import numpy as np

img = Image.open('assets/branding/logo_badge_perfect_square.png').convert("RGBA")
w, h = img.size

# Create a circle mask with anti-aliasing
mask = Image.new("L", (w, h), 0)
draw = ImageDraw.Draw(mask)
cx, cy = w // 2, h // 2
r = int(min(w, h) * 0.47)
draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=255)

# Gaussian blur the mask slightly for smooth antialiased edge
from PIL import ImageFilter
mask = mask.filter(ImageFilter.GaussianBlur(radius=1.5))

img.putalpha(mask)
img.save('assets/branding/logo_badge_clean_circle.png')
print("Clean circle badge saved: (w, h) =", img.size)
