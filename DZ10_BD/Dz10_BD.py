from bs4 import BeautifulSoup
import requests,lxml,sqlite3 as sq

def code_osnova():
    with sq.connect('POGODA.sl3', timeout=5) as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Roma(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time INTEGER DEFAULT "НЕ ИЗВЕСНО",
        pogodazp TEXT DEFAULT "НЕ ИЗВЕСНО"
        )''')

    html = requests.get('https://meteoexpert.org/ru/forecast10/zaporizhzhia/',timeout=100)
    soup = BeautifulSoup(html.text,'lxml')



    for c, i in zip(soup.select('.weekday'),soup.select(".desc")):
        print(c.text,'   ', i.text)
        cur.execute(f'''
                    INSERT INTO Roma (time, pogodazp) VALUES ('{c.text}', '{i.text}');
                    ''')


if __name__ == "__main__":
    code_osnova()