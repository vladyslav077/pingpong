import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QPixmap
import requests
from datetime import datetime


class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Weather')
        self.setGeometry(100, 100, 400, 300)

        self.label_city = QLabel('Місто:', self)
        self.label_city.move(10, 10)

        self.city_combo = QComboBox(self)
        self.city_combo.move(70, 10)
        self.city_combo.addItem("Київ")
        self.city_combo.addItem("Львів")
        self.city_combo.addItem("Одеса")
        self.city_combo.addItem("Харків")
        self.city_combo.addItem("Варшава")
        self.city_combo.addItem("Миколаїв")
        self.city_combo.addItem("Ужгород")
        self.city_combo.addItem("Новояворівськ")
        self.city_combo.addItem("Прилбичі")
        self.city_combo.addItem("Лондон")
        self.city_combo.addItem("Нью-Йорк")
        self.city_combo.addItem("Донецьк")
        self.city_combo.addItem("Маріуполь")
        self.city_combo.addItem("Дубай")
        self.city_combo.currentIndexChanged.connect(self.get_weather)



        self.update_button = QPushButton('Оновити', self)
        self.update_button.setObjectName("update_button")
        self.update_button.move(150, 50)
        self.update_button.clicked.connect(self.update_weather)

        self.weather_label = QLabel('', self)
        self.weather_label.setGeometry(10, 70, 380, 150)
        self.weather_label.setStyleSheet("font-size: 16px;")

        self.icon_label = QLabel(self)
        self.icon_label.setGeometry(250, 10, 130, 130)

        self.last_update_label = QLabel('', self)
        self.last_update_label.move(10, 230)

        self.get_weather()

    def get_weather(self):
        api_key = 'f81703c1f3b81ad93e6644153c4a426e'
        city = self.city_combo.currentText()
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            icon_name = data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/w/{icon_name}.png"

            weather_text = f'Погода: {weather}\nТемпература: {temperature}°C\nВологість: {humidity}%\nШвидкість вітру: {wind_speed} м/с'
            self.weather_label.setText(weather_text)

            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(icon_url).content)
            self.icon_label.setPixmap(pixmap)

            now = datetime.now()
            formatted_date = now.strftime("%d.%m.%Y %H:%M:%S")
            self.last_update_label.setText(f"Останнє оновлення: {formatted_date}")
        else:
            self.weather_label.setText('Місто не знайдено. Спробуйте ще раз.')

    def update_weather(self):
        self.get_weather()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.setStyleSheet("""
     
    QWidget {
        background-color: #00FFF7;
    }

    QLabel {
        font-size: 16px;
    }

    QPushButton {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 10px 0;
        cursor: pointer;
        border-radius: 5px;
    }

    QPushButton:hover {
        background-color: #45a049;
    }

    QPushButton#update_button {
        background-color: #008CBA;
    }

    QPushButton#update_button:hover {
        background-color: #005f7f;
    }

    QComboBox {
        font-size: 16px;
    }

    
    


 """)

    window.show()
    sys.exit(app.exec_())
