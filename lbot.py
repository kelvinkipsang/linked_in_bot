import argparse, os, time 
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup4

def getPeoplesLinks(page):
	links[]
	for links in page.find_all('a'):            #get a elements
		url = link.get('href')                  #hyperlink reference in a tags
		if url:
			if 'profile/view?id=' in url:       #look tor 'profile/v...' in the href
				links.append(url)               #add it to links list
	return links

def getJobLinks(page):
	links = []
	for links in page.find_all('a'):             #same as above function
		url = link.get('href')
		if url:
			if '/jobs' in url:
				links.append(url)
	return links

def getID(url):
	pUrl = urlparse.urlparse(url)                       #parsed url
	return urlparse.parse_qs(pUrl.query)['id'][0]       # query parsed url by id

def Main():
	parser = argparse.Argumentparser()
	parser.add_argument("email", help="linkedin email")  #field that takes email   
	parser.add_argument("password", help="linkedin password") #takes password
	args = parser.parse_args()

	browser = webdriver.Chrome()    #browser object
	browser.get("https://www.linkedin.com/uas/login")  #get login page



