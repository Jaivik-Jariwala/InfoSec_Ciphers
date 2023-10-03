# extract attributes 
from bs4 import BeautifulSoup

#sample html content
html_content ="<a href='https://www.redbus.in/railways/search?src=BRC&dst=ST&doj=20230927&srcName=Vadodara&dstName=Surat%20-%20All%20Stations'>visit example</a>"

#Parse anchor
link = soup.a

print("link text", link.text)
print("linked url",link[:href])