from lxml import html
import collections
import requests
ind1 = 0
page = requests.get('http://mangafox.me/manga/')
tree = html.fromstring(page.text)
namelist = tree.xpath('//div[@class="manga_list"]/ul/li/a/text()')
linklist = tree.xpath('//div[@class="manga_list"]/ul/li/a/@href')
listall = collections.OrderedDict()
while ind1 < len(namelist):
	listall[namelist[ind1]] = linklist[ind1]
	ind1 += 1
print(listall[0])
#for k, v in listall.items():
#  print v