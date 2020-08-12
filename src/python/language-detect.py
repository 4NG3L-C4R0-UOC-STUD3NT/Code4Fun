# https://stackoverflow.com/questions/39142778/python-how-to-determine-the-language

from langdetect import detect, DetectorFactory

print("*************************************************")
print("langdetect")
print("*************************************************")
DetectorFactory.seed = 0
print(detect('hello world'))
print(detect('hola mundo'))
print(detect('bonjour'))
print(detect('الشمس تشرق'))
print(detect('今一はお前さん'))
print(detect("Ein, zwei, drei, vier"))
print(detect("Я люблю вкусные пампушки"))
print("*************************************************")

print("\n...\n")

import json
import chardet

print("*************************************************")
print("chardet")
print("*************************************************")
print(chardet.detect("Я люблю вкусные пампушки".encode('cp1251')))
#print(chardet.detect("Ein, zwei, drei, vier").encode('cp1251'))
print("*************************************************")

