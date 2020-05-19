#from requests_html import HTMLSession
#from bs4 import BeautifulSoup
#from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#import time

def GetauthorAndTags():
    f=open("Address.txt","r")
    content=f.read()
    f.close()

    index=content.find('?ctx')
    url=content[:index]

    #print(content)
    print(url)

    if url=="":
        return ["", []]

    tags=[]

    if 'by' in url.split('-'):
        authorlist=url.split('-')[url.split('-').index('by')+1:]

        temporaryauthorlist=[]
        for name in authorlist:
            if "%" not in name:
                temporaryauthorlist.append(name)

        author = " ".join(temporaryauthorlist)
    else:
        author=""

    f=open("Address.txt","w")
    f.write("")
    f.close()

    return [author,tags]



results=GetauthorAndTags()
print("The author is "+results[0])
#print("The tags are "+str(results[1]))

