from rembg import remove
from PIL import Image
import os

# Pasta de entrada e saída
input_folder = 'C:/Users/normady/Desktop/REMOVE FUNDO IMAGEM/FOTOS_JPEG/'
output_folder = 'C:/Users/normady/Desktop/REMOVE FUNDO IMAGEM/sem_fundo/'

# Verifique se a pasta de saída existe, senão a crie
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterar sobre todos os arquivos na pasta de entrada
for filename in os.listdir(input_folder):
    # Verificar se o arquivo é uma imagem
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Caminho da imagem de entrada
        input_path = os.path.join(input_folder, filename)
        # Abrir a imagem
        input_image = Image.open(input_path)
        # Remover o fundo
        output_image = remove(input_image)
        # Caminho da imagem de saída (convertendo para PNG)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')
        # Salvar a imagem sem fundo
        output_image.save(output_path)

print("Processamento concluído.")
