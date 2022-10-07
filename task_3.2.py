#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

array = ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen', 'anton', 'aoooooooooontooooo', 'elelelelelelelelelel', 'ntoneeee', 'tonee', '253235235a5323352n25235352t253523523235oo235523523523n', 'antoooooooooooooooooooooooooooooooooooooooooooooooooooon', 'unton']
number = 253
for word in array:
    if str(number) in word:
        print(True)
    else:
        print(False)