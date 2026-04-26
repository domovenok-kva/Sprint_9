import allure
from page_objects.login_page import LoginPage
from page_objects.create_acc_page import CreateAccPage
from page_objects.create_recip import CreateRecipPage
from data.urls import Urls

class TestCreateRecipies:

    @allure.title("Создание рецепта")
    @allure.step("Авторизоваться и перейти на таб «Создать рецепт».")
    def test_create_recip_bttn_clck_with_reg(self, user_data, driver):
        create_pg = CreateAccPage(driver)
        u = user_data
        create_pg.user_registration(u)
        log_pg = LoginPage(driver)
        eml = u['username']
        passwrd = u['password']
        log_pg.user_login(eml, passwrd)
        recep_pg = CreateRecipPage(driver)
        recep_pg.create_recip_bttn_click()
        assert recep_pg.recipie_form_is_visible()

    @allure.step("Заполнить все поля формы создания рецепта и нажать кнопку «Создать рецепт».")
    @allure.description("Примечание (ингредиент должен быть добавлен из списка, для отображения списка необходимо начать вводить название ингридиента в поле ввода)" \
    "Проверить, отображается ли:" \
    "карточка созданного рецепта," \
    "название, которое заполняли при создании.")
    def test_create_recip(self, user_data, data_for_recip_name, random_number_for_chckbx, random_letter_for_ingrid, data_for_ingrid_quantity, data_for_minutes, data_for_desctiption, driver):
        create_pg = CreateAccPage(driver)
        u = user_data
        create_pg.user_registration(u)
        log_pg = LoginPage(driver)
        eml = u['username']
        passwrd = u['password']
        log_pg.user_login(eml, passwrd)
        recep_pg = CreateRecipPage(driver)
        recep_pg.create_recip_bttn_click()

        recip_name = data_for_recip_name        
        recep_pg.recip_form_fillin(recip_name, random_number_for_chckbx, random_letter_for_ingrid, data_for_ingrid_quantity, data_for_minutes, data_for_desctiption)
        name_from_page = recep_pg.finde_recip_name_on_page()
        assert recep_pg.card_of_create_recip_is_visible()
        assert recip_name == name_from_page
        



