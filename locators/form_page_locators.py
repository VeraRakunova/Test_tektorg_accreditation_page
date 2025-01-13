from selenium.webdriver.common.by import By


class FormPageLocators:
    """Локаторы для страницы аккредитации"""
    LINK_AKK_PAGE = (By.XPATH, "//div[contains(@class,'x-treelist-row')]//div[contains(text(),'Аккредитация')]")
    FULL_NAME_COMPANY_FIO = (By.XPATH, "//div[contains(@class,'full-organization-name')]//input")
    RESIDENT_RF = (By.XPATH, "//a[contains(@class,'x-btn resident-RF')]")
    RESIDENT_INN = (By.XPATH, "//div[contains(@id,'container')]//input[contains(@id,'form-field-inn-search')]")
    RESIDENT_KPP = (By.XPATH, "//input[contains(@id,'form-field-kpp')]")
    RESIDENT_OKOP = (By.XPATH, "//div[contains(@class,'okopf-field')]//input")#???
    NOT_RESIDENT_RF = (By.XPATH, "//a[contains(@class,'non-resident-RF')]")
    NOT_RESIDENT_RAD_INN = (By.XPATH, "//div[contains(@class,'inn-radio')]//span[contains(@class,'radio')]")
    NOT_RESIDENT_RAD_TIN = (By.XPATH, "//div[contains(@class,'tin-radio')]//span[contains(@class,'radio')]")
    NOT_RESIDENT_DATA = (By.XPATH, "//input[contains(@class,'x-form-field x-form-text x-form-text-default  x-form-empty-field x-form-empty-field-default x-form-invalid-field x-form-invalid-field-default')]")
    USER_LAST_NAME = (By.XPATH, "//div[contains(@class,'last-name')]//input")
    USER_FIRST_NAME = (By.XPATH, "//div[contains(@class,'first-name')]//input")
    USER_SURNAME = (By.XPATH, "//div[contains(@class,'middle-name')]//input")
    USER_POSITION = (By.XPATH, "//div[contains(@class,'user-job')]//input")
    USER_PHONE_COUNTRY_CODE = (By.XPATH, "//div[contains(@class,'phone-country-code')]//input")
    USER_PHONE_CITY_CODE = (By.XPATH, "//div[contains(@class,'phone-city-code')]//input")
    USER_PHONE_NUMBER = (By.XPATH, "//div[contains(@class,'phone-number')]//input")
    USER_PHONE_ADD_NUMBER = (By.XPATH, "//div[contains(@class,'add-number-field')]//input")
    USER_EMAIL = (By.XPATH, "//input[contains(@id,'email')]")
    USER_TIME_ZONE = (By.XPATH, "//input[contains(@id,'time-zone')]")#??
    LOGIN = (By.XPATH, "//input[contains(@id,'username')]")
    PASSWORD = (By.XPATH, "//div[contains(@class,'password x')]//input")
    PASSWORD_CONFIRM = (By.XPATH, "//input[contains(@id,'password-confirm')]")
    CONSENT_PERS_DATA = (By.XPATH, "//div[contains(@id,'checkbox')]//span[contains(@class,'x-form-checkbox')]")
    PIC_CODE = (By.XPATH, "//div[contains(@class,'captcha-code')]//input")
    UPDATE_PIC = (By.XPATH, "/a[contains(@class,'captcha-rebuild')]")
    STOP_ACCREDITATION = (By.XPATH, "//a[contains(@class,'common-button')]//span[contains(text(),'Прекратить')]")
    SIGN_ACCREDITATION = (By.XPATH, "//a[contains(@class,'sign-submit-btn') and @aria-disabled='false']")
