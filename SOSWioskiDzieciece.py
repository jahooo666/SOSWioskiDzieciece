import cStringIO
import os
import tempfile
import urllib
from base64 import b64encode

import math
from flask import Flask, request, render_template
from PIL import Image
import requests
import OverlayingImages

app = Flask(__name__)
app.debug = True
token = "CAACIe34ksn8BAO3pPCorbzHlbfMSYTYJL0p1ieCY0tO6OCKZB3UpudXxX0sGZBlZAwQBai5SClEVY1H3g7faQl3PbNU5sI1cj6ny4FGVp7hCYB1GAKX2xkAaV580UzsSZApEvgwzn9sq746CaOGvZCVoZAGpQHaklxrfAM6RwO2dSeJnyxPfGcDXoBv0pmWKulHZAxQf48H9wZDZD"


@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    qs = 'https://graph.facebook.com/me/picture?type=square&height=3000&width=3000' + '&access_token=CAACIe34ksn8BAO3pPCorbzHlbfMSYTYJL0p1ieCY0tO6OCKZB3UpudXxX0sGZBlZAwQBai5SClEVY1H3g7faQl3PbNU5sI1cj6ny4FGVp7hCYB1GAKX2xkAaV580UzsSZApEvgwzn9sq746CaOGvZCVoZAGpQHaklxrfAM6RwO2dSeJnyxPfGcDXoBv0pmWKulHZAxQf48H9wZDZD'
    res = requests.request('GET', qs)
    file = cStringIO.StringIO(res.content)
    img = Image.open(file)
    img = OverlayingImages.overlay(img)
    tmp = tempfile.mktemp(suffix='.jpg', dir='./')
    img.save(tmp)
    image = open(tmp, 'rb')

    img = image.read()
    trueImage = b64encode( img )

    image.close()
    os.remove(tmp)
    return render_template('templates.html', trueImage = trueImage )

@app.route('/token', methods=['GET', 'POST'])
def token():
    if request.method == 'POST':
        if request.form.get('submit')=='Wstaw zdjecie':
            print "zmieniamy zdjecie"
        if request.form.get('submit')=='Dodaj post':
            print "dodajemy post"
        return render_template('operations.html')
    else:
        return render_template('operations.html')


if __name__ == '__main__':
    app.run()