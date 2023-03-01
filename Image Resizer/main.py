from PIL import Image

import os


class ImageResizer:
    def __init__(self, input_path, output_path, size):
        self.input_path = input_path
        self.output_path = output_path
        self.size = size

    # method to resize images
    def resize_images(self):
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        for file_name in os.listdir(self.input_path):
            if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
                # Open the image file
                with Image.open(os.path.join(self.input_path, file_name)) as img:
                    # Resize the image
                    resized_img = img.resize(self.size, Image.LANCZOS)

                    # Save the resized image to output directory
                    resized_img.save(os.path.join(self.output_path, file_name))
                    print(f"{file_name} resized successfully!")

    def get_input():
        """Get user input for image resizer script."""
        # Get input directory
        input_dir = input("Enter input directory path: ")

        # Get output directory
        output_dir = input("Enter output directory path: ")

        # Get new image dimensions
        width = int(input("Enter new image width: "))
        height = int(input("Enter new image height: "))

        # Return input values as a tuple
        return input_dir, output_dir, (width, height)


if __name__ == '__main__':
    input_path = 'input'
    output_path = 'output'
    size = (800, 600)

    resizer = ImageResizer(input_path, output_path, size)
    resizer.resize_images()
