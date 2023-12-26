from bs4 import BeautifulSoup as bs
import requests

# functions
def get_content_val(row_data):
    if row_data.find("li"):
        return [li.get_text(" ",strip=True).replace("\xa0", " ") for li in row_data.find_all("li")]
    else:
        return row_data.get_text(" ",strip=True).replace("\xa0", " ")

# retrieve content
r = requests.get("https://en.wikipedia.org/wiki/Good_Will_Hunting")
soup = bs(r.content)
info_box = soup.find(class_= "infobox vevent")
info_box_rows = info_box.find_all("tr")

movie_info = {}

for index, row in enumerate(info_box_rows):
    if index == 0:
        movie_info['title'] = row.find("th").get_text(" ",strip=True)
    elif index == 1:
        continue
    else:
        content_key = row.find("th").get_text(" ",strip=True)
        content_value = get_content_val(row.find("td"))
        movie_info[content_key] = content_value

print(movie_info)

