from PIL import Image, ImageChops
import numpy as np

img = Image.open('assets/branding/logo_ve_chuyen_hoang_da.png')
print("Original size:", img.size)

# Find bounding box of the circular badge
# The background is ivory/off-white around (248, 245, 237)
arr = np.array(img)
# Sample corners for background color
bg_col = np.mean([arr[0, 0], arr[0, -1], arr[-1, 0], arr[-1, -1]], axis=0)
print("Background sample color:", bg_col)

# Distance from background
diff = np.sqrt(np.sum((arr.astype(float) - bg_col)**2, axis=2))
mask = diff > 25

# Find bounding box
coords = np.argwhere(mask)
y0, x0 = coords.min(axis=0)
y1, x1 = coords.max(axis=0)
print(f"Bounding box: x={x0}..{x1}, y={y0}..{y1} (w={x1-x0}, h={y1-y0})")

# Crop badge with small margin
margin = 15
crop_x0 = max(0, x0 - margin)
crop_y0 = max(0, y0 - margin)
crop_x1 = min(img.width, x1 + margin)
crop_y1 = min(img.height, y1 + margin)

cropped = img.crop((crop_x0, crop_y0, crop_x1, crop_y1))
cropped.save('assets/branding/logo_badge_square.png')
print(f"Cropped square logo saved: {cropped.size}")

# Create clean circular cutout with transparency
# If we want a clean transparent circular badge
w, h = cropped.size
crop_arr = np.array(cropped.convert("RGBA"))
# Soft edge transparency mask based on color distance from background
crop_diff = np.sqrt(np.sum((crop_arr[:, :, :3].astype(float) - bg_col)**2, axis=2))
alpha = np.clip((crop_diff - 15) / 25 * 255, 0, 255).astype(np.uint8)

# Keep the inside of the circle opaque (the badge itself has white/cream background inside)
# Find circle center and radius
cy, cx = h / 2.0, w / 2.0
r = min(w, h) * 0.49
y_grid, x_grid = np.ogrid[:h, :w]
dist_from_center = np.sqrt((x_grid - cx)**2 + (y_grid - cy)**2)

# Inside the circle (dist < r), alpha is 255. Outside, alpha drops to 0 smoothly.
circle_alpha = np.clip((r + 4 - dist_from_center) / 6.0 * 255, 0, 255).astype(np.uint8)

crop_arr[:, :, 3] = circle_alpha
clean_badge = Image.fromarray(crop_arr)
clean_badge.save('assets/branding/logo_badge_transparent.png')
print("Saved clean circular transparent logo:", clean_badge.size)
