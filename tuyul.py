#usr/bin/python
"""Script Tuyul 100link.co 
    Bypass Captcha Code 
    Coded By : Mr_MSDV
    Github : https://github.com/mrmsdv"""
import requests ,mechanize
import os,sys
import time 
import bs4,json
from urllib import urlretrieve
import cookielib

link="http://trenbisnis.me/jlXdh"
capc = 'http://trenbisnis.me/captcha.php'
#get(link)


def eksek():
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_refresh(False)
    br.set_handle_robots(False)
    br.set_cookiejar(cookielib.LWPCookieJar())
    br.addheaders = [
    (
    "User-Agent","Mozilla/5.0 (Linux; U; Android 5.1)"
    )
    ]
    br.set_proxies({"84.2.35.44:80": "http", "1.62.68.201:6675": "http", "119.254.90.18:8080": "http"})         
    br.open('https://httpbin.org/ip')
    ad = bs4.BeautifulSoup(
    br.response().read(),
        features = "html.parser"
    )
    #print(ad)

    br.open(link)
    ab = bs4.BeautifulSoup(
    br.response().read(),
        features = "html.parser"
    )
    aw = ab.findAll('input')
    #print(aw)
    br.retrieve(capc,'anjay.jpg')
    os.system("tesseract anjay.jpg asu >/dev/null 2>&1")
    time.sleep(2)
    caps = open('asu.txt','r').read().splitlines()

    for i in caps:
        cap = i
        br.select_form(nr=0)
        br.form["captcha"] = "{}".format(cap)
        br.submit()
        ac = bs4.BeautifulSoup(
            br.response().read(),
                features = "html.parser"
            )
        print(cap)
        if "Captcha salah!" in str(ac):
            time.sleep(3)
            print(cap+' salah !!!')
            br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
            eksek()
        else:
            print(cap+' Benar ^_^')
            print(ac)
            exit()
eksek()
