import matplotlib.pyplot as plt
import numpy as np


# Default function to get image info
def image_info(img):
    print(f'Tamanho: {img.shape}\n',
          f'Tipo de dado: {img.dtype}\n',
          f'Menor valor: {img.min()}\n',
          f'Maior valor: {img.max()}\n',
          f'Valores únicos: {len(np.unique(img))}', sep='')


# Read img 
img = plt.imread('pacman.tiff')
num_rows, num_cols = img.shape


# Cria a imagem com borda preta
# adicionando +20px em linhas/colunas -> 10px para cada lado da imagem
# e copiando o valor dos pixels da imagem original para seus respectivos lugares no centro da nova imagem
img_border = np.zeros((num_rows+20, num_cols+20), dtype=img.dtype)
for row in range(num_rows):
    for col in range(num_cols):   
        img_border[row+10, col+10] = img[row, col]

print(num_rows, num_cols)
# Varre a nova imagem alterando os valores dos pixels da borda, para o valor do pixel mais proximo da imagem original
for row in range(num_rows+20):
	for col in range(num_cols+20):
		if row<=10:
			if col<=10:
				img_border[row, col] = img[0, 0]
			elif col>=num_cols-1:
				img_border[row, col] = img[0, num_cols-1]
			else:
				img_border[row, col] = img[0, col-10]
		elif row>=num_rows-1:
			if col<=10:
				img_border[row, col] = img[num_rows-1, 0]
			elif col>=num_cols-1:
				img_border[row, col] = img[num_rows-1, num_cols-1]	
			else:
				img_border[row, col] = img[num_rows-1, col-10]
		else:
			if col<10:
				img_border[row, col] = img[row-10, 0]
			if col>num_cols-1:
				img_border[row, col] = img[row-10, num_cols-1]


# Compare two images
plt.subplot(1, 2, 1)
plt.imshow(img, 'gray')
plt.subplot(1, 2, 2)
plt.imshow(img_border, 'gray')
plt.show()
