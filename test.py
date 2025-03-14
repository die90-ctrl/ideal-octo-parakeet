import base64
from PIL import Image
from io import BytesIO

# Reemplaza 'base64_string' con tu cadena base64
base64_string = "TU_CADENA_BASE64_AQUÍ"

# Decodificando la cadena base64
img_data = base64.b64decode(base64_string)

# Convertir los datos decodificados en una imagen
image = Image.open(BytesIO(img_data))

# Mostrar la imagen
image.show()
