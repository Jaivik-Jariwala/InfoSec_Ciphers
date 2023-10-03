#find all elements by ID
from bs4 import BeautifulSoup

#sample html content 
html_content = "<div id='content><p>Hello, World</p></div>"

#parse the html
soup = BeautifulSoup(html_content,"html.parser")

#find the first div element witht the id attivute set to content 
div = soup.find("div",id="content")

#print the paragrpah
print(div.p.text)