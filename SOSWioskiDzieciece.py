from flask import Flask, request, render_template
from PIL import Image
import requests
import os


app = Flask(__name__)
token = 'CAACEdEose0cBAADz6rHdZBvyZBvJGZAWHmqXCMaFB3ZCI1ZAk2VUtetOV90S7UKXipdoK7Mi74rH9RZBfwZCkZB6JwdDdmZB1ZA1nz54ZABQlCeClkoX49Ll8ZAmXfnBoW8HnGHJZCXl3qZCQYmTrNt4tGWa3CTZCVUDRC31qQn16Tm4nElKpWAbJ2TI1KF7AWuG99gYhNRupZCTDQgOOfWgjr0ZCQmds'

@app.route('/')
def hello_world():
    qs = 'https://graph.facebook.com/me/picture?type=square&height=3000&width=3000' + '&access_token='+token
    res = requests.get(qs)
    #print res.text
    photo_s = res.content
    photo = open('/Users/Marcin/PycharmProjects/SOSWioskiDzieciece/photo.jpg', 'w')
    photo.write(photo_s)
    photo.close()

    # photo = open('/Users/Marcin/PycharmProjects/SOSWioskiDzieciece', 'w')
    #print(photo)
    #photo.write(r.content)
    #photo.close()
    #print qs
    #print r.json()
    #image = Image.open(photo)
    #image.show()
    return render_template('templates.html')


if __name__ == '__main__':
    app.run()
