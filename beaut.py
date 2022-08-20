from bs4 import BeautifulSoup
import requests
with open('register1.html') as htmlf:
    soup=BeautifulSoup(htmlf,'lxml')
print(soup)    
