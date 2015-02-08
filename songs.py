#by somesh kumar :D
from bs4 import BeautifulSoup
import subprocess
from subprocess import call
import time

fp=open("index.html")
soup=BeautifulSoup(fp)
r1=soup.find_all('ul',{"class": "songs-list11"})
r2=r1[0].find_all('a')
links=[]
for i in range(1,len(r2)+1,2):
	links.append(r2[i]['href'])
print links

for each in links:
	each="www.songspk.name"+ each	
	call(["wget",each,"-O","url.html"])
	fp=open("url.html")
	soup=BeautifulSoup(fp)
	r1=soup.find_all('div',{"class":"song-title-bold"})
	r2=r1[1].find_all('a')
	st=r2[0]['href']
	st=st.replace(" ","%20")
	st=st.replace("[","%5B")
	st=st.replace("]","%5D")
	while True:
   		state=subprocess.check_output(["gnome-screensaver-command","--query"])
		state=state.strip()
   		if( not state == "The screensaver is inactive"):			
			time.sleep(60)
		else:call(["wget","-N",st,"-P","/home/somesh/Documents/scripts"]) 
			
#| grep -o "\w*active\w*" >> /dev/null
