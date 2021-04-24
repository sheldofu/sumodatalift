import requests;
import json;
import pprint;
from bs4 import BeautifulSoup

pp = pprint.PrettyPrinter()
URL = 'https://en.wikipedia.org/wiki/Tochinoshin_Tsuyoshi'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
recordTable = soup.find('table', class_='wikitable')
topRow = recordTable.find('tr')
monthsRow = topRow.find_all('th')
monthList = []
for months in monthsRow:
    bler = months
    pp.pprint(bler)
    monthList.append(bler)
# pp.pprint(monthList)
tournamentRecord = []
tournamentRecord.append({'tournament year': 2006, 'tournament month': 'may', 'wins': 9, 'losses': 6})

with open('sumo.json', 'w') as outsumo:
    json.dump(tournamentRecord, outsumo)