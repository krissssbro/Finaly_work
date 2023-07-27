from .pages.login_page import LoginPage, MainPage

def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()