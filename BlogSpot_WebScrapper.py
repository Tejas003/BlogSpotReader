
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import re

#Getting a website of blogspot
main_site = input('Kindly Enter BlogSpot URL\n')
#months = list()
try:
	#trying to open the website if not it will quit program with below output
	url = urllib.request.urlopen(main_site).read()
except:
	print('Can\'nt open the URL')
	quit()


soup1 = BeautifulSoup(url,'lxml')


print('PLease find monthwise blog URL\'s below:\n')

for head in soup1.find_all('a', class_='post-count-link'):

	x = head['href']
	print(x,'\n')
		
print('\n\n')


#asking for destination folder
file = input('Enter file path to store the blogs\n')

while True:
	sub_site = input('Enter any of the above URLs to fetch the text\nDone to quit\n')
	if sub_site == 'Done':
		break

	date = re.findall('[0-9]+',sub_site)

	#forming a file name based on its year and month to store all blogs for that period
	try : 
		filepath = file + '/' + date.get(1) + '_'+ date[0] + '.txt'
	except:
		filepath = file + '/' +  date[0] + '.txt'

	#opening a file to create and write mode
	fhandle = open(filepath,'w+')

	#accesing new site
	try:
		url2 = urllib.request.urlopen(sub_site).read()
	except:
		continue

	soup2 = BeautifulSoup(url2,'lxml')

	divs = soup2.find_all('div', class_='post hentry uncustomized-post-template')

	for div in divs:
		divs2 = div.find('div', class_='post-body entry-content')
		h3 = div.find('h3', class_='post-title entry-title')
		h3text = h3.text

		text = divs2.text
		text = text.replace('\n\n\n','\n')

		#print('\n\----------------------------------------------------------------------n')
		#print(h3.text)
		#print(text)
		#print('\n\----------------------------------------------------------------------n')

		#witing data
		fhandle.write('\n\n---------------------------------------------------------------')
		fhandle.write(f'\n\n{h3.text}\n\n{text}')




