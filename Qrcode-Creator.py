import qrcode
from PIL import Image

qr = qrcode.main.QRCode(version=1 , box_size= 10, border= 2 )
qr.add_data("https://github.com/Praneet-26")
qr.make(fit= True)

img = qr.make_image(fill = 'black', back_color='white')
img.save('PraneetGit.png')