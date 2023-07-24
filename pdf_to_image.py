import fitz
import os
from PIL import Image

def pdf_to_image(pdf_path, image_folder_path, single_image_filename=False, image_format='png', width=None, height=None):
    print('pdf_to_image: ')
    print('pdf: ', pdf_path)
    print('image folder: ', image_folder_path)



    if not single_image_filename:
        # Create output folder if it doesn't exist
        os.makedirs(image_folder_path, exist_ok=True)

    try:
        pdf_document = fitz.open(pdf_path)

        # Loop through each page in the PDF
        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]

            # Render page to a pixmap
            pixmap = page.get_pixmap()

            # Convert the pixmap to a PIL image (RGB)
            img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

            # Resize while maintaining aspect ratio
            if width or height:
                aspect_ratio = pixmap.width / pixmap.height
                if width:
                    new_height = int(width / aspect_ratio)
                    img.thumbnail((width, new_height))
                elif height:
                    new_width = int(height * aspect_ratio)
                    img.thumbnail((new_width, height))

            # Save each image with a unique name
            image_path = f"{image_folder_path}/image_{page_number}.{image_format}" if not single_image_filename else single_image_filename
            img.save(image_path)

            if single_image_filename:
                break

        pdf_document.close()
        print("PDF converted to images successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    # Example usage:
    pdf_file_path = "test_file.pdf"
    output_folder_path = "output_images"  # Folder to store images
    image_path = 'ttt.png'
    width = 200
    height = None  # Set to None to preserve proportions
    pdf_to_image(pdf_file_path, output_folder_path, single_image_filename=image_path, image_format='png', width=width, height=height)
