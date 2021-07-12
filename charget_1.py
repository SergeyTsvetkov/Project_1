import urllib.request # модуль для открыеия url адресов
import chardet        # детектор кодировки символов

data = urllib.request.urlopen('http://google.com/') #запрос к сайту
print(chardet.detect(data.read())['encoding']) # читаем и определяем key[encoding]