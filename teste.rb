require 'rubygems'
require 'open-uri'
require 'nokogiri'
#variavel pagina inicial
pageteste = 'http://www.mangafox.me/directory/?az'
pageuse = 'http://www.mangafox.me/directory/'
ind1 = 2
#chama nokogiri para abrir pagina
page = Nokogiri::HTML(open(pageteste))
#pega lista de quantidade de paginas
pagelist = page.css('div#nav a').map {|link| link['href']}
#pega lista de links, mas também pega link para o primeiro capitulo direto
#linklist = page.css('div.manga_text a').map { |link| link['href'] }
#pega lista de imagens na pagina
imglist = page.css('a.manga_img img').map { |link| link['src'] }
#pega lista de links da pagina
mangalist2 = page.xpath('//div[@class="manga_text"]/a').map { |link| link['href'] }
#puts linklist
#coloca somente o primeiro elemento de cada na saida, remover o [0] para mostrar todos
#puts mangalist2[0]
#puts imglist[0]
linkstring = pagelist[-17].to_s
param = linkstring[3..9]
ultima = linkstring[0..2].to_i
puts param
puts ultima
until ind1 >= ultima do
      ativa = ind1.to_s
      atual = pageuse + ativa + param.to_s
      puts atual
      aberta = Nokogiri::HTML(open(atual))
      aberta_imglist = aberta.css('a.manga_img img').map { |link| link['src'] }
      aberta_mangalist2 = aberta.xpath('//div[@class="manga_text"]/a').map { |link| link['href'] }
      mangalist2 = mangalist2 + aberta_mangalist2
      #puts aberta_mangalist2
      ind1 += 1
end
#lastpage = pageuse + mystring
#puts lastpage
puts mangalist2
#puts pagelist[-17]