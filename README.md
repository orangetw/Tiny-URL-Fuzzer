# Tiny URL Fuzzer

A tiny and cute URL fuzzer in my talk of [Black Hat USA 2017](https://www.blackhat.com/us-17/speakers/Orange-Tsai.html) and [DEFCON 25](https://www.defcon.org/html/defcon-25/dc-25-speakers.html). 

Slides:

* [A New Era of SSRF - Exploiting URL Parser in Trending Programming Languages!](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)

Case Study:

* [How I Chained 4 vulnerabilities on GitHub Enterprise, From SSRF Execution Chain to RCE!](http://blog.orange.tw/2017/07/how-i-chained-4-vulnerabilities-on.html)


# How to use?

All the code are written for hackers. Read the source! Some URL samples you can check [samples.txt](samples.txt)


### Install / Restore
```bash
$ run_me.py install
$ run_me.py restore
```

### Try
```bash
$ try.py http://127.0.0.1

Go.net/url               scheme=http, host=127.0.0.1, port=
Java.net.URL             scheme=http, host=127.0.0.1, port=-1
NodeJS.url               scheme=http, host=127.0.0.1, port=
PHP.parseurl             scheme=http, host=127.0.0.1, port=
Perl.URI                 scheme=http, host=127.0.0.1, port=80
Python.urlparse          scheme=http, host=127.0.0.1, port=
Ruby.addressable/uri     scheme=http, host=127.0.0.1, port=
Ruby.uri                 scheme=http, host=127.0.0.1, port=80


Go.net/http              127.0.0.1:80/
Java.URL                 127.0.0.1:80/
NodeJS.http              127.0.0.1:80/
PHP.curl                 127.0.0.1:80/
PHP.open                 127.0.0.1:80/
Perl.LWP                 127.0.0.1:80/
Python.httplib           127.0.0.1:80/
Python.requests          127.0.0.1:80/
Python.urllib            127.0.0.1:80/
Python.urllib2           127.0.0.1:80/
Ruby.Net/HTTP            127.0.0.1:80/
Ruby.open_uri            127.0.0.1:80/
```

### Fuzz
```bash
$ fuzz.py
```
