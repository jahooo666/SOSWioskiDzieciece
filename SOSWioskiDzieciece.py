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
token = 'CAACEdEose0cBAJuQXTZB0vlgFCMb4TsW6OWX9Rn71Hm9djZCSclPisYQKk934CQj3vqSjdTdnXNrV8vwM7v8PAYlLVtmYNuMdmToZCYNEVAVdYkZBMRTOnWDs712LhFK466YapSUftEkgPIMIis7LZClHLi5sG3X5OUoY2AmsK4Es8o9p1GZBs79ZAhVAQS0QCUZBPml6i9W1HkzZCvorm5BD'


@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    qs = 'https://graph.facebook.com/me/picture?type=square&height=3000&width=3000' + '&access_token=' + token
    res = requests.request('GET', qs)
    file = cStringIO.StringIO(res.content)
    img = Image.open(file)
    img = OverlayingImages.overlay(img)
    tmp = tempfile.mktemp(suffix='.jpg', dir='./')
    img.save(tmp)
    image = open(tmp, 'rb')
    img = image.read()
    os.remove('./' + tmp)
    trueImage = b64encode( img )


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