from random import randint
 
print('Я загадал букву от А до Д угадай её!')
random_letter = chr(randint(ord('А'), ord('Д')))
letter = input('Введите букву: ')

while random_letter != letter:
    letter = input('Попробуй заново: ')
    if random_letter < letter:
        print('Не та!')
    elif random_letter > letter:
          print('Близко')
    else:
          print('Поздравляю вы угадали букву:', random_letter,'!')
