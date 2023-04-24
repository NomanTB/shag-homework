from bs4 import BeautifulSoup
import requests,lxml,sqlite3 as sq

def code_osnova():
    with sq.connect('pogoda.sl3', timeout=5) as con:
        cur = con.cursor()
        # cur.execute('''CREATE TABLE IF NOT EXISTS POGODA(
        # id INTEGER PRIMARY KEY AUTOINCREMENT,
        # time INTEGER DEFAULT "НЕ ИЗВЕСНО",
        # temperature INTEGER DEFAULT "НЕ ИЗВЕСНО"
        # )''')
    headers = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    html = requests.get('https://pogoda.meta.ua/world/ugorshhina/p-tf-rd-/month/',timeout=5)
    soup = BeautifulSoup(html.text,'lxml')

    print(html.status_code)
    # print(soup.select('.fl:nth-child(1)'))
    print(soup.get('.fl:nth-child(3) '))
    # print(html.text)




    # a = soup.select('div .month__wrap')
    # print(a)


if __name__ == "__main__":
    code_osnova()