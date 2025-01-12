from selenium.webdriver.common.by import By


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
blanket_and_scarves_slider = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
blanket_and_scarves_selected = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input')

# Solicitar 2 helados
ice_cream_plus_counter = (By.CLASS_NAME, "counter-plus") #(By.XPATH, "(//div[@class='counter-plus'])[1]")
ice_cream_counter = (By.CLASS_NAME, "counter-plus")

# Aparece modal para buscar un taxi
taxi_search_button = (By.CLASS_NAME, 'smart-button-wrapper')