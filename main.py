from bs4 import BeautifulSoup
import requests

url = 'https://www.youtube.com/watch?v=QoyTUbVOmqo'

webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, "lxml")
meta = soup.find_all('meta', attrs={'property': 'og:video:tag'})
lst = []
for tag in meta:
    lst.append(tag.attrs['content'])
print(lst)
