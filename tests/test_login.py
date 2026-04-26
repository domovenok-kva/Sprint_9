import allure
from page_objects.login_page import LoginPage
from page_objects.create_acc_page import CreateAccPage
from data.urls import Urls

class TestCreateAcc:

    @allure.title("Авторизация")
    @allure.step("Нажать кнопку «Войти»")
    def test_createacc_bttn_click(self, driver):
        log_pg = LoginPage(driver)
        create_pg = CreateAccPage(driver)
        create_pg.create_acc_bttn_click()
        log_pg.login_bttn_click()
        assert log_pg.correct_page_adress() == Urls.login_user_url
    
    @allure.step("Заполнить все поля формы авторизации и нажать кнопку «Войти».")
    @allure.description("Проверить: Произошёл ли переход на главную страницу, отображается ли кнопка «Выход».")
    def test_fillin_all_inpts_in_regform(self, user_data, driver):
        create_pg = CreateAccPage(driver)
        u = user_data
        create_pg.user_registration(u)
        log_pg = LoginPage(driver)
        eml = u['username']
        passwrd = u['password']
        log_pg.user_login(eml, passwrd)
        assert log_pg.exit_bttn_visible()
        assert log_pg.correct_page_adress() == Urls.main_pg_url