import logging
import time

import yaml

from testpage import OperationsHelper

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    time.sleep(3)
    testpage.click_contact_button()
    time.sleep(3)

    assert testpage.get_text_contact_us() == "Contact us!"


def test_step2(browser):
    logging.info("Test_3 step_1 starting")
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata["login"])
    # testpage.enter_pass(testdata["password"])
    # testpage.click_login_button()
    # time.sleep(3)
    # testpage.click_contact_button()
    # time.sleep(3)
    testpage.enter_name_contact("Sergei")
    testpage.enter_email_contact("mail@mail.ru")
    testpage.enter_content_contact("text")
    time.sleep(3)

    assert testpage.get_name_cont_text() == ""
    assert testpage.get_email_cont_text() == ""
    assert testpage.get_content_cont_text() == ""


def test_step3(browser, send_to_email):
    logging.info("Test_3 step_2 starting")
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata["login"])
    # testpage.enter_pass(testdata["password"])
    # testpage.click_login_button()
    # time.sleep(3)
    # testpage.click_contact_button()
    # time.sleep(3)
    # testpage.enter_name_contact("Sergei")
    # testpage.enter_email_contact("mail@mail.ru")
    # testpage.enter_content_contact("text")
    testpage.click_contact_us_button()
    time.sleep(3)

    assert testpage.get_alert_text() == "Form successfully submitted"