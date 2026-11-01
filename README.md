Contador de Monedas Colombianas con YOLOv8 y OpenCV
Documentacion Tecnica del Proyecto

Descripcion General
Sistema de vision artificial desarrollado en Python para la deteccion, clasificacion y sumatoria en tiempo real de denominaciones de monedas colombianas. El proyecto emplea un modelo de deteccion de objetos YOLOv8 entrenado a medida y procesa el streaming de video transmitido desde un dispositivo Android. Al delegar la carga computacional pesada al PC, el sistema logra un conteo fluido y preciso sin depender del hardware limitado de un telefono movil.

Justificacion de la Arquitectura
El proyecto inicio con un enfoque movil nativo utilizando React Native y Expo. Sin embargo, debido a conflictos de dependencias, problemas de compilacion con dependencias de Android Studio y errores nativos de modulos de camara, la arquitectura se refactorizo hacia un modelo cliente-servidor distribuido en red local.

* Captura de Video: Se utiliza un dispositivo Android (ej. Motorola Moto G Max 5G) ejecutando la aplicacion IP Webcam. El telefono actua unicamente como un sensor optico inalambrico.
* Conectividad: La transmision de video se realiza via HTTP sobre una red local directa (Hotspot o Zona Wi-Fi compartida desde el movil). Este enfoque elimina la latencia de routers intermediarios y evita bloqueos por firewalls institucionales o publicos.
* Procesamiento Central (Inferencia): Un PC con Windows (ej. procesador AMD Ryzen 5) ejecutando Python 3.12 recibe el flujo de datos para procesarlo de forma local.
* Motor de Vision y Graficos: Se emplea Ultralytics YOLOv8 para la inferencia y OpenCV (cv2) para decodificar el stream, dibujar las cajas delimitadoras (bounding boxes) y renderizar la interfaz con el total acumulado.

Estructura del Proyecto y Archivos

* CAMARA.PY: Es el script principal de ejecucion. Establece un bucle infinito que lee el feed de video. En cada frame, ejecuta la inferencia de YOLO, extrae los identificadores de clase, utiliza expresiones regulares para aislar unicamente los valores numericos de las etiquetas del dataset, suma los valores y proyecta el texto con el total en COP sobre la imagen en tiempo real.
* entrenar.py: Script auxiliar utilizado para el fine-tuning del modelo base. Descarga los pesos pre-entrenados y aplica transferencia de aprendizaje sobre el dataset local de monedas.
* runs/detect/train-2/weights/best.pt: Archivo binario con los pesos finales del modelo neuronal despues del entrenamiento.
* dataset/: Directorio estructurado que contiene las imagenes de entrenamiento, validacion y el archivo de configuracion data.yaml con las rutas y nombres de las clases.

Requisitos Previos del Sistema

Entorno de PC:

* Sistema Operativo: Windows 10 o Windows 11
* Entorno de ejecucion: Python 3.12 o superior
* Dependencias principales: Instalar mediante el comando "pip install ultralytics opencv-python"
* Recursos de hardware: Se recomienda un procesador multinucleo para mantener un framerate estable durante la inferencia.

Entorno Movil:

* Dispositivo con sistema operativo Android.
* Aplicacion "IP Webcam" instalada desde la Google Play Store.

Guia de Configuracion y Ejecucion

1. Preparacion de la Red Local:
Para garantizar una conexion sin interrupciones, enciende la Zona Wi-Fi (Hotspot) en el telefono Android. Conecta el PC a esta nueva red inalambrica.
2. Inicializacion del Sensor Optico:
Abre IP Webcam en el dispositivo movil. Se recomienda bajar ligeramente la resolucion de video en los ajustes de la app para reducir el consumo de red. Ve al final del menu y selecciona "Start server". Toma nota de la direccion IP local que aparece en la parte inferior de la pantalla de la camara (usualmente 192.168.43.X).
3. Configuracion del Script de Inferencia:
Abre el archivo CAMARA.PY en tu editor de codigo. Localiza la variable de captura y actualiza la ruta HTTP con la IP obtenida en el paso anterior. Asegurate de mantener el sufijo /video al final de la URL.
4. Ejecucion del Sistema:
Abre una terminal, navega a la carpeta del proyecto e inicia el script ejecutando: python CAMARA.PY.
El sistema abrira una ventana mostrando el video en vivo con el procesamiento de vision artificial superpuesto.
Control: Presiona la tecla "q" en el teclado mientras la ventana de video este activa para romper el bucle, liberar el buffer de video y cerrar el programa de forma segura.

Desarrollo y Entrenamiento del Modelo
El modelo fue entrenado localmente partiendo de la arquitectura base yolov8n.pt. El proceso de entrenamiento toma el archivo data.yaml para ubicar las imagenes etiquetadas de las monedas y generar parametros de deteccion adaptados a las condiciones de iluminacion. Si el modelo es demasiado estricto al detectar, se puede ajustar el umbral de confianza (conf) en el script principal, o lanzar un reentrenamiento ejecutando entrenar.py aumentando el numero de epocas para mejorar la precision.

nota: en caso de querer aplicarlo debe instalar una app especial en telefono y cuidar bien el tema de las rutas, de lo contrario no servira, adjunto un archivo best.pt ya entrenado pero en caso de algun malfuncionamiento puede ejecutar el entrenar.py y el mismo hace el proceso

Autor(es): Jeicob David Pinilla Ruiz y fabian abril casallas
Programa: Ingenieria Mecatronica, Universidad Militar Nueva Granada
