from data.users_data import ResidentRFCompanyData, ResidentRfFIOData, NotResidentRFinnData, UserPersonalData, UserAuthenticationData
from faker import Faker
import random

faker_ru = Faker('ru-RU')

def generate_inn(l):
    """Генерация 10 значного ИНН для ЮЛ и 12 значного ИНН для ФЛ """
    nums = [random.randint(1, 9) if x == 0 else random.randint(0, 9) for x in range(0, 9 if l == 10 else 10)]
    weights = [
        [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        [2, 4, 10, 3, 5, 9, 4, 6, 8]
    ]
    if l == 12:
        nums.append(sum([n * w for w, n in zip(weights[0], nums)]) % 11 % 10)
        nums.append(sum([n * w for w, n in zip(weights[1], nums)]) % 11 % 10)
    if l == 10:
        nums.append(sum([n * w for w, n in zip(weights[2], nums)]) % 11 % 10)

    return ''.join(map(str, nums))

def generate_password():
    """Генерация строки пароля в 12 символов с содержанием не менее одной цифры, не менее одной заглавной буквы,
     не менее одной строчной буквы, не менее одного специального символа"""

    numbers = '123456789'
    lowercase_letters = 'qwertyuiopasdfghjklzxcvbnm'
    uppercase_letters = lowercase_letters.upper()
    special_characters = r'!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    psw = [random.choice(list(numbers)),
           random.choice(list(lowercase_letters)),
           random.choice(list(uppercase_letters)),
           random.choice(list(special_characters))]

    for x in range(9):
        psw.append(random.choice(list(numbers + lowercase_letters + uppercase_letters + special_characters)))

    psw = list(psw)
    random.shuffle(psw)

    return ''.join(psw)

def generated_resident_rf_company_data():
    return ResidentRFCompanyData(
        full_name_company_fio=faker_ru.company(),
        resident_inn=generate_inn(10),
        resident_kpp=f'{random.randint(1,999999999):09}'
    )

def generated_resident_rf_fio_data():
    return ResidentRfFIOData(
        full_name_company_fio = faker_ru.name(),
        resident_inn = generate_inn(12)
    )

def generated_not_resident_rf_inn_data():
    return NotResidentRFinnData(
        full_name_company_fio = faker_ru.name(),
        not_resident_data = generate_inn(12)
    )

def generated_not_resident_rf_tin_data():
    return NotResidentRFinnData(
        full_name_company_fio = faker_ru.name(),
        not_resident_data = faker_ru.ssn()
    )

def generated_user_personal_data():
    """
    Если Faker сформирует существующий код страны более 5 знаков - тест упадет.
    Например: +44-1624 — код страны острова Мэн
    Поэтому добавлен срез [:4]

    """
    fio = faker_ru.name().split(' ')
    first_name = fio[1] if fio[1] else ''
    surname = fio[2] if fio[2] else ''
    last_name = fio[0] if fio[0] else ''
    position = ['Руководитель товарного направления',
                'Начальник отдела логистики',
                'Начальник отдела закупок',
                'Менеджер по логистике',
                'Менеджер по закупкам',
                '']

    return UserPersonalData(
        user_first_name=first_name,
        user_surname=surname,
        user_last_name=last_name,
        user_position=random.choice(position),
        user_phone_country_code=faker_ru.country_calling_code().replace('+','')[:4],
        user_phone_city_code=str(random.randint(1,999999)),
        user_phone_number=faker_ru.phone_number(),
        user_email=faker_ru.email()
    )

def generated_user_authentication_data():
    psw = generate_password()
    captcha=''
    for x in range(6):
        captcha = captcha + random.choice(
            list('123456789qwertyuiopasdfghjklzxcvbnm'))

    return UserAuthenticationData(
        login=faker_ru.email(),
        password=psw,
        password_confirm=psw,
        captcha=captcha
    )