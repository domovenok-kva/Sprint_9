import allure
from locators.locators import Locators
from page_objects.base_page import BasePage



class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать на кнопку Войти")
    def login_bttn_click(self):
        self.click_element(Locators.login_bttn)

    @allure.step("Заполнить поле Почта")
    def fillin_log_email_inpt(self, email):
        self.fill_inpt(Locators.log_email_inpt, email)

    @allure.step("Заполнить поле Пароль")
    def fillin_log_passwrd_inpt(self, passwrd):
        self.fill_inpt(Locators.log_passwrd_inpt, passwrd)
    
    @allure.step("Нажать кнопку Войти")
    def login_acc_bttn_click(self):
        self.click_element(Locators.log_form_bttn)

    @allure.title("Залогин")
    def user_login(self, nick, passw):
        self.fillin_log_email_inpt(nick)
        self.fillin_log_passwrd_inpt(passw)
        self.login_acc_bttn_click()
    
    @allure.step("Отображается корректный адрес страницы")
    def correct_page_adress(self):
        self.driver.implicitly_wait(10)
        return self.page_url()
    
    def exit_bttn_visible(self):
        return self.find_element(Locators.exit_bttn)