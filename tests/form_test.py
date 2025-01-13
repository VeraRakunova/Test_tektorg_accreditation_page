from pages.form_page import FormPage
from conftest import driver
from logs import app_logger

logger = app_logger.get_logger(__name__)

class TestFormPage:

    def test_form_fio_rf(self,driver):
        logger.info("Начат тест 1: заполнение данных для ФЛ резидента РФ ")
        form_page = FormPage(driver,'https://rn.tektorg.ru/#front/register')
        form_page.open()
        assert form_page.link_accreditation_page_visible() == True, "страница не загрузилась"
        form_page.fill_fields_for_resident_rf_fio()
        form_page.fill_fields_for_user_data()
        form_page.fill_fields_for_authorization()

        assert form_page.sign_button_visible()==True, "тест заполнения полей для ФЛ резидента РФ"


    def test_form_company_rf(self,driver):
        logger.info("Начат тест 2: заполнение данных для ЮЛ резидента РФ ")
        form_page = FormPage(driver,'https://rn.tektorg.ru/#front/register')
        form_page.open()
        assert form_page.link_accreditation_page_visible() == True, "страница не загрузилась"
        form_page.fill_fields_for_resident_rf_company()
        form_page.fill_fields_for_user_data()
        form_page.fill_fields_for_authorization()

        assert form_page.sign_button_visible() == True, "тест заполнения полей для ЮЛ резидента РФ "

    def test_form_not_rf_inn(self,driver):
        logger.info("Начат тест 3: заполнение данных для ФЛ нерезидента РФ ИНН")
        form_page = FormPage(driver,'https://rn.tektorg.ru/#front/register')
        form_page.open()
        assert form_page.link_accreditation_page_visible() == True, "страница не загрузилась"
        form_page.fill_fields_for_not_resident_rf_inn()
        form_page.fill_fields_for_user_data()
        form_page.fill_fields_for_authorization()

        assert form_page.sign_button_visible() == True, "тест заполнения полей для ФЛ нерезидента РФ ИНН"

    def test_form_not_rf_tin(self,driver):
        logger.info("Начат тест 4: заполнение данных для ФЛ нерезидента РФ TIN")
        form_page = FormPage(driver,'https://rn.tektorg.ru/#front/register')
        form_page.open()
        assert form_page.link_accreditation_page_visible() == True, "страница не загрузилась"
        form_page.fill_fields_for_not_resident_rf_tin()
        form_page.fill_fields_for_user_data()
        form_page.fill_fields_for_authorization()

        assert form_page.sign_button_visible() == True, "тест заполнения полей для ФЛ нерезидента РФ TIN"
