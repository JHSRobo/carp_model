import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import cv2
import time
from carp_regions import images

class CarpVideo(Node):
      
      def __init__(self):
        super().__init__('carp_video')
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.org = (50, 50)
        self.fontScale = 1
        self.color = (255, 0, 0)
        self.thickness = 2

      def show_images(self):
        #Go through CSV file and show images
        with open("carp.csv") as file:
            for line in file: 
                    row = line.rstrip().split(",")
                    image = cv2.imread(images[row[1]])
                    image = cv2.putText(image, row[0], self.org, self.font, self.fontScale, self.color, self.thickness, cv2.LINE_AA)
                    window_name = 'image'
                    cv2.imshow(window_name, image)
                    cv2.waitKey(1000)
                    cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    video = CarpVideo()
    video.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()