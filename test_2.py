# import time
# import yaml
# from module import Site
# from  selenium import webdriver
from testpage import OperationsHelper
import logging
import yaml
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


# Проверка на вход с не валидными данными
def test_step1(browser):
    logging.info("Test_2 step_1 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


# Проверка на вход с валидными данными
def test_step2(browser):
    logging.info("Test_2 step_2 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()

    assert testpage.get_text_blog() == "Blog"


# Провека на создание нового поста по тайтлу
def test_step3(browser):
    # залогинится
    logging.info("Test_2 step_3 starting")
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata["login"])
    # testpage.enter_pass(testdata["password"])
    # testpage.click_login_button()
    # создания поста
    testpage.click_new_post_button()
    testpage.enter_title_post(testdata["title"])
    testpage.enter_content_post(testdata["content"])
    testpage.click_create_new_post_button()
    time.sleep(3)
    # Проверка наличия названия поста на странице
    assert testpage.get_text_post() == "Congratulations"

# Добавить в проект тест по проверке механики работы формы Contact Us на главной странице личного кабинета.
# Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.
def test_step4(browser, send_to_email):
    # залогинится
    logging.info("Test_2 step_4 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    time.sleep(3)
    testpage.click_contact_button()
    time.sleep(3)
    testpage.enter_name_contact("Sergei")
    testpage.enter_email_contact("mail@mail.ru")
    testpage.enter_content_contact("text")
    testpage.click_contact_us_button()
    time.sleep(3)

    assert testpage.get_alert_text() == "Form successfully submitted"




# def test_step1():
#     x_selector1 = """//*[@id="login"]/div[1]/label/input"""
#     input1 = site.find_element("xpath", x_selector1)
#     input1.send_keys("test")
#     x_selector2 = """//*[@id="login"]/div[2]/label/input"""
#     input2 = site.find_element("xpath", x_selector2)
#     input2.send_keys("test")
#     btn_selector = "button"
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#     x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
#     err_lable = site.find_element("xpath", x_selector3)
#     assert err_lable.text == "401"
#
#
# # Проверка на вход с не валидными данными
# def test_step2(site, log_xpath, pass_xpath, btn_xpath_2, result_xpath):
#     input1 = site.find_element("xpath", log_xpath)
#     input1.send_keys("test")
#     input2 = site.find_element("xpath", pass_xpath)
#     input2.send_keys("test")
#     btn = site.find_element("xpath", btn_xpath_2)
#     btn.click()
#     err_lable = site.find_element("xpath", result_xpath)
#     assert err_lable.text == "401"
#
#
# # Проверка на вход с валидными данными
# def test_step_3(site, log_xpath, pass_xpath, btn_xpath_2, result_login):
#     input1 = site.find_element("xpath", log_xpath)
#     input1.send_keys(testdata["login"])
#     input2 = site.find_element("xpath", pass_xpath)
#     input2.send_keys(testdata["password"])
#     btn = site.find_element("xpath", btn_xpath_2)
#     btn.click()
#     login = site.find_element("xpath", result_login)
#     assert login.text == "Blog"
#
#
# # Провека на создание нового поста
# def test_step_4(site, log_xpath, pass_xpath, btn_xpath_2, title_xpath, btn_xpath_3, btn_xpath_4, new_post_xpath,
#                 result_login):
#     input1 = site.find_element("xpath", log_xpath)
#     input1.send_keys(testdata["login"])
#     input2 = site.find_element("xpath", pass_xpath)
#     input2.send_keys(testdata["password"])
#     btn = site.find_element("xpath", btn_xpath_2)
#     btn.click()
#     btn_2 = site.find_element("xpath", btn_xpath_3)
#     btn_2.click()
#     time.sleep(5)
#     input3 = site.find_element("xpath", title_xpath)
#     input3.send_keys(testdata["title"])
#     btn_4 = site.find_element("xpath", btn_xpath_4)
#     btn_4.click()
#     time.sleep(5)
#     new_post = site.find_element("xpath", new_post_xpath)
#     assert new_post.text == "Congratulations"
