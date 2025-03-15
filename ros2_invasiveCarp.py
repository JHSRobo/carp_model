import cv2
import rclpy
from rclpy.node import Node

class CarpVideo(Node):
    def __init__(self):
        super().__init__('carp_video')
        self.org = (50, 50)  # Origin point for text on images
        self.fontScale = 1  # Font scale for text
        self.color = (255, 0, 0)  # Color of the text (BGR format)
        self.thickness = 2  # Thickness of the text

    def show_images(self):
        # Go through CSV file and show images
        with open("carp.csv") as file:
            for line in file:
                row = line.rstrip().split(",")  # Split each line by comma
                image = cv2.imread(images[row[1]])  # Read the image file
                # Put text on the image
                image = cv2.putText(image, row[0], self.org, self.font, self.fontScale, self.color, self.thickness, cv2.LINE_AA)
                window_name = 'image'  # Window name for displaying images
                cv2.imshow(window_name, image)  # Display the image
                cv2.waitKey(1000)  # Wait for 1 second
                cv2.destroyAllWindows()  # Close the window

def main(args=None):
    rclpy.init(args=args)  # Initialize ROS 2 Python client library
    video = CarpVideo()  # Create an instance of CarpVideo
    video.show_images()  # Call the method to show images
    video.destroy_node()  # Destroy the node
    rclpy.shutdown()  # Shutdown ROS 2

if __name__ == '__main__':
    main()  # Run the main function
