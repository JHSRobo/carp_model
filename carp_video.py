import cv2
import time

#Associate region number with image
regions = {
    "0": r'C:\Users\jonah\Downloads\Region 0.jpg',
    "1": r'C:\Users\jonah\Downloads\Region 1.jpg',
    "2": r'C:\Users\jonah\Downloads\Region 2.jpg',
    "3": r'C:\Users\jonah\Downloads\Region 3.jpg',
    "4": r'C:\Users\jonah\Downloads\Region 4.jpg',
    "5": r'C:\Users\jonah\Downloads\Region 5.jpg',
}

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2

#Go through CSV file and show images
with open("carp.csv") as file:
   	for line in file: 
            row = line.rstrip().split(",")
            image = cv2.imread(regions[row[1]])
            image = cv2.putText(image, row[0], org, font, fontScale, color, thickness, cv2.LINE_AA)
            window_name = 'image'
            cv2.imshow(window_name, image)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()