# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group
import time

class T1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\\Users\\roman\\PycharmProjects\\python_training\\env\\drivers\\firefoxdriver\\geckodriver.exe')
        self.driver.implicitly_wait(30)
        self.verificationErrors = []

    def test_t2(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, "admin", "secret")
        self.open_groups_page(driver)
        self.create_group(driver, Group(name="123", header="1234", footer="12345"))
        self.logout(driver)

    def test_t1(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, "admin", "secret")
        self.open_groups_page(driver)
        self.create_group(driver, Group(name="sdf", header="sdf", footer="sdffd"))
        self.logout(driver)
        time.sleep(3)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def create_group(self, driver, group):
        # создание группы
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

    def open_groups_page(self, driver):
        # открытие группы
        driver.find_element_by_link_text("groups").click()

    def login(self, driver, username, password):
        # логин
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        # открытие страницы
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
