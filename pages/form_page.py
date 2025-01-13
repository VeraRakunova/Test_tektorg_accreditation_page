from selenium.common import TimeoutException
from generator.generator import generated_resident_rf_fio_data, generated_resident_rf_company_data, \
    generated_not_resident_rf_inn_data, generated_not_resident_rf_tin_data, generated_user_personal_data, \
    generated_user_authentication_data
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
from logs import app_logger

logger = app_logger.get_logger(__name__)

class FormPage(BasePage):

    """Класс содержит последовательности методов генерации данных и заполнения ими форм, отдельно по блокам форм"""

    def fill_fields_for_resident_rf_fio(self):
        fio = generated_resident_rf_fio_data()
        logger.info(fio)
        self.element_is_visible(Locators.FULL_NAME_COMPANY_FIO).send_keys(fio.full_name_company_fio)
        self.element_is_visible(Locators.RESIDENT_RF).click()
        self.element_is_visible(Locators.RESIDENT_INN).send_keys(fio.resident_inn)

    def fill_fields_for_resident_rf_company(self):
        company = generated_resident_rf_company_data()
        logger.info(company)
        self.element_is_visible(Locators.FULL_NAME_COMPANY_FIO).send_keys(company.full_name_company_fio)
        self.element_is_visible(Locators.RESIDENT_RF).click()
        self.element_is_visible(Locators.RESIDENT_INN).send_keys(company.resident_inn)
        self.element_is_visible(Locators.RESIDENT_KPP).send_keys(company.resident_kpp)

    def fill_fields_for_not_resident_rf_inn(self):
        fio = generated_not_resident_rf_inn_data()
        logger.info(fio)
        self.element_is_visible(Locators.FULL_NAME_COMPANY_FIO).send_keys(fio.full_name_company_fio)
        self.element_is_visible(Locators.NOT_RESIDENT_RF).click()
        self.element_is_visible(Locators.NOT_RESIDENT_RAD_INN).click()
        self.element_is_visible(Locators.NOT_RESIDENT_DATA).send_keys(fio.not_resident_data)

    def fill_fields_for_not_resident_rf_tin(self):
        fio = generated_not_resident_rf_tin_data()
        logger.info(fio)
        self.element_is_visible(Locators.FULL_NAME_COMPANY_FIO).send_keys(fio.full_name_company_fio)
        self.element_is_visible(Locators.NOT_RESIDENT_RF).click()
        self.element_is_visible(Locators.NOT_RESIDENT_RAD_TIN).click()
        self.element_is_visible(Locators.NOT_RESIDENT_DATA).send_keys(fio.not_resident_data)

    def fill_fields_for_user_data(self):
        user = generated_user_personal_data()
        logger.info(user)
        self.element_is_visible(Locators.USER_FIRST_NAME).send_keys(user.user_first_name)
        self.element_is_visible(Locators.USER_LAST_NAME).send_keys(user.user_last_name)
        self.element_is_visible(Locators.USER_SURNAME).send_keys(user.user_surname)
        self.element_is_visible(Locators.USER_POSITION).send_keys(user.user_position)
        self.element_is_visible(Locators.USER_PHONE_COUNTRY_CODE).send_keys(user.user_phone_country_code)
        self.element_is_visible(Locators.USER_PHONE_CITY_CODE).send_keys(user.user_phone_city_code)
        self.element_is_visible(Locators.USER_PHONE_NUMBER).send_keys(user.user_phone_number)
        self.element_is_visible(Locators.USER_EMAIL).send_keys(user.user_email)

    def fill_fields_for_authorization(self):

        user_auto = generated_user_authentication_data()
        logger.info(user_auto)
        self.element_is_visible(Locators.LOGIN).send_keys(user_auto.login)
        self.element_is_visible(Locators.PASSWORD).send_keys(user_auto.password)
        self.element_is_visible(Locators.PASSWORD_CONFIRM).send_keys(user_auto.password_confirm)
        self.element_is_visible(Locators.CONSENT_PERS_DATA).click()
        self.element_is_visible(Locators.PIC_CODE).send_keys(user_auto.captcha)

    def sign_button_visible(self):
        """
        Проверка активности кнопки 'Подписать и отправить заявку'
        """
        try:
            self.element_is_visible(Locators.SIGN_ACCREDITATION)
        except TimeoutException:
            logger.info('TimeoutException, нет кнопки Подписать и отправить заявку')
            return False

        return True

    def link_accreditation_page_visible(self):
        """
        Проверка загрузки страницы
        """
        try:
            self.element_is_visible(Locators.LINK_AKK_PAGE)
        except TimeoutException:
            logger.info('TimeoutException, не загрузилась страница/нет ссылки на страницу Аккредитации')
            return False

        return True


