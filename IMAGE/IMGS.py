from PIL import Image,ImageFilter
before=Image.filter("hi.png")
after=before.filter(ImageFilter.BLUR)
after.save("out.png")

