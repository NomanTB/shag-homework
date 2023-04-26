from bs4 import BeautifulSoup
import requests,lxml,sqlite3 as sq

class DZ:
    def __init__(self):
        html = requests.get('https://meteoexpert.org/ru/forecast10/zaporizhzhia/', timeout=100)
        soup = BeautifulSoup(html.text, 'lxml')

        self.pogoda_and_time ={}

        for c, i in zip(soup.select('.weekday'), soup.select(".desc")):

            self.c = str(c).replace('<div class="weekday">', '').replace('</div>', '')
            self.i = str(i).replace('div', '').replace('</b>', '').replace('<b>', '').replace('<', '').replace('class="desc">', '').replace("</div>']", '')

            self.pogoda_and_time[self.c] = [self.i]


    def code_osnova(self):
        with sq.connect('POGODA.sl3', timeout=5) as con:
            cur = con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS POGODA(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time INTEGER DEFAULT "НЕ ИЗВЕСНО",
            pogodazp TEXT DEFAULT "НЕ ИЗВЕСНО"
            )''')

            for c, i in zip(self.pogoda_and_time.keys(),self.pogoda_and_time.values()):
                cur.execute(f'''
                            INSERT INTO POGODA (time, pogodazp) VALUES (\"%s\",\"%s\");
                            '''%(c,i))



if __name__ == "__main__":
    d = DZ()
    d.code_osnova()