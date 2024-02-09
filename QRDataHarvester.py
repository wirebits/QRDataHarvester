#QRDataHarvester
#A tool which records the data from QR Code and save in the txt file.
#Author - WireBits

import argparse
from PIL import Image
from pyzbar.pyzbar import decode

def scan_qr_code(image_path, output_file):
    image = Image.open(image_path)
    
    image_format = image.format.lower()

    if image_format not in ["jpeg", "jpg", "png", "bmp"]:
        print("[-] Unsupported image format! Select JPEG, JPG, PNG or BMP only!")
        return

    decoded_data = decode(image)

    if len(decoded_data) > 0:
        qr_data = decoded_data[0].data.decode("utf-8")
        with open(output_file, "w") as file:
            file.write(qr_data)
        print("[+] QR code data saved to", output_file + "!")
    else:
        print("[+] No QR code found in the image!")

def main():
    parser = argparse.ArgumentParser(description="Scan a QR code from an image and save the extracted data to a text file.")
    parser.add_argument("-i", help="Path to the input image containing the QR code")
    parser.add_argument("-o", help="Path to the output text file")
    args = parser.parse_args()

    if any(arg is None for arg in (args.i, args.o)):
        print("[Usage]: python QRDataHarvester.py -i name_of_image.png -o name_of_text_file.txt")
        print("[Example]: python QRDataHarvester.py -i helloQR.png -o data.txt")
    else:
        try:
            scan_qr_code(args.i, args.o)
        except Exception as e:
            print("[-] Error:", str(e))

if __name__ == "__main__":
    main()