from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

##################################################################

car = 'CR-Z'
firstHalf = 'SJ61'

##################################################################

secondHalf = ''
url = 'https://www.checkcardetails.co.uk/cardetails/' + firstHalf


def checker(url, secondHalf):
    page = requests.get(url + secondHalf)
    soup = BeautifulSoup(page.content, "html.parser")

    if soup.find('p', {'id': 'reg-error'}):
        return None

    if (soup.find('h5', {'class': 'car_make_model text-center'}).text.find(car) != -1):
        return {car, url + secondHalf}

    return None


found = []


def generator():
    for i in range(65, 91):
        print(chr(i))
        for j in range(65, 91):
            for k in range(65, 91):
                secondHalf = chr(i) + chr(j) + chr(k)
                current = checker(url, secondHalf)
                if current is not None:
                    found.append(current)
                    print(current, end=" ")
                    print(datetime.now().strftime("%H:%M:%S"))
    return found


if __name__ == '__main__':
    print('Start time: ' + datetime.now().strftime("%H:%M:%S"))

    found = generator()
