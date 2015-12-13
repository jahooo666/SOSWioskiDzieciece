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
token = "CAACEdEose0cBADVf0pe9CLFZAgXRZABGglRFmFgXb8u4u73xjnoqQNkTp6XYhCsZAn3tHbKc6mLxTS5jKboNfSmsFFJD7jGDJT5PVaeWZCfTQx673MCtufgspSbZCaXeKPGZBGsBP4jyOYYBQCpWC9ZBc1429272zpz6ldHRqnD6TFEd6H1GaZCtBqVoTJ6ogQw4ibp4gpnywQZDZD"
caly = '&access_token=' + token

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    qs = 'https://graph.facebook.com/me/picture?type=square&height=3000&width=3000' + caly
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
        print 'post'
        if request.form.get('submit')=='Wstaw zdjecie':
            #ponizej podejscie z tokenem i nawet adresem ustawionym na sztywno DZiala!
            #req = "https://graph.facebook.com/me/photos/?url=http://hodowanko.pl/application/assets/styles/common/images/piesel.png"+'&access_token=CAACEdEose0cBADVf0pe9CLFZAgXRZABGglRFmFgXb8u4u73xjnoqQNkTp6XYhCsZAn3tHbKc6mLxTS5jKboNfSmsFFJD7jGDJT5PVaeWZCfTQx673MCtufgspSbZCaXeKPGZBGsBP4jyOYYBQCpWC9ZBc1429272zpz6ldHRqnD6TFEd6H1GaZCtBqVoTJ6ogQw4ibp4gpnywQZDZD'

            req = "https://graph.facebook.com/me/photos/"+'&access_token=CAACEdEose0cBADVf0pe9CLFZAgXRZABGglRFmFgXb8u4u73xjnoqQNkTp6XYhCsZAn3tHbKc6mLxTS5jKboNfSmsFFJD7jGDJT5PVaeWZCfTQx673MCtufgspSbZCaXeKPGZBGsBP4jyOYYBQCpWC9ZBc1429272zpz6ldHRqnD6TFEd6H1GaZCtBqVoTJ6ogQw4ibp4gpnywQZDZD'

            url = "https://graph.facebook.com/me/photos/"
            header={'Authorization': 'access_token CAACEdEose0cBADVf0pe9CLFZAgXRZABGglRFmFgXb8u4u73xjnoqQNkTp6XYhCsZAn3tHbKc6mLxTS5jKboNfSmsFFJD7jGDJT5PVaeWZCfTQx673MCtufgspSbZCaXeKPGZBGsBP4jyOYYBQCpWC9ZBc1429272zpz6ldHRqnD6TFEd6H1GaZCtBqVoTJ6ogQw4ibp4gpnywQZDZD' }
            files={'profilowe.jpg': open('profilowe.jpg', 'rb')}

            r = requests.post(url,header,files)

            #r = requests.post(req, files={'profilowe.jpg': open('profilowe.jpg', 'rb')})
            #tak jak w linijce wyzej powinno sie wstawiac to jest gotowy request ale nie wiem czemu wywala ze nie ma tokena-probowalem na rozne sposoby i wszystkie sie jebia
            #r = requests.post(req)
            print r.content
            print r
            print "zmieniamy zdjecie"
        if request.form.get('submit')=='Dodaj post':
            print "dodajemy post"
        return render_template('operations.html')
    else:
        return render_template('operations.html')


if __name__ == '__main__':
    app.run()