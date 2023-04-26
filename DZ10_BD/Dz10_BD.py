from bs4 import BeautifulSoup
import requests,lxml,sqlite3 as sq

class DZ:
    def __init__(self):
        html = requests.get('https://meteoexpert.org/ru/forecast10/zaporizhzhia/', timeout=100)
        soup = BeautifulSoup(html.text, 'lxml')

        for c, i in zip(soup.select('.weekday'), soup.select(".desc")):
            self.c = c
            self.i = i
            print(c.text, '   ', i.text)
            # cur.execute(f'''
            #             INSERT INTO POGODA (time, pogodazp) VALUES ('{c.text}', '{i.text}');
            #             ''')


    def code_osnova(self):
        with sq.connect('POGODA.sl3', timeout=5) as con:
            cur = con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS POGODA(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time INTEGER DEFAULT "НЕ ИЗВЕСНО",
            pogodazp TEXT DEFAULT "НЕ ИЗВЕСНО"
            )''')
            p = self.c
            p1 = p.text

            g = self.i
            g1 = g.text
            cur.execute(f'''
                    INSERT INTO POGODA (time, pogodazp) VALUES ('{p1}', '{g1}');
                    ''')






if __name__ == "__main__":
    d = DZ()
    d.code_osnova()
    # code_osnova()