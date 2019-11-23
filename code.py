from selenium import webdriver
from requests import get
from re import findall
import sys

def firstlevel(url,words):
    print(len(words))
    errors = 0
    for word,count in zip(words,range(len(words))):
        sys.stdout.write('{:.4f}% testes\r'.format(100*count/len(words)))
        url_ = url
        url_ += '/{}'.format(word)
        try:
            if get(url_).status_code == 200:
                print('caminho encontrado:\n{}'.format(url_))
        except:
            errors += 1
    print (errors)

def wl_from_site(url):
    words = []
    pg = webdriver.Chrome()
    pg.get(url)
    words += findall(r'\w+',pg.find_element_by_id("bodyContent").text)
    pg.close()
    return words

def wl_from_file(path):
    words = []
    f = open(path)
    words += findall(r'\w+',f.read())
    return words

def wl_clean(words):
    words = [w.lower() for w in words]
    words = list(dict.fromkeys(words))
    return words


url = r'http://weak-system-lab.lacunasoftware.com'

words = ['register', 'user', 'login', 'api', 'system', 'info', 'challenge','get','input', 'username', 'post', 'access']
words += ['bin', 'lib', 'tools', 'menu']

#words += wl_from_site(r'https://en.wikipedia.org/wiki/Computer_security')
#words += wl_from_site(r'https://en.wikipedia.org/wiki/Web_template_system')

words += wl_from_file('Filenames_or_Directories_Common.wordlist')

words = wl_clean(words)

words_found = ['api','system','secret','info']
url += '/{}'.format(words_found[0])
#url += '/{}'.format(words_found[1])
#url += '/{}'.format(words_found[3])

firstlevel(url,words)
