import requests
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    # for locator in locators["css"].keys():
    #     ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


# класс с методами (действиями с локаторами из файла test_1)
class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_token(self):
        try:
            result = requests.post(url=testdata["url"],
                                   data={"username": testdata["login"], "password": testdata["password"]})
            return result.json()["token"]
        except:
            logging.exception("Exception get token")
            return None

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return False
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    # функция ввода логина

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="path form")

    # функция ввода пароля

    def enter_title_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_TITLE"], word, description="title post form")

    def enter_content_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_CONTENT"], word,
                                   description="content post form")

    def enter_description_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_DESCRIPTION"], word,
                                   description="content contact description form")

    def enter_name_contact(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NAME_CONTACT"], word,
                                   description="name contact form")

    def enter_email_contact(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_EMAIL_CONTACT"], word,
                                   description="email contact form")

    def enter_content_contact(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_CONTACT"], word,
                                   description="content contact form")

    # CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login button")

    def click_new_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_NEW_POST"], description="new post button")

    def click_create_new_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], description="create new post button")

    def click_contact_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="contact button")

    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description="contact us button")

    # GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error text")

    def get_text_blog(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_RESULT_LOGIN"], description="text blog")

    def get_text_post(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_NEW_POST"], description="text post")

    def get_text_email(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_EMAIL_CONTACT"], description="text email")

    def get_new_post_descr(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_NEW_POST_DESCRIPTION"], description="text description")

    def get_name_cont_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_NAME_CONTACT"],
                                          description="text name cont text")

    def get_text_contact_us(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CONTACT_US_FIELD"],
                                          description="text contact us")

    def get_email_cont_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_EMAIL_CONTACT"],
                                          description="email cont text")

    def get_content_cont_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CONTENT_CONTACT"],
                                          description="content cont text")

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f"We find text {text} in error alert")
        return text




