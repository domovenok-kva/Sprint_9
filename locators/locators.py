from selenium.webdriver.common.by import By

class Locators:

    create_acc_bttn  = (By.XPATH, "//a[contains(@href, '/signup')]")
    login_bttn = (By.XPATH, "//a[contains(@href, 'signin')]")

    name_inpt = (By.XPATH, "//div[text()='Имя']/following-sibling::input[@type='text']")
    surname_inpt = (By.XPATH, "//div[text()='Фамилия']/following-sibling::input[@type='text']")
    nickname_inpt = (By.XPATH, "//div[text()='Имя пользователя']/following-sibling::input[@type='text']")
    email_inpt = (By.XPATH, "//div[text()='Адрес электронной почты']/following-sibling::input[@type='text']")
    new_password_inpt = (By.XPATH, "//div[text()='Пароль']/following-sibling::input[@type='password']")

    create_bttn = (By.XPATH, "//button[contains(@class, 'style_button__1FFWl styles_button__146Sy style_button_style_dark-blue__1cpq7')]")

    login_form = (By.XPATH, "//form[contains(@class, 'styles_form__2nwxz styles_form__2_42b')]")

    log_email_inpt = (By.XPATH, "//div[text()='Электронная почта']/following-sibling::input[@type='text']")
    log_passwrd_inpt = (By.XPATH, "//div[text()='Пароль']/following-sibling::input[@type='password']")
    log_form_bttn =  (By.XPATH, "//button[contains(@class, 'style_button__1FFWl styles_button__1jD3X style_button_style_dark-blue__1cpq7')]")

    exit_bttn =  (By.XPATH, "//a[text()='Выход']")

    recipie_creation_bttn = (By.XPATH, "//a[contains(@href, 'recipes/create')]")

    recipie_form = (By.XPATH, "//form[contains(@class, 'styles_form__2nwxz styles_form__3XFkE')]")

    recipie_name_inpt = (By.XPATH, "//div[text()='Название рецепта']/following-sibling::input[@type='text']")
    recipie_time_inpt = (By.XPATH, "//div[text()='Время приготовления']/following-sibling::input[@type='text']")
    recipie_description_txtarea = (By.XPATH, "//div[text()='Описание рецепта']/following-sibling::textarea[contains(@class,'styles_textareaField')]")
    ingrid_amount_inpt = (By.XPATH, "//input[contains(@class, 'styles_ingredientsAmountValue')]")

    breakfast_chckbox = (By.XPATH, "//button[contains(@style, 'background-color: orange')]")
    lunch_chckbox = (By.XPATH, "//button[contains(@style, 'background-color: green')]")
    dinner_chckbox = (By.XPATH, "//button[contains(@style, 'background-color: purple')]")

    ingrid_choose_inpt = (By.XPATH, "//input[contains(@class, 'styles_inputField__3eqTj styles_ingredientsInput__1zzql')]")
    list_of_ingrids_dropdown = (By.XPATH, "//div[contains(@class, 'styles_ingredientsInputs__1W-NV')]/div[contains(@class, 'styles_container__3ukwm')]")

    add_ingrid_bttn = (By.XPATH, "//div[text()='Добавить ингредиент']")

    picture_of_dish = (By.CSS_SELECTOR, "input[type='file']")

    create_recip_bttn = (By.XPATH, "//button[text()='Создать рецепт']")
    name_of_recip = (By.XPATH, "//h1[contains(@class, 'styles_single-card__title__2QMPq')]")
    recip_fin_card = (By.XPATH, "//div[contains(@class, 'styles_single-card__info__2_cny')]")

# Добавить в покупки

    

