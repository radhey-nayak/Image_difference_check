"""Auth: Radhashyam Nayak"""
import cv2

prev_img = cv2.imread("old1.jpg", 1)
new_img = cv2.imread("new1.jpg", 1)

old_img_resize = cv2.resize(prev_img, (500, 500))
new_img_resize = cv2.resize(new_img, (500, 500))

diff = cv2.absdiff(old_img_resize, new_img_resize)

# Converting To Gray Scale
gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

# Converting Gray Image To Blur Image For Perfect Result
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Thresshold
_, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

# Itaration
dilated = cv2.dilate(thresh, None, iterations=3)

# Contours
contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop
for contour in contours:

    # for creating boxes On The Moving Object: 1
    #(x, y, w, h) = cv2.boundingRect(contour)

    # Checking Contour area
    if cv2.contourArea(contour) < 500:
        continue

    # for creating boxes On The Moving Object: 1
    #cv2.rectangle(old_img_resize, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #cv2.rectangle(new_img_resize, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Drawing Contour
    cv2.drawContours(old_img_resize, contour, -1, (255, 0, 0), 3)
    cv2.drawContours(new_img_resize, contour, -1, (255, 0, 0), 3)

    # Printing Text On Frames
    cv2.putText(old_img_resize, "OLD IMAGE STATUS: {}".format("movement"), (10, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                1, (0, 0, 255), 1)
    cv2.putText(new_img_resize, "NEW IMAGE STATUS: {}".format("movement"), (10, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                1, (0, 0, 255), 1)

cv2.imshow("Old Image", old_img_resize)
cv2.imshow("New Image", new_img_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()
