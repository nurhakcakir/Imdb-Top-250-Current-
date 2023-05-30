import requests
from bs4 import BeautifulSoup
ImdbUrl= "https://www.imdb.com/chart/top/"

r= requests.get(ImdbUrl)
soup=BeautifulSoup(r.content,"html.parser")
incoming_data = soup.find_all("table",{"class":"chart full-width"} )
film_table=(incoming_data[0].contents)[len(incoming_data[0].contents)-2]

film_table=film_table.find_all("tr")

for film in film_table:
    film_titles=film.find_all("td",{"class":"titleColumn"})
    film_name=film_titles[0].text
    film_name=film_name.replace("\n","")

    print(film_name)
    print("*************************************")