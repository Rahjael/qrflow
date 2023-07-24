import qrcode
from PIL import Image

def generate_qr_code(data, filename, width, height):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")    
    img.save(filename)

    # Resize the image using PIL
    img = Image.open(filename)
    img.thumbnail((width, height))
    img.save(filename)






if __name__ == "__main__":
    # Example usage

    data = {
        "DOC": "FATT",
        "NUM": "425/FE",
        "DATE": "2023-07-21",
        "CODE": "EF8S89R0"
    }
    
    data_to_encode = data
    filename = "test.png"
    generate_qr_code(data_to_encode, filename)


