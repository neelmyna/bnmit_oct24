#pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

# URL of News Site
url = "https://www.bbc.com/news"
html_file_name = 'news_html.html'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
print(response.status_code)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    html = soup.prettify()
    print(type(html))
    print(html)

with open('news_webpage.html', 'w') as fp:
    for line in html:
        fp.write(line)

'''
fp = open('news_webpage.html', 'w')
fp.write("Purchase Amount: " 'TotalAmount')
fp.close()
'''