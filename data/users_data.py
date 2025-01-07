from dataclasses import dataclass
"""Классы данных для отдельных разделов формы на странице аккредитации: 
4 вида ФЛ и ЮЛ, 
личная информация пользователя 
и данные аутентификации  """

@dataclass
class ResidentRFCompanyData:
    full_name_company_fio: str = None
    resident_inn: str = None
    resident_kpp: str = None

@dataclass
class ResidentRfFIOData:
    full_name_company_fio: str = ""
    resident_inn: str = ""

@dataclass
class NotResidentRFinnData:
    full_name_company_fio: str = None
    not_resident_data: str = None

@dataclass
class NotResidentRFtinData:
    full_name_company_fio: str = None
    not_resident_data: str = None

@dataclass
class UserPersonalData:
    user_first_name: str = None
    user_last_name: str = None
    user_surname: str = None
    user_position: str = None
    user_phone_country_code: str = None
    user_phone_city_code: str = None
    user_phone_number: str = None
    user_email: str = None

@dataclass
class UserAuthenticationData:
    login: str = None
    password: str = None
    password_confirm: str = None
    captcha: str = None
