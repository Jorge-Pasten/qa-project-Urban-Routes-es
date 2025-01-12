import data
import selector
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    # MÉTODOS
    # Configurar dirección
    def __init__(self, driver):
        self.driver = driver
        self.locators = UrbanRoutesPage

    def set_from(self, from_address):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(selector.from_field))
        self.driver.find_element(*selector.from_field).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector.to_field))
        self.driver.find_element(*selector.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*selector.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*selector.to_field).get_property('value')

    # Seleccionar tarifa Comfort
    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Pedir un taxi")]')))
        self.driver.find_element(*selector.order_taxi_button).click()

    def click_comfort_tariff_button(self):
        self.driver.find_element(*selector.comfort_button).click()

    def is_comfort_tariff_selected(self):
        try:
            self.driver.find_element(*selector.comfort_button)
            return True
        except:
            return False


    # Llenar número de teléfono
    def click_add_phone_number(self):
        self.driver.find_element(*selector.add_phone_number).click()

    def set_phone_number(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'phone')))
        self.driver.find_element(*selector.phone_number_field).send_keys(data.phone_number)

    def click_next_button(self):
        self.driver.find_element(*selector.next_button).click()

    def set_sms_code(self, code):
        self.driver.find_element(*selector.sms_code).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*selector.confirm_button).click()

    def validate_phone_number(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector.add_phone_number))
        displayed_number = self.driver.find_element(*selector.add_phone_number).text
        assert displayed_number == data.phone_number


    # Añadir tarjeta de crédito
    def click_payment_method_button(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp-text')))
        self.driver.find_element(*selector.payment_method_button).click()

    def click_add_card_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Agregar tarjeta")]')))
        self.driver.find_element(*selector.add_card_button).click()

    def click_card_number_field(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'number')))
        self.driver.find_element(*selector.card_number_field).click()

    def set_card_number_field(self, card_number):
        self.driver.find_element(*selector.card_number_field).send_keys(data.card_number)

    def click_card_code_field(self):
        self.driver.find_element(*selector.card_code_field).click()

    def set_card_code_field(self, card_code):
        self.driver.find_element(*selector.card_code_field).send_keys(card_code)

    def click_add_button(self):
        self.driver.find_element(*selector.add_button).click()

    def click_x_button(self):
        self.driver.find_element(*selector.x_button).click()

    def validate_card_number(self):
        actual_card_number = self.driver.find_element(*selector.card_added).get_property('value')
        return actual_card_number


    # Mensaje para el controlador
    def set_comment_field(self, message_for_driver):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'comment')))
        self.driver.find_element(*selector.comment_field).send_keys(message_for_driver)

    def get_comment_field(self):
        return self.driver.find_element(*selector.comment_field).get_attribute('value')

    # Solicitar una manta y pañuelos
    def click_blanket_and_scarves_slider(self):
        self.driver.find_element(*selector.blanket_and_scarves_slider).click()

    def get_blanket_and_scarves_selected(self):
        return self.driver.find_element(*selector.blanket_and_scarves_selected)


    # Solicitar 2 helados
    def click_ice_cream_plus_counter(self):
        self.driver.find_element(*selector.ice_cream_plus_counter).click()

    def get_selected_ice_cream_count(self):
        ice_cream_count_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]').text
        return int(ice_cream_count_element)

    # Aparece modal para buscar un taxi
    def click_taxi_search_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')))
        self.driver.find_element(*selector.taxi_search_button).click()

