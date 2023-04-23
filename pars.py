from bs4 import BeautifulSoup
import requests, json, lxml

def code():
    def convertor(deletet):
        n = input('Сколько гривен у нас есть')
        n1 = float(n)
        b1 = b[valuta]
        d = float(b1)
        d1 = d / deletet
        print(n1 * d1)



    headers = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }


    html = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
    soup = BeautifulSoup(html.text, 'lxml')

    b = {}

    for row in soup.select('tbody tr'):
        name = row.select_one('td:nth-child(4)').text.strip()
        of_rate = float(row.select_one('td:nth-child(5)').text.strip().replace(',', '.'))
        numb_za_valutu = float(row.select_one('td:nth-child(3)').text.strip().replace(',', '.'))

        b[name] = of_rate

    c = str(b.keys()).replace('dict_keys', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '')
    print('выберете валюту:',c)
    valuta = input('Выберете валюту в которую хотите перевести: ')

    if valuta in b:
        if valuta == 'Вона' or'Теньге' or 'Форинт':
            convertor(100)
        elif valuta == 'Єна' or 'Індійська рупія' or 'Російський рубль':
            convertor(10)
        elif valuta == 'Рупія':
            convertor(1000)
        else:
            convertor(1)

    print(valuta)
    print(numb_za_valutu)

if __name__ == "__main__":
    code()


