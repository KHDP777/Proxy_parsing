import csv
import json
import requests
from bs4 import BeautifulSoup

def connect(url):
    headers = {
        "Accept": "image / avif, image / webp, * / *",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0"
        }
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    return soup


def main():
    global_count = 0
    # current_ip = {}
    page = 0
    for i in range(0, 720, 64):
        url = f"https://hidemy.name/ru/proxy-list/?type=h&start={i}#list"
        soup = connect(url)
        ip_adress = soup.find_all("tr")
        count = 0
        for item in ip_adress:
            if count != 0:
                global_count += 1
                list_of_td = item.find_all("td")
                current_ip ={
                    f"{global_count}": [{
                        "ip": list_of_td[0].text,
                        "port": list_of_td[1].text,
                        "country": list_of_td[2].find("span", class_="country").text,
                        "city":  list_of_td[2].find("span", class_="city").text,
                        "ping":  list_of_td[3].find("div", class_="bar").text,
                        "type": list_of_td[4].text,
                        "save": list_of_td[5].text,
                        "mark": list_of_td[6].text,
                    }]
                }
                # list_of_element = []
                # for key, value in current_ip[f"{global_count}"]:
                #     list_of_element.append(value)
                array = list(current_ip[f"{global_count}"][0].values())
                with open("all_date.json", "a") as file:
                    json.dump(current_ip, file, indent=4, ensure_ascii=False)
                with open(f"main.csv", "a", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        array
                    )
                # print(current_ip)
                # print(item)
            count += 1
        print(f"Страница {page} обработана...")
        page += 1
    print("END")


main()