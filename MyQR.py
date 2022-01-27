# This is a simple QRCode generator using python 
# You can generate QRCode for any image , for any text , for any link or for anything else using this generator.
# I have generated this QRCode for my linkedin account.
from distutils.log import ERROR
import qrcode 
import image
qr = qrcode.QRCode(
    version = 13, 
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border = 5,
)
# You can  give parameters according to your choice for version,box_size and border.
qr.add_data("https://www.linkedin.com/in/harshita-sharma-9805a2215") # You can give anything between quotes for which you want to generate QRCode.
qr.make(fit=True)
img = qr.make_image(fill_color="black",back_color="white") 
img.save('MyQR.png') # give file name that you want to give.
