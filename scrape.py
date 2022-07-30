from bs4 import BeautifulSoup
from urllib.request import urlopen

base_url = "https://www.pensador.com"
page = urlopen(base_url + "/autor/platao/" )
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

while True:    
    phrases = soup.find_all("p", class_="frase")
    for phrase in phrases:
        print(phrase.text)    

    next_page = soup.find("a", class_="nav", text="Próxima >")
    if next_page is None:
        break
    url = next_page["href"]
    page = urlopen(base_url + url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

page.close()