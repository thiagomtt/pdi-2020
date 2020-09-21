# Projeto 1 - Processamento Digital de Imagens
#
# Implementação da técnica de preenchimento de borda pelo valor do pixel mais próximo
#
# Grupo:
# Agustin Gabriel Amaral Castillo
# Jorge Vinicius Gonçalves
# Thiago de Moraes Teixeira
# Victoria de Martini de Souza


# Bibliotecas
import matplotlib.pyplot as plt
import numpy as np


# Default function to get image info
def image_info(img):
    print(f'Tamanho: {img.shape}\n',
          f'Tipo de dado: {img.dtype}\n',
          f'Menor valor: {img.min()}\n',
          f'Maior valor: {img.max()}\n',
          f'Valores únicos: {len(np.unique(img))}', sep=''
          )


# Read original image 
img = plt.imread('cameraman.tiff')
num_rows, num_cols= img.shape

# Define o tamanho da borda em pixels
tamanho_borda = 10

# Cria a imagem IMG_BORDER com borda preta (para ser preenchida)
# adicionando 2x tamanho da borda em linhas/colunas -> tamanho/2 para cada lado da imagem
# e copiando o valor dos pixels da imagem original para seus respectivos lugares no centro da nova imagem
img_border = np.zeros((num_rows+(tamanho_borda*2), num_cols+(tamanho_borda*2)), dtype=img.dtype)
for row in range(num_rows):
    for col in range(num_cols):   
        img_border[row+(tamanho_borda), col+(tamanho_borda)] = img[row, col]


# Varre a nova imagem alterando os valores dos pixels da borda, para o valor do pixel mais proximo da imagem original
for row in range(num_rows+(tamanho_borda*2)):
	for col in range(num_cols+(tamanho_borda*2)):
		if row<=tamanho_borda:
			if col<=tamanho_borda:
				img_border[row, col] = img[0, 0]

			elif col>=num_cols+(tamanho_borda-1):
				img_border[row, col] = img[0, num_cols-1]

			else:
				img_border[row, col] = img[0, col-tamanho_borda]

		elif row>=num_rows+(tamanho_borda-1):
			if col<=tamanho_borda:
				img_border[row, col] = img[num_rows-1, 0]

			elif col>=num_cols+(tamanho_borda-1):
				img_border[row, col] = img[num_rows-1, num_cols-1]	

			else:
				img_border[row, col] = img[num_rows-1, col-tamanho_borda]

		else:
			if col<tamanho_borda:
				img_border[row, col] = img[row-tamanho_borda, 0]

			elif col>num_cols+(tamanho_borda-1):
				img_border[row, col] = img[row-tamanho_borda, num_cols-1]


# Mostra info das imagens apos o procedimento
print('Imagem original')
image_info(img)
print()
print('Imagem com borda')
image_info(img_border)


# Compara as duas imagens lado a lado
plt.subplot(1, 2, 1)
plt.imshow(img, 'gray')
plt.subplot(1, 2, 2)
plt.imshow(img_border, 'gray')
plt.show()
