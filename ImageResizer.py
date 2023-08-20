import cv2
source = "aaaa.jpg"
destination = "newimage.jpg"

src = cv2.imread("aaaa.jpg", cv2.IMREAD_UNCHANGED)

#percent by which the image is resized
scale_percent = 60

#calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)
