# Play trending Videos

from bs4 import BeautifulSoup
import requests
import webbrowser
import subprocess

response = requests.get("https://www.youtube.com/feed/trending")

data = response.txt
soup = BeautifulSoup(data,"lxml")

#get all the header tags

i=0;
con = TRUE
while con == TRUE:
       l1=[]
       for link in soup.find_all("h3",{"class":"yt-lockup-title"}):
            for var in link.find_all("a"):
                    title =  var.get("title")
                    href = var.get("href")
                    print("Title[%s] = %s\n"%(i,title))
                    l1.insert(i,href)
                    i=i+1
                    
       choice = int(raw_input("Enter your choice of video or press -1"))
       select = l1[choice]
       link = "https://www.youtube.com"+select
