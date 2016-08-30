#coding:utf-8
# Last modified: 2016-08-30 14:02:15
# by zhangdi http://jondy.net/
import re

regxp = re.compile(r'^([\d\.]+)\s+([_\w\.\-]+)')

cmd = '/ip dns static add name=%s address=%s disabled=no'

namelist = []
for line in open('hosts').readlines():
  resp = regxp.findall(line) 
  if resp:
    ip, domain = resp[0]
    if domain not in namelist:
      print cmd % (domain, ip)
    namelist.append(domain)
