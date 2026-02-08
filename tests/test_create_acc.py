import allure
from page_objects.create_acc_page import CreateAccPage
from data.urls import Urls

class TestCreateAcc:

    @allure.title("Создание аккаунта")
    @allure.step("Нажать кнопку «Создать аккаунт»")
    def test_createacc_bttn_click(self, driver):
        create_pg = CreateAccPage(driver)
        create_pg.create_acc_bttn_click()
        assert create_pg.correct_page_adress() == Urls.crete_user_url
    
    @allure.step("Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт»")
    @allure.description("Проверить: " \
    "Произошёл ли переход на страницу авторизации, " \
    "отображается ли форма авторизации.")
    def test_fillin_all_inpts_in_regform(self, user_data, driver):
        create_pg = CreateAccPage(driver)
        create_pg.user_registration(user_data)
        assert create_pg.login_form_is_visible()
        assert create_pg.correct_page_adress() == Urls.login_user_url
