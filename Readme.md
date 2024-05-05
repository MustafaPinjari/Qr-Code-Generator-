# QR Code Generator

This Python program generates QR codes for different types of links such as web links, email addresses, and phone numbers.

## Requirements

- Python 3.x
- qrcode library (`pip install qrcode`)

## How to Run

1. Clone this repository or download the `qr_code_generator.py` file.
2. Navigate to the directory where `qr_code_generator.py` is located.
3. Open a terminal or command prompt.
4. Run the following command to execute the program:

6. Follow the prompts to enter the type of link (web, email, phone) and the specific link.
7. The program will generate a QR code and save it as `[link_type]_qr_code.png` in the same directory.

## Features

- Supports generating QR codes for web links, email addresses, and phone numbers.
- User-friendly interface with prompts for input.
- Automatically formats the content based on the link type.

## Example

Suppose you want to generate a QR code for a web link (e.g., https://www.example.com):
1. Run the program using the steps mentioned above.
2. Enter 'web' as the link type and 'https://www.example.com' as the link.
3. The program will generate a QR code and save it as `web_qr_code.png` in the same directory.

## Future Enhancements

- Support for more link types such as SMS, location coordinates, etc.
- GUI interface for a more interactive user experience.
- Error handling for invalid inputs.

Feel free to contribute to this project or provide feedback for improvements!
