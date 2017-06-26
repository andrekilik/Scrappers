import io
from lxml import html
import collections
import requests
import PIL.Image
from PIL import ImageTk
from Tkinter import *
from urllib2 import urlopen
def get_list(event):
    """
    function to read the listbox selection
    and put the result in an entry widget
    """
    # get selected line index
    index = listbox1.curselection()[0]
    # get the line's text
    seltext = listbox1.get(index)
    mangapage = requests.get(listall[seltext])
    mangatree = html.fromstring(mangapage.text)
    imagem = mangatree.xpath('//div[@class="cover"]/img/@src')
    link = str(imagem)
    sizelink = len(link) - 2
    rlink = link[2:sizelink]
    image_bytes = urlopen(rlink).read()
    # internal data file
    data_stream = io.BytesIO(image_bytes)
    # open as a PIL image object
    pil_image = PIL.Image.open(data_stream)
    # optionally show image info
    # get the size of the image
    w, h = pil_image.size
    # split off image file name
    fname = rlink.split('/')[-1]
    sf = "{} ({}x{})".format(fname, w, h)
    root.title("Test Cover Display")
    # convert PIL image object to Tkinter PhotoImage object
    tk_image = ImageTk.PhotoImage(pil_image)
    # put the image on a typical widget
    label = Label(root, image=tk_image, bg='brown')
    label.config(image=tk_image)
    root.update_idletasks()
    root.after(0, get_list(event))
    #label.image = tk_image
    #label.place(x=10,y=650)
    #label.pack(padx=10, pady=65)
root = Tk()
ind1 = 0
page = requests.get('http://mangafox.me/manga/')
tree = html.fromstring(page.text)
namelist = tree.xpath('//div[@class="manga_list"]/ul/li/a/text()')
linklist = tree.xpath('//div[@class="manga_list"]/ul/li/a/@href')
listall = collections.OrderedDict()
listbox1 = Listbox(root,width=50,)
listbox1.place(x=10,y=100)
while ind1 < len(namelist):
  listbox1.insert(END, namelist[ind1])
  listall[namelist[ind1]] = linklist[ind1]
  ind1 += 1
scroll = Scrollbar(root, command=listbox1.yview)
listbox1.configure(yscrollcommand=scroll.set)
listbox1.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)
listbox1.bind('<ButtonRelease-1>', get_list)
root.mainloop()