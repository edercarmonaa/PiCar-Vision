# PiCar Vision

PiCar Vision es un prototipo para controlar un carro basado en Raspberry Pi mediante teclado, cámara y procesamiento básico de visión por computadora.

El proyecto reúne pruebas de movimiento por GPIO, vista de cámara, detección de rostros/cuerpo, transmisión de video y lectura de sensores para apoyar la construcción de un carro educativo con Raspberry Pi.

## El problema

Construir un carro con Raspberry Pi suele requerir probar muchas piezas por separado: motores, relevadores, cámara, sensores, transmisión de video y procesamiento de imágenes. Sin una base organizada, esas pruebas quedan dispersas y es fácil perder qué script controla cada componente o publicar accidentalmente archivos locales innecesarios.

Este proyecto ayuda a estudiantes, makers o docentes que necesitan una base simple para validar hardware real antes de avanzar hacia funciones más complejas de visión o autonomía.

## La solución

PiCar Vision agrupa scripts enfocados en pruebas concretas:

- Control del carro con flechas del teclado desde una interfaz `tkinter`.
- Vista de cámara Raspberry Pi integrada en la interfaz.
- Detección con OpenCV usando clasificadores Haar.
- Pruebas directas de GPIO para validar motores, relevadores y LEDs.
- Transmisión/recepción básica de video por socket.
- Lectura de temperatura y humedad con DHT11 y pantalla LCD I2C.

El flujo normal es validar primero GPIO y cámara, después ejecutar una interfaz de control y finalmente experimentar con detección visual o streaming.

## Funcionalidades principales

- Control de movimiento: avanzar, retroceder, girar a la izquierda y girar a la derecha.
- Control por teclado con las flechas en una ventana `tkinter`.
- Activación de pines GPIO usando lógica activa en bajo.
- Visualización de video desde la cámara Pi.
- Detección de rostro, cuerpo completo o parte inferior del cuerpo con OpenCV.
- Detección de bordes/contornos con Canny.
- Pruebas independientes de cámara, GPIO, sensor DHT11, LCD I2C y streaming.

## ¿Qué mejora este proyecto?

- Reduce el tiempo de diagnóstico al separar pruebas de cámara, GPIO, sensores y red.
- Permite comprobar si el cableado del carro responde antes de integrar visión artificial.
- Evita depender de valores sensibles o archivos locales para ejecutar las pruebas.
- Deja una estructura más clara para revisar el proyecto antes de publicarlo.

## ¿Para quién está pensado?

- Estudiantes que están aprendiendo Raspberry Pi, GPIO y OpenCV.
- Docentes que necesitan ejemplos prácticos de robótica educativa.
- Makers que quieren una base inicial para un carro controlado con cámara.

## Tecnologías utilizadas

- Python
- Tkinter
- Raspberry Pi GPIO
- PiCamera
- OpenCV
- Pillow
- imutils
- NumPy
- Adafruit DHT
- LCD I2C mediante `smbus`/`smbus2`
- Sockets TCP para pruebas de video

## Requisitos

Hardware:

- Raspberry Pi con Raspberry Pi OS.
- Cámara compatible con PiCamera.
- Módulo de control para motores o relevadores conectado a GPIO.
- Opcional: sensor DHT11 en GPIO 26.
- Opcional: pantalla LCD I2C.

Software:

- Python 3.
- Paquetes de sistema para cámara, OpenCV, I2C y GPIO según la versión de Raspberry Pi OS.
- Dependencias Python listadas en `requirements.txt`.

En Raspberry Pi OS puede ser necesario instalar paquetes de sistema como:

```bash
sudo apt update
sudo apt install python3-pip python3-tk python3-opencv python3-smbus i2c-tools
```

## Instalación

