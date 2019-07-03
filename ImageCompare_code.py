import cv2 
import numpy as np

#Original = cv2.imread("original1.jpg")
#Edited = cv2.imread("edited1.jpg")

# Card Image Compare
Original = cv2.imread("baseline_card.jpg")
Edited = cv2.imread("latest_card.jpg")
diff = cv2.subtract(Original, Edited)
cv2.imwrite("xray_card.jpg", diff)
im = cv2.imread("xray_card.jpg")
im1 = cv2.imread("latest_card.jpg")
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
thresh,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im1, contours, -1, (0,255,0), 2)
cv2.imwrite("compared_image_card.jpg", im1)

# Other Language Compare
Original = cv2.imread("baseline_chromeotherlang.jpg")
Edited = cv2.imread("latest_firefoxotherlang.jpg")
diff = cv2.subtract(Original, Edited)
cv2.imwrite("xray_otherlang.jpg", diff)
im = cv2.imread("xray_otherlang.jpg")
im1 = cv2.imread("latest_firefoxotherlang.jpg")
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
thresh,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im1, contours, -1, (0,255,0), 2)
cv2.imwrite("compared_image_otherLang.jpg", im1)

# Desktop Compare
Original = cv2.imread("baseline_desktop.jpg")
Edited = cv2.imread("latest_desktop.jpg")
diff = cv2.subtract(Original, Edited)
cv2.imwrite("xray_desktop.jpg", diff)
im = cv2.imread("xray_desktop.jpg")
im1 = cv2.imread("latest_desktop.jpg")
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#imgray = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
# new code inserted
# define range of blue color in HSV
#lower_blue = np.array([110,50,50])
#upper_blue = np.array([130,255,255])
ret,thresh = cv2.threshold(imgray,127,255,0)
#thresh = cv2.inRange(imgray,lower_blue,upper_blue)
thresh,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im1, contours, -1, (0,255,0), 2)
cv2.imwrite("compared_image_desktop.jpg", im1)

# Mobile Browser Compare
Original = cv2.imread("baseline_mobileBrowser.jpg")
Edited = cv2.imread("latest_mobileBrowser.jpg")
diff = cv2.subtract(Original, Edited)
cv2.imwrite("xray_mobile.jpg", diff)
im = cv2.imread("xray_mobile.jpg")
im1 = cv2.imread("latest_mobileBrowser.jpg")
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
thresh,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im1, contours, -1, (0,255,0), 2)
cv2.imwrite("compared_image_mobile.jpg", im1)


#### Old code
#diff = cv2.subtract(Original, Edited)
#cv2.imwrite("diff.jpg", diff)

#im = cv2.imread("diff.jpg")
#im1 = cv2.imread("edited1.jpg")

#imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(imgray,127,255,0)
#thresh,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#cv2.drawContours(im1, contours, -1, (0,255,0), 2)
#cv2.drawContours(im1, contours, -1, (0,255,0), 1)

#cv2.imwrite("see_this.jpg", im1)
#cv2.imwrite("ccmpared_image.jpg", im1)