#Import Library
import qrcode
import image
#Generate QR Code
img=qrcode.make('Hello World')
img.save('hello.png')