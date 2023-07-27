from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #assert "login" in MainPage.should_be_login_link()  # сообщение об ошибке
        assert "login" in driver.current_url  # сообщение об ошибке

    def should_be_login_page(self):
        #assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login page is not presented"
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_page(self):
        #assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register page is not presented"
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"


