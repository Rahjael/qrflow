import fitz
from PIL import Image
import io






def pdf_to_image(pdf_path, image_folder_path, image_format='png', width=None, height=None):
    print('pdf_to_image: ')
    print('pdf: ', pdf_path)
    print('image folder: ', image_folder_path)
    try:
        pdf_document = fitz.open(pdf_path)

        print(pdf_document)

        # Loop through each page in the PDF
        for page_number in range(len(pdf_document)):
            print(page_number)
            page = pdf_document[page_number]
            image_list = page.get_images(full=True)

            for index, image in enumerate(image_list):
                # Get the image data
                image_bytes = image[6]

                # Create a PIL Image object from the image data
                pil_image = Image.open(io.BytesIO(image_bytes))

                if width or height:
                    pil_image.thumbnail((width, height))

                # Save each image with a unique name
                image_path = f"{image_folder_path}/image_{page_number}_{index}.{image_format}"
                pil_image.save(image_path)

        pdf_document.close()
        print("PDF converted to images successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    # Example usage:
    pdf_file_path = "test_file.pdf"
    output_folder_path = "output_images"  # Folder to store images
    width = 800
    height = None  # Set to None to preserve proportions
    pdf_to_image(pdf_file_path, output_folder_path, width=width, height=height)
