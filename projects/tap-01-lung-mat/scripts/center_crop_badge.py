from PIL import Image
import numpy as np

img = Image.open('assets/branding/logo_ve_chuyen_hoang_da.png')
arr = np.array(img)

# Find coordinates of dark/colored pixels
bg_col = np.array([252, 245, 228])
diff = np.sqrt(np.sum((arr.astype(float) - bg_col)**2, axis=2))
mask = diff > 30

coords = np.argwhere(mask)
# Center of mass of the badge
cy = int(np.mean(coords[:, 0]))
cx = int(np.mean(coords[:, 1]))
print(f"Center of badge: cx={cx}, cy={cy}")

# Measure extent
min_y, min_x = coords.min(axis=0)
max_y, max_x = coords.max(axis=0)
radius = max(max_x - cx, cx - min_x, max_y - cy, cy - min_y) + 10
print(f"Radius: {radius}")

# Crop square around center
x0 = max(0, cx - radius)
y0 = max(0, cy - radius)
x1 = min(img.width, cx + radius)
y1 = min(img.height, cy + radius)

# Adjust to make exact square
w = x1 - x0
h = y1 - y0
side = max(w, h)
print(f"Square side: {side}")

badge_square = img.crop((cx - side//2, cy - side//2, cx + side//2, cy + side//2))
badge_square.save('assets/branding/logo_badge_perfect_square.png')
print("Saved perfect square badge:", badge_square.size)
