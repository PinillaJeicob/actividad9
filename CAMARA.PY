import cv2
import re
from ultralytics import YOLO

modelo = YOLO("C:/contador-monedas/runs/detect/train/weights/best.pt") 
# Asegúrate de volver a poner tu IP exacta de IP Webcam
cap = cv2.VideoCapture('http://192.168.110.11:8080/video') 

while cap.isOpened():
    exito, frame = cap.read()
    if exito:
        resultados = modelo(frame, conf=0.15)
        total_dinero = 0
        
        for deteccion in resultados[0].boxes:
            clase_id = int(deteccion.cls[0])
            nombre_clase = modelo.names[clase_id]
            
            # Esto te mostrará en la terminal negra exactamente qué lee el modelo
            print(f"Etiqueta detectada: {nombre_clase}")
            
            # Extrae solo los dígitos de la etiqueta (ej. saca '500' de 'moneda500')
            numeros = re.findall(r'\d+', nombre_clase)
            if numeros:
                total_dinero += int(numeros[0])

        frame_anotado = resultados[0].plot()
        
        cv2.putText(frame_anotado, f"Total: ${total_dinero} COP", (20, 60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

        cv2.imshow("Conteo de Monedas", frame_anotado)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()