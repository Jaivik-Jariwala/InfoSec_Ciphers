#scraping the real website 
# make a http request and retreive the html content of web page and parse the html to ectreac the 
import requests
from bs4 import BeautifulSoup

#maker an http ge trequest
url =" "
response = requests.get(url) 

#parse html  
soup =/ BeautifulSoup(response.test, "html.parser")

#extract and print 
print("page title", soup.title.text)