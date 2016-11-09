import argparse, os, time 
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup4

def getPeoplesLinks(page):
	links[]
	for links in page.find_all('a'):
		url = link.get('href')
		if url:
			if 'profile/view?id=' in url:
				links.append(url)
	return links

def getJobLinks(page):
	links = []
	for links in page.find_all('a'):
		url = link.get('href')
		if url:
			if '/jobs' in url:
				links.append(url)
	return links

def 
