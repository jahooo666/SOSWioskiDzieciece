import Image

background = Image.open("progilowe.jpg")
foreground = Image.open("percent.png")

background.paste(foreground, (0, 0), foreground)
background.show()