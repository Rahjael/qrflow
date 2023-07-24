import qrcode


def generate_qr_code(data, filename):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
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


