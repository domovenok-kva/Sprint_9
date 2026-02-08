import allure
from locators.locators import Locators
from page_objects.base_page import BasePage
import secrets
import time
from data.paths_for_test import PathsForTest


class CreateRecipPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать на кнопку Создать рецепт")
    def create_recip_bttn_click(self):
        self.click_element(Locators.recipie_creation_bttn)

    @allure.step("Видимость формы Создания рецепта")
    def recipie_form_is_visible(self):
        return self.find_element(Locators.recipie_form)
    
    @allure.step("Заполнить название рецепта")
    def fillin_recip_name_inpt(self, rec_name):
        self.fill_inpt(Locators.recipie_name_inpt, rec_name)

    @allure.step("Заполнить количество ингридиента")
    def fillin_ingrid_amount_inp(self, ingrid_amount):
        self.fill_inpt(Locators.ingrid_amount_inpt, ingrid_amount)

    @allure.step("Заполнить время приготовления")
    def fillin_recip_time_cooking_inpt(self, time_cook):
        self.fill_inpt(Locators.recipie_time_inpt, time_cook)

    @allure.step("Заполнить описание рецепта")
    def fillin_ricip_description(self, recip_descrip):
        self.fill_inpt(Locators.recipie_description_txtarea, recip_descrip)


    @allure.step("Выбор тега")
    def choose_chckbox(self, number):
        if number == 1:
            self.click_element(Locators.lunch_chckbox)
            self.click_element(Locators.dinner_chckbox)
        elif number == 2:
            self.click_element(Locators.breakfast_chckbox)
            self.click_element(Locators.dinner_chckbox)
        elif number == 3:
            self.click_element(Locators.breakfast_chckbox)
            self.click_element(Locators.lunch_chckbox)
        elif number == 4:
            self.click_element(Locators.dinner_chckbox)
        elif number == 5:
            self.click_element(Locators.lunch_chckbox)
        elif number == 6:
            self.click_element(Locators.breakfast_chckbox)
        elif number == 7:
            pass

    @allure.step("Выбор случайного ингридиента")
    def choose_random_ingrid(self, letter):
        self.fill_inpt(Locators.ingrid_choose_inpt, letter)
        time.sleep(1) 
        suggestions = self.find_elements(Locators.list_of_ingrids_dropdown)
        name_list = [s.text for s in suggestions if s.text.strip()]
        result = secrets.choice(name_list)
        for s in suggestions:
            if s.text == result:
                s.click()
            break
        
    @allure.step("Клик на Добавить ингредиент")
    def choose_ingrid_bttn_click(self):
        self.click_element(Locators.add_ingrid_bttn)

    @allure.step("Загрузить фото блюда")
    def downlod_recip_photo(self, number):
        if number % 2 == 0:
            self.photo_dwnld(Locators.picture_of_dish, PathsForTest.full_path1)
        else:
            self.photo_dwnld(Locators.picture_of_dish, PathsForTest.full_path2)

    @allure.step("НАажть на кнопку Создать рецепт")
    def finally_create_recip_bttn_click(self):
        self.click_element(Locators.create_recip_bttn)
    
    @allure.step("Найти название рецепта на странице")
    def finde_recip_name_on_page(self):
        return self.get_element_value(Locators.name_of_recip)
    
    @allure.step("Видимость карточки созданного рецепта")
    def card_of_create_recip_is_visible(self):
        return self.element_visability(Locators.recip_fin_card)

    @allure.title("Заполенение формы рецепта")
    def recip_form_fillin(self,rec_name, number, letter, ingrid_amount, time_cook, recip_descrip):
        self.fillin_recip_name_inpt(rec_name)
        self.choose_chckbox(number)

        for i in range(number):
            self.choose_random_ingrid(letter)
            self.fillin_ingrid_amount_inp(ingrid_amount)
            self.choose_ingrid_bttn_click() 
        
        self.fillin_recip_time_cooking_inpt(time_cook)
        self.fillin_ricip_description(recip_descrip)
        
        self.downlod_recip_photo(number)
        self.finally_create_recip_bttn_click()

