import qrcode

img = qrcode.make('http://google.com')
type(img)
img.save("hjkmile.png")
#Test statement