```bash
git clone https://github.com/tu-usuario/PiCar-Vision.git
cd PiCar-Vision
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Raspberry Pi, algunas librerías de hardware pueden depender de paquetes del sistema. Si `opencv-python`, `RPi.GPIO`, `picamera` o `Adafruit_DHT` fallan desde `pip`, instala la variante recomendada por Raspberry Pi OS para tu modelo y versión.

## Configuración

El proyecto no requiere secretos para funcionar. Las variables disponibles están documentadas en `.env.example`:

| Variable | Uso | Valor por defecto |
| --- | --- | --- |
| `HAAR_CASCADE_DIR` | Carpeta de clasificadores Haar de OpenCV. | `/usr/local/share/OpenCV/haarcascades` |
| `DHT_PIN` | Pin GPIO del sensor DHT11. | `26` |
| `LCD_I2C_ADDR` | Dirección I2C de la pantalla LCD. | `0x3f` |
| `STREAM_HOST` | Host para transmitir video H.264. | `127.0.0.1` |
| `STREAM_PORT` | Puerto para transmitir video H.264. | `8000` |
| `FRAME_SERVER_HOST` | Host del receptor de frames por socket. | `127.0.0.1` |
| `FRAME_SERVER_PORT` | Puerto del receptor de frames por socket. | `8089` |

Si decides usar un archivo `.env`, no lo subas al repositorio. Mantén `.env.example` solo con valores de ejemplo.

## Ejecutar el proyecto

Control principal del carro con detección de rostro:

```bash
python3 control.py
```

También puedes ejecutar directamente:

```bash
python3 interfaz.py
```

Prueba de GPIO del carro:

```bash
python3 prueba1.py
```

Prueba básica de cámara:

```bash
python3 camara.py
```

Detección facial independiente:

```bash
python3 face.py
```

Sensor DHT11 con LCD I2C:

```bash
python3 sensorTemp.py
```

## Uso

1. Conecta el hardware del carro a los pines GPIO definidos en el código.
2. Ejecuta `prueba1.py` para confirmar que los motores, relevadores y LEDs responden.
3. Ejecuta `camara.py` o `face.py` para validar la cámara.
4. Ejecuta `control.py`.
5. Usa las flechas del teclado para mover el carro mientras ves la cámara.

Pines usados por las interfaces principales:

| Función | GPIO |
| --- | --- |
| Izquierda | 4 |
| Derecha | 27 |
| Avanzar | 22 |
| Retroceder | 23 |
| LED derecho | 26 |
| LED izquierdo | 16 |
| LED atrás | 13 |

## Estructura del proyecto

```text
.
├── control.py          # Lanzador de la interfaz principal
├── interfaz.py         # Control del carro con detección de rostro
├── interfaz2.py        # Control del carro con detección de bordes
├── interfaz3.py        # Control con detección de parte inferior del cuerpo
├── interfaz4.py        # Control con detección de cuerpo completo
├── prueba1.py          # Prueba de motores, relevadores y LEDs
├── camara.py           # Prueba simple de cámara
├── face.py             # Detección facial independiente
├── stream.py           # Streaming H.264 por socket
├── server.py           # Receptor de frames por socket
├── sensorTemp.py       # DHT11 + LCD I2C
├── lcd_i2c_driver.py   # Driver LCD I2C
└── tensor.py           # Experimento de detección con TensorFlow
```

## Capturas

El repositorio todavía no incluye capturas reales. Pueden agregarse posteriormente cuando el proyecto se ejecute sobre la Raspberry Pi con el hardware conectado.

## Seguridad

- No guardes contraseñas, tokens, API keys ni credenciales reales dentro del código.
- Usa variables de entorno para configuración local.
- No subas archivos `.env`; este proyecto incluye `.env.example` como plantilla.
- Revisa cualquier cambio con herramientas de búsqueda de secretos antes de publicar.
- `server.py` usa `pickle` para deserializar frames; ejecútalo solo en una red confiable o reemplaza ese formato antes de exponerlo a terceros.

## Pruebas

No hay tests automatizados en este proyecto. La validación actual es manual y depende del hardware:

- `prueba1.py` para GPIO y movimiento.
- `camara.py` o `face.py` para cámara.
- `sensorTemp.py` para DHT11 y LCD.
- `control.py` para integración de interfaz, cámara y movimiento.

## Estado del proyecto

Prototipo funcional para entorno Raspberry Pi. El código contiene pruebas útiles y una interfaz principal, pero aún requiere validación en hardware real antes de considerarse estable.

## Limitaciones actuales

- Depende de hardware específico de Raspberry Pi.
- No incluye tests automatizados.
- `tensor.py` depende de TensorFlow Object Detection API y de archivos de modelo que no están incluidos en el repositorio.
- La transmisión de frames con `pickle` no debe exponerse a redes no confiables.
- Los pines GPIO están definidos directamente en los scripts principales.

## Próximas mejoras

- Centralizar la configuración de pines GPIO.
- Agregar tests para lógica no dependiente de hardware.
- Crear una interfaz única para seleccionar modo de visión.
- Reemplazar `pickle` por un formato de transmisión más seguro.
- Documentar un diagrama de conexión del hardware.
- Agregar capturas reales del proyecto funcionando.

## Contribuciones

1. Haz un fork del repositorio.
2. Crea una rama para tu cambio.
3. Mantén los cambios enfocados y documentados.
4. Prueba en Raspberry Pi cuando el cambio involucre hardware.
5. Abre un pull request explicando qué cambiaste y cómo lo validaste.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
