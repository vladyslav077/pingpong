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

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.central_widget.setStyleSheet("background-color: #F0E10F;")

        self.label_city = QLabel('Місто:', self)
        self.layout.addWidget(self.label_city)

        self.city_combo = QComboBox(self)
        self.city_combo.addItems(["Київ", "Львів", "Одеса", "Харків", "Варшава", "Миколаїв", "Ужгород",
                                  "Новояворівськ", "Прилбичі", "Лондон", "Нью-Йорк", "Донецьк", "Маріуполь", "Дубай"])
        self.layout.addWidget(self.city_combo)
        self.city_combo.currentIndexChanged.connect(self.get_weather)
        self.city_combo.setStyleSheet("""
            QComboBox {
                background-color: #fff;
                border: 1px solid #ccc;
                padding: 5px;
                border-radius: 3px;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)

        self.button = QPushButton('Отримати погоду', self)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.get_weather)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: #fff;
                padding: 7px 10px;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

        self.update_button = QPushButton('Оновити', self)
        self.layout.addWidget(self.update_button)
        self.update_button.clicked.connect(self.update_weather)
        self.update_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: #fff;
                padding: 7px 10px;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)

        self.weather_label = QLabel('', self)
        self.layout.addWidget(self.weather_label)
        self.weather_label.setStyleSheet("font-size: 16px;")

        self.icon_label = QLabel(self)
        self.layout.addWidget(self.icon_label)

        self.last_update_label = QLabel('', self)
        self.layout.addWidget(self.last_update_label)

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
            self.weather_label.setText('Місто не знайдено.Спробуйте ще раз.')

    def update_weather(self):
        self.get_weather()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())

