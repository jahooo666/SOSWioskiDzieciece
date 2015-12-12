from PIL import Image

#forgrBackgrRatio = 1/3 #stosunek wielkosci obrazka nakladanego do tla na ktore nakladamy
def overlay(photo):
    background = photo #w maksymalnej rozdzielczosci jaka sie uda pobrac
    foreground = Image.open("percent.png")

    bsize = background.size[0] #szerokosc ale i wysokosc bo bedziemy mieli kwadrat wiec luzik
    fsize = foreground.size[0]

    newFsize = bsize/3 #forgrBackgrRatio
    foreground = foreground.resize((newFsize,newFsize), Image.ANTIALIAS)#procent zresizowany do rozmiarow

    background.paste(foreground, (bsize-newFsize, bsize-newFsize), foreground)
    return background