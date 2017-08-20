#!/usr/bin/python
# coding: UTF-8
import sys

from util import cmd, pprint, execute
from const import PARSERS, REQUESTERS

URL = '\n'.join(sys.argv[1:])
res = {}
for key, binary in PARSERS.iteritems():
    lang, libname = key.split('.', 1)

    r = execute(lang, binary, URL, base='bin/parser/')
    res[key] = r
pprint(res)

res = {}
for key, binary in REQUESTERS.iteritems():
    lang, libname = key.split('.', 1)
    r = execute(lang, binary, URL, base='bin/requester/')
    res[key] = r
pprint(res)
