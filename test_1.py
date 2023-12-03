import time

import yaml
from module import Site
from  selenium import webdriver

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_step1():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    err_lable = site.find_element("xpath", x_selector3)
    assert err_lable.text == "401"

#Проверка на вход с не валидными данными
def test_step2(site, log_xpath, pass_xpath, btn_xpath_2, result_xpath):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys("test")
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys("test")
    btn = site.find_element("xpath", btn_xpath_2)
    btn.click()
    err_lable = site.find_element("xpath", result_xpath)
    assert err_lable.text == "401"

#Проверка на вход с валидными данными
def test_step_3(site, log_xpath, pass_xpath, btn_xpath_2, result_login):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath_2)
    btn.click()
    login = site.find_element("xpath", result_login)
    assert login.text == "Blog"

#Провека на создание нового поста
def test_step_4(site, log_xpath, pass_xpath, btn_xpath_2, title_xpath, btn_xpath_3, btn_xpath_4, new_post_xpath,  result_login):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath_2)
    btn.click()
    btn_2 = site.find_element("xpath", btn_xpath_3)
    btn_2.click()
    time.sleep(5)
    input3 = site.find_element("xpath", title_xpath)
    input3.send_keys(testdata["title"])
    btn_4 = site.find_element("xpath", btn_xpath_4)
    btn_4.click()
    time.sleep(5)
    new_post = site.find_element("xpath", new_post_xpath)
    assert new_post.text == "Congratulations"