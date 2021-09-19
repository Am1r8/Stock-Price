import requests
import json
from time import sleep
import sys


def print_s(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.1)


print("""\n\n

____ ___ ____ ____ _  _    ___  ____ _ ____ ____ 
[__   |  |  | |    |_/     |__] |__/ | |    |___ 
___]  |  |__| |___ | \_    |    |  \ | |___ |___ 
                                                 
\n\n\n\n""")

line = input("Give me a stock symbol?\n")

header = {'X-Finnhub-Token':'c53qr8aad3if62bgj550'}

r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={line}', headers = header)
rcontent = (r.content)
rjson = json.loads(rcontent)
value = rjson['c']
previousClose = rjson['pc']

try:
    percentChange = ((value - previousClose)/previousClose) * 100
except:
    print_s("\n\nStock Symbol is incorrect\n")
    sleep(20)
    exit()


print("\n\n" + line + ':\n')
print("Current Value", "$" + str(value) + "\n", sep = " - ")
print("Previous Close", "$" + str(previousClose) + "\n", sep = " - ")
print("Percent Change: ", "{:.3f}".format(percentChange)+ "%" + "\n")

sleep(60)