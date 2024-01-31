import secrets
import string


def pass_gen(pass_length, is_numbers_in_pass, is_uppercase_pass, is_lowercase_pass, is_special_characters_in_pass):
    if is_numbers_in_pass == '' and is_uppercase_pass == '' and is_lowercase_pass == '' and is_special_characters_in_pass == '':
        return 'Не удалось сгенерировать пароль'
    else:
        return 'Вот сгенерированный пароль: ' + ''.join(secrets.choice(is_numbers_in_pass + is_uppercase_pass + is_lowercase_pass + is_special_characters_in_pass) for x in range(int(pass_length)))







while True:
    pass_length = input('Укажите длину пароля ')
    if not pass_length.isnumeric():
        print('Можно ввести только цифры')
    else:
        break

while True:
    is_numbers_in_pass = input('Должны ли быть цифры в пароле Y/N? ')
    if is_numbers_in_pass == 'y':
        is_numbers_in_pass = string.digits
        break
    elif is_numbers_in_pass == 'n':
        is_numbers_in_pass = ''
        break
    else:
        print('Ошибка! Введите y или n ')

while True:
    is_uppercase_pass = input('Пароль должен содержать строчные буквы Y/N? ')
    if is_uppercase_pass == 'y':
        is_uppercase_pass = string.ascii_uppercase
        break
    elif is_uppercase_pass == 'n':
        is_uppercase_pass = ''
        break
    else:
        print('Ошибка! Введите y или n ')

while True:
    is_lowercase_pass = input('Пароль должен содержать прописные буквы Y/N? ')
    if is_lowercase_pass == 'y':
        is_lowercase_pass = string.ascii_lowercase
        break
    elif is_lowercase_pass == 'n':
        is_lowercase_pass = ''
        break
    else:
        print('Ошибка! Введите y или n ')

while True:
    is_special_characters_in_pass = input('В пароле должны присутстовать специальные символы Y/N? ')
    if is_special_characters_in_pass == 'y':
        is_special_characters_in_pass = string.punctuation
        break
    elif is_special_characters_in_pass == 'n':
        is_special_characters_in_pass = ''
        break
    else:
        print('Ошибка! Введите y или n ')

print(pass_gen(pass_length, is_numbers_in_pass, is_uppercase_pass,is_lowercase_pass, is_special_characters_in_pass))
