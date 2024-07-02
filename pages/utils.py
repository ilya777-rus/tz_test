locations = [
    {
        "name": "СБИС - Уфа",
        "address": "ул. Октябрьской Революции, д. 78",
        "phone1": "+7 347 224-91-00",
        "phone2": "+7 347 262-58-40",
        "website": "sbis.ru",
        "email": "info@ufa.tensor.ru"
    },
    {
        "name": "СБИС | ЦЕНТР ВНЕДРЕНИЯ",
        "address": "ул. Менделеева, д. 219, 1ЭТАЖ",
        "phone1": "+7 906 100-60-10",
        "phone2": "+7 347 246-62-46",
        "website": "sbis.pro",
        "email": "help@sbis.pro"
    },
    {
        "name": "СБИС | ЦЕНТР ВНЕДРЕНИЯ",
        "address": "ул. Революционная, д. 173, 1ЭТАЖ",
        "phone1": "+7 906 100-60-10",
        "phone2": "+7 347 258-85-88",
        "website": "sbis.pro",
        "email": "help@sbis.pro"
    },
    {
        "name": "Ай-Ти Консультант",
        "address": "ул. Новоженова",
        "phone1": "+7 917 453-52-21",
        "phone2": "+7 347 246-09-36",
        "email": "info@ciufa.ru"
    },
    {
        "name": "Криптолинк",
        "address": "ул. Батырская 4/2 офис 404",
        "phone1": "+7 347 246-18-35",
        "website": "криптолинк.рф",
        "email": "criptolink2017@ya.ru"
    },
    {
        "name": "АБТ Сервисы для бизнеса",
        "address": "ул. Кирова, д. 52, оф. 702 (7 этаж)",
        "phone1": "+7 347 286-54-52",
        "website": "abt.ru",
        "email": "ufa@abt.ru"
    },
    {
        "name": "ИП Русаков В.В.",
        "address": "ул. Султанова, 2",
        "phone1": "+7 927 317-49-55",
        "phone2": "+7 917 770-20-25",
        "email": "rvlado@mail.ru"
    },
    {
        "name": "РПЦИ Акцент плюс",
        "address": "бул. Молодежный, 10",
        "phone1": "+7 347 237-73-40",
        "website": "cons.akcentplus.ru/sbis.php",
        "email": "tenzorakcent@yandex.ru"
    },
    {
        "name": "Группа компаний Софт-Сервис",
        "address": "ул. Менделеева, 134/7",
        "phone1": "+7 347 222-20-21",
        "email": "mela@soft-servis.ru"
    },
    {
        "name": "Корпорация РД",
        "address": "ул. Маршала Жукова, 29 3 этаж, блок Б",
        "phone1": "+7 917 777-81-88",
        "email": "elena@corprd.ru"
    },
    {
        "name": "Акцент плюс",
        "address": "бул. Молодежный, 10",
        "phone1": "+7 347 237-73-40",
        "email": "tenzorakcent@yandex.ru"
    },
    {
        "name": "ИП Мухамедьянова Гузель Зигануровна - УФА",
        "address": "пр-кт Октября, д. 1, к. 2 каб. 402",
        "phone1": "+7 927 954-90-90",
        "email": "info@tamira.cc"
    }
]
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


locations1 = [
    {"name": "СБИС - Уфа", "address": "ул. Октябрьской Революции, д. 78"},
    {"name": "СБИС | ЦЕНТР ВНЕДРЕНИЯ", "address": "ул. Менделеева, д. 219, 1ЭТАЖ"},
    {"name": "СБИС | ЦЕНТР ВНЕДРЕНИЯ", "address": "ул. Революционная, д. 173, 1ЭТАЖ"},
    {"name": "Ай-Ти Консультант", "address": "ул. Новоженова"},
    {"name": "Криптолинк", "address": "ул. Батырская 4/2 офис 404"},
    {"name": "АБТ Сервисы для бизнеса", "address": "ул. Кирова, д. 52, оф. 702 (7 этаж)"},
    {"name": "ИП Русаков В.В.", "address": "ул. Султанова, 2"},
    {"name": "РПЦИ Акцент плюс", "address": "бул. Молодежный, 10"},
    {"name": "Группа компаний Софт-Сервис", "address": "ул. Менделеева, 134/7"},
    {"name": "Корпорация РД", "address": "ул. Маршала Жукова, 29 3 этаж, блок Б"},
    {"name": "Акцент плюс", "address": "бул. Молодежный, 10"},
    {"name": "ИП Мухамедьянова Гузель Зигануровна - УФА", "address": "пр-кт Октября, д. 1, к. 2 каб. 402"}
]

locations2 = [
    {"name": "СБИС - Камчатка", "address": "ул.Ленинская, 59, оф.202, 205"},
]



class FileDownloadComplete:
    def __init__(self, download_dir, known_files):
        self.download_dir = download_dir
        self.known_files = known_files
        self.new_file = None

    def __call__(self, driver):
        # print('CAALLLLLLLLLLLLLLLLLLLLLL')
        current_files = set(os.listdir(self.download_dir))
        # print(current_files)
        new_files = current_files - self.known_files
        # print(new_files)
        if new_files:
            self.new_file = new_files.pop()
            return self.new_file
        return False

