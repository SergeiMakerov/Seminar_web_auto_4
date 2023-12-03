import pytest
from module import Site
import yaml
from  selenium import webdriver

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def log_xpath():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def pass_xpath():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def btn_xpath():
    return """//*[@id="login"]/div[3]/button/div"""


@pytest.fixture()
def btn_xpath_2():
    return """//*[@id="login"]/div[3]/button"""
             # //*[@id="login"]/div[3]/button

@pytest.fixture()
def btn_xpath_3():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def btn_xpath_4():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""

@pytest.fixture()
def title_xpath():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def new_post_xpath():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def result_xpath():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def result_login():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def site():
    my_site = Site(testdata["address"])
    yield my_site
    my_site.close()

# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.get("https://test-stand.gb.ru/")
#     myDynamicElement = driver.find_element_by_id("myDynamicElement")
#     return myDynamicElement