#Crie um código em Python que teste se o site pudim esta acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Site NotOk!')
else:
    print('Site Ok!')
