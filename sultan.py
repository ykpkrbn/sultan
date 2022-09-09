from bs4 import BeautifulSoup as soup
from requests import get
import json


r = get("http://www.afyonaskf.com/puan-durumu/arsiv/2021-2022--2-amator-lig-b")
parser = soup(r.content, "html.parser")

table = parser.select_one("table.table-hover")

rows = table.select("tr")

data = [row.select("td") for row in rows[1:]]



boo = [

[_.text for _ in d] for d in \

data

]

teams = list()

for b in boo:
 d = dict(zip(["sirano", "takimadi", "oynanan_oyun", "galibiyet", "beraberlik", "maglubiyet", "attigi_gol", "yedigi_gol", "puan", "average"], b))
 teams.append(d)

json_data = json.dumps(str(teams))

with open("veriler.json", "w", encoding="utf8") as f:
     f.write(json_data)


print(teams)