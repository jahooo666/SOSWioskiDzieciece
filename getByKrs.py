from bs4 import BeautifulSoup
import urllib2

def getOrganisationInfo(krsNumber):

    query = 'https://api.mojepanstwo.pl/krs/podmioty?conditions[krs]=' + str(krsNumber)
    response = urllib2.urlopen('https://api.mojepanstwo.pl/krs/podmioty?conditions[krs]=' + str(krsNumber))

    html = response.read()
    print(html)

getOrganisationInfo(krsNumber = '0000056901')
