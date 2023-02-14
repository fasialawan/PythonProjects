import qrcode

# Get input from user
data = input("Enter the text to encode: ")

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
filename = "qr_code.png"
img.save(filename)
print(f"QR code saved to {filename}")
