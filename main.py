import requests;
import json;
import pprint;
from bs4 import BeautifulSoup, NavigableString

pp = pprint.PrettyPrinter()
URL = 'https://en.wikipedia.org/wiki/Tochinoshin_Tsuyoshi'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
recordTable = soup.find('table', class_='wikitable')
topRow = recordTable.find('tr')
monthsRow = topRow.find_all('th')
tournamentRecord = []
monthList = []
locationList = []
yearList = []
rankList = []
recordList = []

for months in monthsRow:
    spanSelection = months.find('span')
    if spanSelection == None:
        continue
    spanSaved = spanSelection.extract()
    location = spanSaved.find('a')
    locationList.append(location.text)
    monthList.append(months.text)
# pp.pprint(monthList)
# pp.pprint(locationList)

for resultsRow in topRow.next_siblings:
    year = resultsRow.find('th')
    if isinstance(year , int) or year == None:
        continue
    # print(year.text)
    yearList.append(year.text)
    tournamentCells = resultsRow.find_all('td')
    # pp.pprint(tournamentCells)
    for tournamentCell in tournamentCells:
        tournament = tournamentCell.find('span')
        if tournament == None:
            continue
        # rankList.append(tournament.text)
        record = tournament.next_sibling.next_sibling
        if isinstance(record, NavigableString):
            continue
        pp.pprint(record.text)
        recordList.append({'tournament':tournament.text,'record':record.text})

pp.pprint(rankList)


for y in yearList:
    for m in monthList:
        for r in recordList:
            tournamentRecord.append({'tournament year': y, 'tournament month': m, 'record': r })

with open('sumo.json', 'w') as outsumo:
    json.dump(tournamentRecord, outsumo)