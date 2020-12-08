# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень).
# Напишите решения через list и через dict


# seasons = {'Зима': [12, 1, 2],
#            'Весна': [3, 4, 5],
#            'Лето': [6, 7, 8],
#            'Осень': [9, 10, 11],
#            }
# user_input = int(input('Введите номер месяца: '))
# for key in seasons.keys():
#     if user_input in seasons[key]:
#         print(key)


seasons_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8],  [9, 10, 11]]
seasons_month = ['зима', 'весна', 'лето', 'осень']
seasons_input = int(input('Введите номер месяца: '))
seasons_dict = dict(zip(seasons_month, seasons_list))
# print(seasons_dict)
for key in seasons_dict.keys():
    if seasons_input in seasons_dict[key]:
        print(key)
