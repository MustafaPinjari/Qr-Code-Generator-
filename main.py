import qrcode

def generate_qr_code(link_type, link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Based on the link type, format the content accordingly
    if link_type == 'web':
        qr.add_data(link)
    elif link_type == 'email':
        qr.add_data(f"mailto:{link}")
    elif link_type == 'phone':
        qr.add_data(f"tel:{link}")
    else:
        print("Invalid link type!")
        return

    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white')

    # Save the QR code image
    qr_img.save(f'{link_type}_qr_code.png')
    print(f"QR code for {link_type} link generated and saved as {link_type}_qr_code.png")

if __name__ == "__main__":
    link_type = input("Enter the type of link (web, email, phone): ").lower()
    link = input("Enter the link: ")

    generate_qr_code(link_type, link)
  
