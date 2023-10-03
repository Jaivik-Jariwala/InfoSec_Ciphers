!pip install bs4
!pip install BeautifulSoup
#navigate the html tree
from bs4 import BeautifulSoup

#sample html content 
html_content = "<div><p>parapgraph 1</p><>Paragraph 2</p></div>"

#parse the html 
soup = BeautifulSoup(html_content, "html.parser")

#navigate the html tree 
d = soup.div 
for p in d.find_all("p"):
    print(p.text)