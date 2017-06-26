from lxml import html
import requests
import collections
page = requests.get('http://mangafox.me/manga/')
tree = html.fromstring(page.text)
namelist = tree.xpath('//div[@class="manga_list"]/ul/li/a/text()')
linklist = tree.xpath('//div[@class="manga_list"]/ul/li/a/@href')
#print len(linklist)
ind1 = 0


#pega imagem na pagina interna do manga
#imagem = tree.xpath('//div[@class="cover"]/img/@src')

#pega descricao na pagina interna do manga, caso nao tenha warning
#namelist = tree.xpath('//div[@id="title"]/p/text()')


listnum = collections.OrderedDict()
listall = collections.OrderedDict()
while ind1 < len(namelist):
	#print "Name", namelist[ind1]
	#print "Link", linklist[ind1]
	listnum[ind1] = namelist[ind1]
	listall[namelist[ind1]] = linklist[ind1]
	ind1 += 1
print(listall[listnum[0]])

