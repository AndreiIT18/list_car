# list_of_cars = ['Ауди', 'БМВ', 'Додж', 'Киа', 'Ламборгини']
# if 'Ламборгини' in list_of_cars:
#     print('В списке есть Ламборгини')
# else:
#     print('В списке нет Ламборгини')

list_of_cars = ['Ауди', 'Додж', 'Киа', 'Ламборгини', 'Линкольн', 'Роллс-Ройс', 'Тесла', 'БМВ']
list_of_expensive_cars = ['Линкольн', 'Роллс-Ройс', 'Тесла', 'БМВ', 'Ламборгини' ]
for car in list_of_cars:
    if car in list_of_expensive_cars:
        print(car + ' дорогая машина')    
    else:
        print('Не дорогая машина ' + car)