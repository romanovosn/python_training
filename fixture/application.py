from selenium import webdriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\\Users\\roman\\PycharmProjects\\python_training\\env\\drivers\\firefoxdriver\\geckodriver.exe')
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)

    def create_group(self, group):
        # создание группы
        driver = self.driver
        self.open_groups_page()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # сохранение группы
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("group page").click()

    def open_groups_page(self):
        # открытие группы
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def open_home_page(self):
        # открытие страницы
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
