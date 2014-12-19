from collections import Counter as C
import urllib2
import nltk

urls=[]
with open('manisourcehtml1.html','r+') as f:
	urls=map(lambda x:"http://en.wikipedia.org"+x[13:x.index('" title')],filter(lambda x:x.startswith('<td><a href="/wiki/') and '(' not in x,f.readlines()))
print urls
 
import pdb
pdb.set_trace()
c=C()
with open('manibackup1.txt','w+') as f:
	for url in urls:
		raw=nltk.clean_html(urllib2.urlopen(url).read())
		if '^' in raw:
			raw=raw[:raw.index('^')]
		raws=raw.split();
		print url
		c.update(C(filter(lambda x:all(map(str.isalpha,x)) and len(x)>3,map(lambda x:str.lower(x),\
		raws))))
	f.write(str(c))