from easygui import *
from lxml import html
import collections
import requests
ind1 = 0
page = requests.get('http://mangafox.me/manga/')
tree = html.fromstring(page.text)
namelist = tree.xpath('//div[@class="manga_list"]/ul/li/a/text()')
linklist = tree.xpath('//div[@class="manga_list"]/ul/li/a/@href')
listnum = collections.OrderedDict()
listall = collections.OrderedDict()
while ind1 < len(namelist):
	listnum[ind1] = namelist[ind1]
	listall[namelist[ind1]] = linklist[ind1]
	ind1 += 1
TITLE = "QG Loader"
msg ="Manga?"
choices = listnum.values()
choice = choicebox(msg, TITLE, choices)
if choice in choices:
  title = choice
  mangapage = requests.get(listall[choice])
  mangatree = html.fromstring(mangapage.text)
  print(mangatree)
  mangaimg = mangatree.xpath('//div[@class="cover"]/img/@src')
  print(mangaimg)
  ########VERIFICAR O COMANDO ABAIXO
  imageUrl = xhtml.xpath('//img[@alt="something"]')
  #image = mangaimg
  #msg = "Is this the manga?"
  #chaplist = mangatree.xpath('//a[@class="tips"]/@href')
  #choices2 = chaplist
  #choices2 = ["Yes","No"]
  #choice2 = buttonbox(msg, image=image, choices2)
