# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from model.group import Group
import time

class T1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\\Users\\roman\\PycharmProjects\\python_training\\env\\drivers\\firefoxdriver\\geckodriver.exe')
        self.driver.implicitly_wait(30)
        self.verificationErrors = []

    def test_t2(self):
        self.login("admin", "secret")
        self.create_group(Group(name="123", header="1234", footer="12345"))
        self.logout()

    def test_t1(self):
        self.login("admin", "secret")
        self.create_group(Group(name="sdf", header="sdf", footer="sdffd"))
        self.logout()
        time.sleep(3)

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

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

    def login(self, username, password):
        # логин
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        # открытие страницы
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
