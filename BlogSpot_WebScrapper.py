
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

	for head in soup2.find_all('div', class_='post hentry uncustomized-post-template'):

		heading = head.h3.text
		#writing heading to file
		fhandle.write(f'\n\n---------------------------------------------------------------------\n')
		fhandle.write(f'Heading {heading}\n')
	
		for i in soup2.find_all('div', class_='post-body entry-content'):
			i2 = i.text.replace('\n\n\n','\n').strip()
			#witing data
			fhandle.write(f'\n\n{i["id"]}\n{i2}')




