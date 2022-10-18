import sys      # Нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import os
import csv
import requests
from urllib.parse import quote
import design       # Это наш файл дизайна конвертированный pyuic5 design.ui -o design.py

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Для доступа к переменным, методам в файле design.py
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.pushButton_2.clicked.connect(self.file_save)
        self.pushButton_3.clicked.connect(self.file_open)
        self.pushButton.clicked.connect(self.resp)
        self.pushButton.clicked.connect(self.pars)
        self.pushButton_4.clicked.connect(self.open_file)


    def file_open(self):
        try:
            with open ('save.bin', 'r') as f:
                data = f.read().splitlines()
                self.textEdit_1.selfText(data[0])
                self.textEdit_2.selfText(data[1])
                self.textEdit_5.selfText(data[2])
        # Если нечего загружать
        except IndexError:
            pass

    def file_save(self):        # Функция сохранения настроек
        with open ('save.bin', 'w') as f:
            zapros = self.textEdit_1.toPlainText()
            org = self.textEdit_2.toPlainText()
            proxy = self.textEdit_5.toPlainText()
            f.write(f'{zapros}\n{org}\n{proxy}')

    def resp(self):
        result = self.textEdit_2.toPlainText()
        text = self.textEdit_1.toPlainText()
        qu = quote(text)
        proxy = self.textEdit_5.toPlainText()

        with requests.Session() as se:
            se.headers = {
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'en-US,en;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.62',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Referer': 'http://www.wikipedia.org/',
                'Connection': 'keep-alive',
            }

            response = requests.get('http://en.wikipedia.org/', headers=se.headers)

            # Возможность использовать прокси
            se.proxies = {
                "http": f"{proxy}",
                "https": f"{proxy}",
            }

            # получаем csrf токен
            resp = se.get('https://yandex.ru/maps/api/search?').json()
            csrf = resp.get('csrfToken')


            # Отправляем запрос и получаем ответ json
            self.item = se.get(f'https://yandex.ru/maps/api/search?add_type=direct&ajax=1&client_usecase=suggest&csrfToken=c6bd2e1f2d7e988035142c1f79d716774ec2d42a%3A1645445184&direct_page_id=670942&experimental%5B0%5D=rearr%3Dscheme_Local%2FGeo%2FStopInsaneChainFiltration%3D1&experimental%5B1%5D=rearr%3Dscheme_Local%2FGeo%2FRearrangeMovedOrgsUnderNew%3D1&experimental%5B2%5D=rearr%3Dscheme_Local%2FGeo%2FClosedDocsL3Coef%3D-0.01&experimental%5B3%5D=rearr%3Dscheme_Local%2FGeo%2FDisablePostfiltrationForMovedToOrgs%3D1&lang=ru_RU&ll=39.81041100000001%2C43.53367145768097&origin=maps-form&parent_reqid=1645464470728046-1151449557-man1-3794-man-addrs-nmeta-new-8031&results=25&s=2166097429&sessionId=1645445183915_708056&snippets=masstransit%2F2.x%2Cpanoramas%2F1.x%2Cbusinessrating%2F1.x%2Cbusinessimages%2F1.x%2Cphotos%2F2.x%2Cexperimental%2F1.x%2Csubtitle%2F1.x%2Cvisits_histogram%2F2.x%2Ctycoon_owners_personal%2F1.x%2Ctycoon_posts%2F1.x%2Crelated_adverts%2F1.x%2Crelated_adverts_1org%2F1.x%2Ccity_chains%2F1.x%2Croute_point%2F1.x%2Ctopplaces%2F1.x%2Cmetrika_snippets%2F1.x%2Cplace_summary%2F1.x%2Conline_snippets%2F1.x%2Cbuilding_info_experimental%2F1.x%2Cprovider_data%2F1.x%2Cservice_orgs_experimental%2F1.x%2Cbusiness_awards_experimental%2F1.x%2Cbusiness_filter%2F1.x%2Cattractions%2F1.x%2Cpotential_company_owners%3Auser%2Cpin_info%2F1.x%2Clavka%2F1.x%2Cbookings%2F1.x%2Cbookings_personal%2F1.x%2Cfuel%2F1.x%2Crealty_experimental%2F2.x%2Cmatchedobjects%2F1.x%2Cdiscovery%2F1.x%2Ctopobjects%2F1.x%2Chot_water%2F1.x%2Cshowtimes%2F1.x%2Cafisha_json_geozen%2F1.x%2Cencyclopedia%2F1.x%2Cstories_experimental%2F1.x%2Crealty_buildings%2F1.x&spn=3.036254692368999%2C0.289398863231213&suggest_reqid=1645467265044090-3377036268-suggest-maps-yp-12&test-buckets=492633%2C0%2C78%3B515131%2C0%2C48%3B515363%2C0%2C61%3B515930%2C0%2C27%3B519431%2C0%2C14%3B426572%2C0%2C13%3B518730%2C0%2C94%3B520557%2C0%2C33%3B497421%2C0%2C11%3B517273%2C0%2C65%3B511878%2C0%2C97%3B517353%2C0%2C78%3B521271%2C0%2C39&text=%D0%B5%D0%B4%D0%B0%20%D1%81%D0%BE%D1%87%D0%B8&yandex_gid=39&z=8.59').json()

            
    def pars(self):
        # получение списка организаций
        print(self.item)

        parser = self.item.get('data').get('items')

        # название организации
        names = ['Название']
        for name in parser:
            names.append(name.get('titel'))

        # статус доставки
        actions = ['Доставка']
        for action in parser:
            try:
                t = action.get('advert').get('actionButtons')
                for button in t:
                    if button.get('title') == 'Заказать доставку':
                        actions.append(button.get('value'))
                    else:
                        actions.append('-')
            except:
                actions.append('-')

        # адрес организации
        addr = ['Адрес']
        for address in parser:
            addr.append(address.get('description'))

        data = [names], [actions], [addr]

        # сохраняем в csv
        with open('data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerows(row)
        self.textBrowser.setText('Создан файл "data.csv".')

    # кнопка открытия файла
    def open_file(self):
        os.system('data.csv')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

# Компилирование: pyinstaller --noconsole --add-data "design.py;." --icon="logo.ico" --onefile main.py