from pyquery import PyQuery as pq
#from lxml import etree
import urllib

d = pq(url='http://wiki.teamliquid.net/dota2/Wings_Gaming')

totalRows = len(d(".activesquad tr"))


for num in range(2,totalRows):
    name = d(".activesquad tr").eq(num).find('td').eq(2).html()
    nickname = d(".activesquad tr").eq(num).find('td a').eq(1).html()
    position = d(".activesquad tr").eq(num).find('td').eq(3).html()
    if str(d(".activesquad tr").eq(num).find('td').eq(1).find('img')).find("Captain") > -1:
        print "Captain"
    print nickname
    print name.strip()
    print position.strip()
    print "\n"
