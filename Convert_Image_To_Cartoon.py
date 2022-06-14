
import cv2 as cv
import os

#create file path 
file_dir = "C:\\Users\\USER\\Pictures"
file_name = input("Enter your name images: ".upper())
file_path = os.path.join(file_dir, file_name)

#reading image
image = cv.imread(file_path)

#conversion code
Image_convert = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

gray = cv.medianBlur(Image_convert,5)
edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,5)

#using bilateralFilter to filter color
color = cv.bilateralFilter(image, 9, 250,250)
#color2 = cv.bilateralFilter(image, 20, 450, 450)

#combine two color for to display color for cartoon image
cartoon = cv.bitwise_and(color, color, mask=edges)

print("----------------------------------------------------------")
input_filename = input("Input file name you want to save: ".upper())
saving =  cv.imwrite(os.path.join(file_dir, input_filename), cartoon)

#display image
cv.imshow("Image",image)
cv.imshow("Cartoon",cartoon)
#------------------------------------------------------------------#
if saving ==True:
    print("--------------------------------")
    print("Image is saved successfully\n")
else:
    print("--------------------------------")
    print("Not Success when saving\n")

#stop screen no limit time
cv.waitKey(0)
