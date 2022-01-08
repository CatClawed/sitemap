import xml.etree.cElementTree as ET
import datetime

games = ['totori', 'escha', 'shallie', 'ryza2', 'bluereflection', 'second-light']

langs = {
    "totori": ["en", "ja"],
    "escha": ["en", "ja"],
    "shallie": ["en", "ja"],
    "ryza2": ["en", "fr", "ko", "ja", "sc", "tc"],
    "bluereflection": ["en"],
    "second-light": ["en", "ja", "sc", "tc"],
}

code = {
    "en":"en",
    "fr":"fr",
    "ko":"ko",
    "ja":"ja",
    "sc":"zh-Hans",
    "tc":"zh-Hant"
}

for game in games:

    urlset = ET.Element("urlset")
    urlset.set('xmlns','http://www.sitemaps.org/schemas/sitemap/0.9')
    urlset.set('xmlns:xhtml','http://www.w3.org/1999/xhtml')
    
    file = open("text/"+game+".txt", 'r')
    
    for line in file:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = 'https://barrelwisdom.com/{0}/{1}/{2}'.format(game, line.strip(), "en")
        for lang in langs[game]:
            l = ET.SubElement(url, 'xhtml:link')
            l.set('rel','alternate')
            l.set('hreflang',code[lang])
            l.set('href', 'https://barrelwisdom.com/{0}/{1}/{2}'.format(game, line.strip(), lang))
    
    tree = ET.ElementTree(urlset)
    tree.write("xmls/"+game+".xml", encoding='utf-8', xml_declaration=True)
    
file = open("text/"+'blog.txt','r')
urlset = ET.Element("urlset")
urlset.set('xmlns','http://www.sitemaps.org/schemas/sitemap/0.9')
for line in file:
    url = ET.SubElement(urlset, "url")
    ET.SubElement(url, "loc").text = 'https://barrelwisdom.com/{0}'.format(line.strip())

# main page
url = ET.SubElement(urlset, "url")
ET.SubElement(url, "loc").text = 'https://barrelwisdom.com/'
ET.SubElement(url, "changefreq").text = 'weekly'
ET.SubElement(url, "priority").text = '1.0'

tree = ET.ElementTree(urlset)
tree.write("xmls/blog.xml", encoding='utf-8', xml_declaration=True)

# sitemap index

index = ET.Element("sitemapindex")
index.set('xmlns','http://www.sitemaps.org/schemas/sitemap/0.9')

games.append('blog')

for game in games:
    sitemap = ET.SubElement(index, "sitemap")
    ET.SubElement(sitemap, 'loc').text = 'https://barrelwisdom.com/media/sitemaps/{0}.xml'.format(game)
    ET.SubElement(sitemap, 'lastmod').text = datetime.datetime.now().strftime("%Y-%m-%d")
    
tree = ET.ElementTree(index)
tree.write('xmls/sitemap.xml',encoding='utf-8', xml_declaration=True)