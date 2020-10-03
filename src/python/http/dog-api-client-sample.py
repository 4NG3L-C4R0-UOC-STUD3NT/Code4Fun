import enum
import requests
import json
from PIL import Image
from io import BytesIO

class MenuOptionsIds(enum.Enum): 
    SHOW_BREEDS = 1
    SHOW_RANDOM_IMAGE = 2
    QUIT = 99

DOG_API_URL = "https://dog.ceo/api"

mainMenuOptions = { MenuOptionsIds.SHOW_BREEDS: ' 1. Show dog breeds', 
                    MenuOptionsIds.SHOW_RANDOM_IMAGE: ' 2. Show breed images',
                    MenuOptionsIds.QUIT: '99. Quit' }

availableOptions = [option.value for option in mainMenuOptions]


def pause():
    wait = input("PRESS ENTER TO CONTINUE...")

def showImage(url):
    response = requests.get(url)
    print(response.status_code)
    img = Image.open(BytesIO(response.content))
    img.show()

def getDogBreeds():
    url = DOG_API_URL + '/breeds/list/all'
    response = requests.get(url)
    result = []
    if response.status_code == 200:
        data = json.loads(response.content)
        result = [key for key in data['message'].keys()]

    return result

def getDogBreedImageUrl(breed = 'labrador'):
    url = DOG_API_URL + '/breed/_BREED_/images/random'
    url = url.replace('_BREED_', breed)
    
    result = None
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        result = str(data['message'])
    
    return result

def showDogBreeds(dogBreeds = None):
    if dogBreeds == None:
        dogBreeds = getDogBreeds()
    print('')
    print('Dog breeds:')
    
    breeds = dogBreeds.copy()
    while len(breeds) % 4 != 0: breeds.append('')
        
    split = int(len(breeds)/4)
    l1 = breeds[0:split]
    l2 = breeds[split:split*2]
    l3 = breeds[split*2:split*3]
    l4 = breeds[split*3:]
    for a, b, c, d in zip(l1,l2,l3,l4):
        print("%-20s %-20s %-20s %-20s" % (a, b, c, d))
    print('')

def selectDogBreed(dogBreeds = None):
    if dogBreeds == None:
        dogBreeds = getDogBreeds()
        
    breed = str(input("Select a dog breed (BACK to return to main menu): "))
        
    return breed

def showDogBreedImage():
    dogBreeds = getDogBreeds()
    
    while True:
        showDogBreeds(dogBreeds)
        breed = selectDogBreed(dogBreeds).lower()

        if breed == 'back':
            break
        elif breed in dogBreeds:
            imgUrl = getDogBreedImageUrl(breed)
            if Image != None:
                showImage(imgUrl)
            else:
                print(f'there are not images for dog breed = {breed}')
        else: 
            print(f'does not exists dog breed = {breed}')
            pause()
    
# max(mylist, key=len)
def selectMenuOption(availableOptions):
    option = 0
    
    isAValidOption = False
    while not isAValidOption:
        try:
            option = int(input("Select an option: "))
            if option in availableOptions:
                isAValidOption = True
            else:
                print(f"does not exist the option = {option}")
        except ValueError:
            print("Invalid option!!!")
    
    return option

def showMainMenuOptions():
    print('')
    for code, option in mainMenuOptions.items():
        print(option)
    print('=================================')

print('Working with the DOG api [https://dog.ceo/dog-api/documentation/]')
while True:
    showMainMenuOptions()
    option = selectMenuOption(availableOptions)
    
    if MenuOptionsIds.SHOW_BREEDS.value == option:
        showDogBreeds()
    elif MenuOptionsIds.SHOW_RANDOM_IMAGE.value == option:
        showDogBreedImage()
    elif MenuOptionsIds.QUIT.value == option:
        break


print('finished...')




