import os
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup
import json


url_base ='https://www.google.co.in/search?hl=en&tbm=isch&source=hp&biw=1366&bih=654&ei=_xC2XPnmE5bEvwScyYjACw&q={}&oq={}&gs_l=img.12..0l10.572.1915..4098...0.0..0.995.3494.2-1j1j0j2j2......0....1..gws-wiz-img.TOjImdqpwhU'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

def get_links(search_name):
    search_name = search_name.replace(' ', '+')
    url = url_base.format(search_name, search_name)
    request = ulib.Request(url, None, headers)
    data = ulib.urlopen(request).read()
    soup = Soup(data,'lxml')
    links=[]
    for img in soup.findAll('img'):
    	if 'fidget' in img.get('alt'):
    		links.append(img.get('src'))
    return links


def save_images(links, search_name):
    directory = search_name.replace(' ', '_')
    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i, link in enumerate(links):
    	savepath = os.path.join(directory, '{:06}.png'.format(i))
    	ulib.urlretrieve(link, savepath)


if __name__ == '__main__':
    search_name = 'fidget spinner'
    links = get_links(search_name)
    print(links)
