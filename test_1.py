from testpage import OperationsHelper
import logging
import yaml
import time


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)



def test_step1(browser):
    logging.info("Test_1 step_1 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    testpage.click_new_post_button()
    time.sleep(3)
    # testpage.enter_title_post(testdata["title"])
    # testpage.enter_content_post(testdata["content"])
    # testpage.enter_description_post(testdata["description"])
    # testpage.click_create_new_post_button()

    assert testpage.get_token() == "65dfe3f15af5a29b962b686e4ba9edb7"


def test_step2(browser, send_to_email):
    # залогинится
    logging.info("Test_1 step_2 starting")
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata["login"])
    # testpage.enter_pass(testdata["password"])
    # testpage.click_login_button()
    #создания поста
    testpage.click_new_post_button()
    testpage.enter_title_post(testdata["title"])
    testpage.enter_content_post(testdata["content"])
    testpage.enter_description_post(testdata["description"])
    testpage.click_create_new_post_button()
    time.sleep(3)
    assert testpage.get_new_post_descr() == "You can add something text here"


