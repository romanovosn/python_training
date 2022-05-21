from selenium import webdriver

class Application:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'/env/drivers/firefoxdriver/geckodriver.exe')
        self.driver.implicitly_wait(30)


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

    def destroy(self):
        self.driver.quit()