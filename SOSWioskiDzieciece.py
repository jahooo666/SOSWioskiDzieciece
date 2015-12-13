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
#app_url = '/matlaczm/SOS'
app = Flask(__name__)
app.debug = True


@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        token = request.form['token']
        uid = request.form['uid']
        qs = 'https://graph.facebook.com/'+ str(uid) +'/picture?type=square&height=3000&width=3000&?access_token=' + str(token)
        res = requests.request('GET', qs)
        #print(res.content)
        file = cStringIO.StringIO(res.content)
        img = Image.open(file)
        img = OverlayingImages.overlay(img)
        img.show()
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
        return render_template('facebook.html')


if __name__ == '__main__':
    app.run()