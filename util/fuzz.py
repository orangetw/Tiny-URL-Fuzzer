# coding: UTF-8

from urlparse import urlparse
import urllib, urllib2, httplib, requests

def my_urlparse(url):
    try:
        parsed = urlparse(url)
        if parsed.port:
            return 'scheme=%s, host=%s, port=%d' % (parsed.scheme, parsed.netloc, parsed.port)
        else:
            return 'scheme=%s, host=%s, port=' % (parsed.scheme, parsed.netloc)    
    except ValueError:
        return 'err'

def my_httplib(url):
    try:
        conn = httplib.HTTPConnection(urlparse(url).netloc)
        conn.request("GET", urlparse(url).path)
        data = conn.getresponse().read().strip()
        conn.close()
    except Exception:
        data = 'err'
    return data

def my_urllib(url):
    try:
        return urllib.urlopen(url).read().strip()
    except Exception:
        return 'err'

def my_urllib2(url):
    try:
        return urllib2.urlopen(url).read().strip()
    except Exception:
        return 'err'

def my_requests(url):
    try:
        return requests.get(url).content.strip()
    except Exception:
        return 'err'

