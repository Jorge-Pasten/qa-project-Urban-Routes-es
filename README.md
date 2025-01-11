# Urban Routes: Pruebas automatizadas para solicitar un taxi

## Descripción del Proyecto
Urban Routes es una aplicación para solicitar un taxi en línea donde el pasajero puede configurar su viaje. Este proyecto se ha desarrollado con el fin de someter la aplicación a diferentes pruebas automatizadas para evaluar el proceso de solicitar un taxi.

El proyecto incluye 8 pruebas:

1. Configurar las direcciones de inicio y fin del viaje
2. Seleccionar la tarifa Comfort
3. Ingresar un número de teléfono
4. Agregar el método de pago tarjeta de crédito
5. Escribir un mensaje para el controlador
6. Pedir una manta y pañuelos
7. Pedir 2 helados
8. Aparece el modal para buscar un taxi

## Ejecución de las Pruebas

Para ejecutar las pruebas es necesario:
- Tener configurado Python 3.
- Tener instalados los paquetes `pytest` y `Selenium`.
- Las pruebas se realizan en el navegador Google Chrome (se puede ajustar la configuración del navegador en el método setup_class de la clase TestUrbanRoutes).
- Las pruebas se ejecutan desde el archivo "main.py".

### Tecnologías Utilizadas

- Python
- pytest
- Selenium
- WebDriver