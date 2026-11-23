from PIL import Image
import numpy as np

im = Image.open('assets/branding/logo_ve_chuyen_hoang_da.png')
w, h = im.size
print("Width:", w, "Height:", h)

# Center of image is 512, 286.
# If radius is 275:
# x: 512-275 = 237, 512+275 = 787
# y: 286-275 = 11, 286+275 = 561
# Let's crop x from 225 to 799 (width 574), y from 0 to 572 (height 572)
# That's nearly 1:1!

cx = 512
cy = 286
r = 280

crop_box = (max(0, cx - r), max(0, cy - r), min(w, cx + r), min(h, cy + r))
print("Crop box:", crop_box)
cropped = im.crop(crop_box)
print("Cropped size:", cropped.size)
cropped.save('assets/branding/logo_circle_fitted.png')
