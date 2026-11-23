import cv2
import numpy as np
from PIL import Image

# Load color logo
img = cv2.imread('assets/branding/logo_circle_fitted.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert and blur
inv = 255 - gray
blur = cv2.GaussianBlur(inv, (21, 21), 0)

# Color dodge to create pencil sketch
sketch = cv2.divide(gray, 255 - blur, scale=256)

# Enhance pencil lines with adaptive threshold
edges = cv2.Canny(gray, 50, 150)
kernel = np.ones((2, 2), np.uint8)
dilated_edges = cv2.dilate(edges, kernel, iterations=1)

# Combine sketch and edges
final_sketch = cv2.bitwise_and(sketch, 255 - dilated_edges)

# Apply paper tint
paper_tint = np.full_like(img, [240, 245, 248]) # BGR for ivory/cream paper
gray_3ch = cv2.cvtColor(final_sketch, cv2.COLOR_GRAY2BGR)
sketch_on_paper = cv2.multiply(gray_3ch, paper_tint, scale=1/255.0).astype(np.uint8)

cv2.imwrite('assets/branding/logo_sketch_lineart.png', sketch_on_paper)
print("Sketch line art saved successfully: assets/branding/logo_sketch_lineart.png")
