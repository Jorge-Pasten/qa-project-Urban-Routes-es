import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    # Configurar la dirección
    from_field = (By.ID,'from')
    to_field = (By.ID,'to')

    # Seleccionar tarifa Comfort
    order_taxi_button = (By.XPATH, '//*[contains(text(), "Pedir un taxi")]')
    comfort_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    comfort_tariff_button = (By.XPATH, "*//div[contains(@class, ' tcard active') and .//dic[text()='Comfort']*)")


    # Ingresar número de teléfono.
    add_phone_number = (By.CLASS_NAME, 'np-text')
    phone_number_field = (By.ID, 'phone')
    next_button = (By.XPATH, '//*[contains(text(), "Siguiente")]')
    sms_code = (By.ID, 'code')
    confirm_button = (By.XPATH, '//*[contains(text(), "Confirmar")]')

    # Añadir tarjeta de crédito
    payment_method_button = (By.CLASS_NAME, 'pp-text')
    add_card_button = (By.XPATH, '//*[contains(text(), "Agregar tarjeta")]')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.XPATH, '//div[@class="card-code-input"]/input[@id="code"]') #(By.ID, 'code')
    add_button = (By.XPATH, "//button[@type='submit' and text()='Agregar']")
    card_added = (By.XPATH, '//*[@id="number"]')
    x_button = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active .close-button')

    # Mensaje para el controlador
    comment_field = (By.ID, 'comment')

    # Solicitar una manta y pañuelos
    blanket_and_scarves_slider = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div[contains(@class, 'r-sw')]//span[@class='slider round']")

    # Solicitar 2 helados
    ice_cream_plus_counter = (By.CLASS_NAME, "counter-plus") #(By.XPATH, "(//div[@class='counter-plus'])[1]")
    ice_cream_counter = (By.CLASS_NAME, "counter-plus")

    # Aparece modal para buscar un taxi
    taxi_search_button = (By.CLASS_NAME, 'smart-button-wrapper')


    # MÉTODOS

    # Configurar dirección
    def __init__(self, driver):
        self.driver = driver
        self.locators = UrbanRoutesPage

    def set_from(self, from_address):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.to_field))
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Seleccionar tarifa Comfort
    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Pedir un taxi")]')))
        self.driver.find_element(*self.order_taxi_button).click()

    def click_comfort_tariff_button(self):
        self.driver.find_element(*self.comfort_button).click()

    def is_comfort_tariff_selected(self):
        try:
            self.driver.find_element(*self.comfort_button)
            return True
        except:
            return False


    # Llenar número de teléfono
    def click_add_phone_number(self):
        self.driver.find_element(*self.add_phone_number).click()

    def set_phone_number(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'phone')))
        self.driver.find_element(*self.phone_number_field).send_keys(data.phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_sms_code(self, code):
        self.driver.find_element(*self.sms_code).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click()

    def validate_phone_number(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.add_phone_number))
        displayed_number = self.driver.find_element(*self.add_phone_number).text
        assert displayed_number == data.phone_number


    # Añadir tarjeta de crédito
    def click_payment_method_button(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp-text')))
        self.driver.find_element(*self.payment_method_button).click()

    def click_add_card_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Agregar tarjeta")]')))
        self.driver.find_element(*self.add_card_button).click()

    def click_card_number_field(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'number')))
        self.driver.find_element(*self.card_number_field).click()

    def set_card_number_field(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(data.card_number)

    def click_card_code_field(self):
        self.driver.find_element(*self.card_code_field).click()

    def set_card_code_field(self, card_code):
        self.driver.find_element(*self.card_code_field).send_keys(card_code)

    def click_add_button(self):
        self.driver.find_element(*self.add_button).click()

    def click_x_button(self):
        self.driver.find_element(*self.x_button).click()

    def validate_card_number(self):
        actual_card_number = self.driver.find_element(*self.card_added).get_property('value')
        return actual_card_number

    def close_window(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.x_button).click()


    # Mensaje para el controlador
    def set_comment_field(self, message_for_driver):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'comment')))
        self.driver.find_element(*self.comment_field).send_keys(message_for_driver)

    def get_comment_field(self):
        return self.driver.find_element(*self.comment_field).get_attribute('value')

    # Solicitar una manta y pañuelos
    def click_blanket_and_scarves_slider(self):
        self.driver.find_element(*self.blanket_and_scarves_slider).click()


    # Solicitar 2 helados
    def click_ice_cream_plus_counter(self):
        self.driver.find_element(*self.ice_cream_plus_counter).click()

    def get_selected_ice_cream_count(self):
        ice_cream_count_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]').text
        return int(ice_cream_count_element)

    # Aparece modal para buscar un taxi
    def click_taxi_search_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')))
        self.driver.find_element(*self.taxi_search_button).click()

