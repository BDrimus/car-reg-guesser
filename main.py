from bs4 import BeautifulSoup
import requests
import time

firstHalf = 'KY09'
secondHalf = ''
url = 'https://www.checkcardetails.co.uk/cardetails/' + firstHalf

def checker(url, secondHalf):
    page = requests.get(url + secondHalf)
    soup = BeautifulSoup(page.content, "html.parser")

    if soup.find('p', {'id':'reg-error'}):
        return None

    if (soup.find('h5', {'class':'car_make_model text-center'}).text.find('C30') != -1):
        return {'C30', url + secondHalf}

    return None

found = []

def generator():
    for i in range(65, 91):
        for j in range(65, 91):
            for k in range(65, 91):
                secondHalf = chr(i)+chr(j)+chr(k)
                current = checker(url, secondHalf)
                if current != None:
                    found.append(current)
                    print(found)

                time.sleep(0.1)
    return found


if __name__ == '__main__':

    found = generator()
    print(found)




