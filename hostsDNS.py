#coding:utf-8
# Last modified: 2016-08-28 01:01:14
# by zhangdi http://jondy.net/
from twisted.internet import reactor, defer
from twisted.names import client, dns, error, server
import os.path
import re

regxp = re.compile(r'^([\d\.]+)\s+([_\w\.\-]+)')

class hostsResolver(object):
  def __init__(self, hosts):
    self.hosts = hosts

  def _hostsResponse(self, query):
    name = query.name.name
    print 'resolve:', name, self.hosts.get(name)
    answer = dns.RRHeader(name=name,payload=dns.Record_A(address=self.hosts.get(name)))
    return [answer], [], []

  def query(self, query, timeout=None):
    if query.name.name in self.hosts.keys():
      return defer.succeed(self._hostsResponse(query))
    else:
      return defer.fail(error.DomainError())

def main():
  hosts = dict()
  hostsfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hosts')
  for line in open(hostsfile).readlines():
    resp = regxp.findall(line)
    if resp:
      hosts[resp[0][1]] = resp[0][0]
  factory = server.DNSServerFactory(
    clients=[hostsResolver(hosts), client.Resolver(servers=[('8.8.8.8', 53)])]
  )
  protocol = dns.DNSDatagramProtocol(controller=factory)
  reactor.listenUDP(53, protocol)
  reactor.listenTCP(53, factory)
  reactor.run()

if __name__ == '__main__':
  raise SystemExit(main())
