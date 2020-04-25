import requests
from bs4 import BeautifulSoup
import pprint

number_of_pages=3
res = requests.get(f"https://news.ycombinator.com/news?p={number_of_pages}")

soup = BeautifulSoup(res.text, "html.parser")

# Soup Basics

# to get all links in page soup.find_all("a")
# to get the first link in page soup.find("a")
# to get title of page soup.title
# to find all divs in page soup.find_all("div")
# to get an element whose id you know soup.find(id="<id>")
# if you are getting elements based on css then use soup.select instead of soup.find. For eg
# to find all elements which have a class="score" applied on them soup.select(".score")

links = soup.select(".storylink")
subtext = soup.select(".subtext")

def extractPoints(obj):
    return obj["points"]

def create_custom_hacker_news(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[index].select(".score")

        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))

            if points > 100:
                hn.append({"title": title, "link": href, "points": points})
    
    return sorted(hn, key=extractPoints, reverse=True)


pprint.pprint(create_custom_hacker_news(links, subtext)) 
