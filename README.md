# Urban Routes - Pruebas Automatizadas con Selenium y Pytest

## Descripción del Proyecto
Este proyecto corresponde al Sprint 8 en el proceso de QA Engineer de TripleTen para la aplicación de rutas y transporte Urban Routes.

La aplicación permite a los usuarios crear rutas y calcular la duración y precio del viaje para diferentes tipos de transporte. Incluye opciones como: automóvil personal, a pie, taxi, bicicleta, scooter y auto compartido. Además, cuenta con tres modos de viaje: Óptimo, Flash y Personal.

El objetivo del proyecto fue automatizar las pruebas del flujo de solicitud de taxi y asegurar que las funciones críticas se comporten según lo esperado.

## Tecnologías Utilizadas
- **Python** (para la automatización de pruebas)
- **Selenium WebDriver** (para la automatización del navegador)
- **Pytest** (framework de pruebas)
- **Git y GitHub** (para control de versiones y almacenamiento del código)


## Casos de Prueba Implementados
Los casos de prueba se basan en la siguiente lista de comprobación:

| #  | Descripción del Caso de Prueba | Resultado Esperado |
|----|--------------------------------|-----------------------------|
| 1  | Configurar dirección "Desde" y "Hasta" | La dirección se establece correctamente |
| 2  | Seleccionar tarifa Comfort | Se muestra el precio correcto |
| 3  | Ingresar número de teléfono | El campo acepta solo números válidos |
| 4  | Agregar tarjeta de crédito | El botón 'link' se activa tras perder el enfoque |
| 5  | Enviar mensaje al conductor | El mensaje se muestra en la interfaz |
| 6  | Solicitar manta y pañuelos | El pedido se refleja correctamente |
| 7  | Solicitar 2 helados | Se agregan al pedido |
| 8  | Modal de búsqueda de taxi | Se muestra correctamente |

## Instalación y Ejecución de las Pruebas
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es
```

### 2️⃣ Ejecución de las Pruebas

Para ejecutar las pruebas es necesario:

- Tener configurado Python 3.
- Tener instalados los paquetes pytest y Selenium.
- Las pruebas se realizan en el navegador Google Chrome (se puede ajustar la configuración del navegador en el método setup_class de la clase TestUrbanRoutes).
- Las pruebas se ejecutan desde el archivo "main.py".


## Autor
Proyecto realizado por **Jorge Luis Pasten Peña** como parte del proceso de aprendizaje en QA Engineer de TripleTen.
