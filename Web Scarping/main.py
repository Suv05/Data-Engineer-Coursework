import requests
from bs4 import BeautifulSoup

# Specify the URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/IBM'

response=requests.get(url)

# Store the HTML content in a variable
html_content=response.text

# Create a BeautifulSoup object to parse the HTML
soup=BeautifulSoup(html_content,'html.parser')

# Display a snippet of the HTML content
print(html_content[:500])

# Find all <a> tags (anchor tags) in the HTML
links=soup.find_all('a')

# Print the href attribute of each <a> tag
# for link in links:
#     print(link.text)
    
#print all h1 tags
for h1 in soup.find_all('h3'):
    print(h1.text)