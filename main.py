import qrcode
import os

# Función para contar archivos existentes y evitar duplicados
def contar_archivos():
    contador = 1
    while os.path.exists(f'codigo_qr_{contador}.png'):
        contador += 1
    return contador

# Pedir al usuario que ingrese la URL
url = input('Ingresa la URL de tu página web: ')

# Crear el código QR con alta resolución
qr = qrcode.QRCode(
    version=1,  # Controla el tamaño del código QR (del 1 al 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Mayor corrección de errores
    box_size=20,  # Tamaño más grande de cada caja para mayor resolución
    border=4,  # Tamaño del borde
)

qr.add_data(url)
qr.make(fit=True)

# Crear la imagen del QR con alta resolución
img = qr.make_image(fill='black', back_color='white')

# Generar nombre único para el archivo
contador = contar_archivos()
filename = f'qrs/codigo_qr_{contador}.png'

# Guardar la imagen en un archivo PNG con un nombre único
img.save(filename)

print(f"Código QR generado y guardado como '{filename}' en alta resolución.")
