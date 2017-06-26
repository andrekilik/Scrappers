require 'rubygems'
require 'nokogiri'
require 'open-uri'
pageteste = 'http://mangafox.me/manga/'
#pageuse = 'http://www.mangafox.me/directory/'
page = Nokogiri::HTML(open(pageteste))
imglist = page.css('a.series_preview.manga_open a').map { |link| link['href'] }
#puts mangalist2
#teste = page.css('a')
#puts teste
#teste2 = page.css('li')
#puts teste2
#teste3 = page.css('li').css('a')
#puts teste3
#top_level = page.search('div#manga_list > ul > li > a')
#puts top_level
####### GETS JUST THE LINKS
mangalist2 = page.xpath('//div[@class="manga_list"]/ul/li/a').map { |link| link['href'] }


####### GETS JUST THE DESCRIPTIONS
test1 = page.xpath('//div[@class="manga_list"]/ul/li/a/text()').collect {|node| node.text.strip}
puts mangalist2[0]




####### MOUNTS A HASH WITH BOTH LINKS AND DESCRIPTIONS
#h = {}
#page.xpath('//div[@class="manga_list"]/ul/li/a').each do |link|
#  h[link.text.strip] = link['href']
#end


#puts h.values
#puts h.index(0)
#h.each_key do |key|
#  puts key
#end
##testl = page.xpath('//div[@class="manga_list"]/ul/li/a').map {|link| link['href']}
#puts testl