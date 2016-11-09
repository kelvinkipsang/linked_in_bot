import argparse, os, time 
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def getPeoplesLinks(page):
    links=[]
    for links in page.find_all('a'):            #get a elements
        url = link.get('href')                  #hyperlink reference in a tags
        if url:
            if 'profile/view?id=' in url:       #look tor 'profile/v...' in the href
                links.append(url)               #add it to links list
    return links

def getJobLinks(page):
    links=[]
    for links in page.find_all('a'):             #same as above function
        url = link.get('href')
        if url:
            if '/jobs' in url:
                links.append(url)
    return links

def getID(url):
    pUrl = urlparse.urlparse(url)                       #parsed url
    return urlparse.parse_qs(pUrl.query)['id'][0]       # query parsed url by id

def ViewBot(browser):
    visited = {}   #store ids that we visited
    pList = [] #store ids that we plan to visit
    count=0
    while True:
        #sleep to make sure everything loads
        time.sleep(random.uniform(3.5,7.0))
        #source of current webpage
        page = BeautifulSoup(browser.page_source)
        people = getPeoplesLinks(page)  #people links in page
        if people:
            for person in people:
                ID = getID(person)
                if ID not in visited:
                    pList.append(person)
                    visited[ID] = 1
        if pList: #if there are people to visit,then visit
            person = pList.pop() #remove
            browser.get(person) #look for removed
            count += 1
        else:    #otherwise find people via job pages
            jobs =getJobLinks(page)  #from current page
            if jobs:
                job = random.choice(jobs)         #make sure they  
                root = 'http://www.linkedin.com' # have linked in
                roots = 'http://www.linkedin.com'#correct address
                if root not in job or roots not in job:
                    job = 'https://www.linkedin.com' +job #job link to go to
                browser.get(job)    #go to job webpage
            else:
                print "i'm lost...exiting"   #if no jobs on page
                break

        print "[+]" +browser.title+"Visited! \n ("\
        +str(count)+"/"+str(len(pList))+") Visited/Queue"
        #pages visited...how many
        #how many pages left to visit-pList
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("email", help="linkedin email")  #field that takes email   
    parser.add_argument("password", help="linkedin password") #takes password
    args = parser.parse_args()

    browser = webdriver.Chrome('/usr/bin/chromedriver')    #browser object
    browser.get("https://www.linkedin.com/uas/login")  #get login page

    emailElement = browser.find_element_by_id("session_key-login") #find element on login page using id
    emailElement.send_keys(args.email)   #type into field what we type
    passElement = browser.find_element_by_id("session_password-login")
    passElement.send_keys(args.password)
    passElement.submit()  #submit details

    os.system('clear')
    print "[+] You are logged in! Bot is Starting"
    ViewBot(browser)
    browser.close()

if __name__ == "__main__":
    Main()


