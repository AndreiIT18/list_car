list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
list_months_of_winter = ['January', 'February', 'December']
list_months_of_spring = ['March', 'April', 'May']
list_months_of_summer = ['June', 'July', 'August']
list_months_of_autumn = ['September', 'October', 'November']
for months in list_of_months:
    if months in list_months_of_winter:
        print(months + ' месяц зимы')
    else:
        if months in list_months_of_spring:
            print(months + ' месяц весны')
        else:
            if months in list_months_of_summer:
                print(months + ' месяц лета')
            else:
                if months in list_months_of_autumn:
                    print(months + ' месяц осени')
                else:
                    print('Спасибо')
