# Projeto 1 - Processamento Digital de Imagens
#
# Implementação da técnica de preenchimento de borda espelhando os valores dos pixels da imagem original 
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
img = plt.imread('pacman.tiff')
num_rows, num_cols = img.shape

# Define o tamanho da borda em pixels
tamanho_borda = 10

# Cria a imagem IMG_BORDER com borda preta (para ser preenchida)
# adicionando 2x tamanho da borda em linhas/colunas -> tamanho/2 para cada lado da imagem
# e copiando o valor dos pixels da imagem original para seus respectivos lugares no centro da nova imagem
img_border = np.zeros((num_rows+(tamanho_borda*2), num_cols+(tamanho_borda*2)), dtype=img.dtype)
for row in range(num_rows):
    for col in range(num_cols):
        img_border[row+tamanho_borda, col+tamanho_borda] = img[row, col]


for linha_atual in range(tamanho_borda, num_rows+tamanho_borda):
	print(linha_atual)
	diagonal_pixels = tamanho_borda

	for pixel in range(1, tamanho_borda+1):
		# Direção Horizontal esquerda e direita da imagem
		img_border[linha_atual][tamanho_borda-pixel] 										= img[linha_atual-tamanho_borda][pixel]
		img_border[linha_atual][num_cols+(tamanho_borda-1)+pixel] 							= img[linha_atual-tamanho_borda][num_cols-1-pixel]

		# Direção vertical cima e baixo da imagem 
		img_border[tamanho_borda-pixel][linha_atual] 										= img[pixel][linha_atual-tamanho_borda]
		img_border[num_rows+(tamanho_borda-1)+pixel][linha_atual] 							= img[num_rows-1-pixel][linha_atual-tamanho_borda]

		if linha_atual == tamanho_borda:
			# Diagonal superior esquerda
			img_border[linha_atual-pixel][tamanho_borda-pixel] 								= img[pixel][pixel]

			# Diagonal superior direita
			img_border[linha_atual-pixel][num_cols+(tamanho_borda-1)+pixel] 				= img[pixel][num_cols-1-pixel]			

			if diagonal_pixels >= 2:
				for line in range(1, diagonal_pixels):
					# Linhas para esquerda da diagonal superior esquerda  
					img_border[linha_atual-pixel][tamanho_borda-pixel-line]					= img[pixel][pixel+line]

					# Linhas para cima da diagonal superior esquerda
					img_border[linha_atual-pixel-line][tamanho_borda-pixel]					= img[pixel+line][pixel]

					# Linhas para direita da diagonal superior direita
					img_border[linha_atual-pixel][num_cols+(tamanho_borda-1)+pixel+line]	= img[pixel][num_rows-1-pixel-line]

					# Linhas para cima da diagonal superior direita
					img_border[linha_atual-pixel-line][num_cols+(tamanho_borda-1)+pixel]	= img[pixel+line][num_rows-1-pixel]

		if linha_atual == num_rows+(tamanho_borda-1):
			# Diagonal inferior esquerda
			img_border[linha_atual+pixel][tamanho_borda-pixel] 								= img[num_rows-1-pixel][pixel]
			
			# Diagonal inferior direita
			img_border[linha_atual+pixel][num_cols+(tamanho_borda-1)+pixel] 				= img[num_rows-1-pixel][num_cols-1-pixel]			

			if diagonal_pixels >= 2:
				for line in range(1, diagonal_pixels):
					# Linhas para esquerda da diagonal inferior esquerda
					img_border[linha_atual+pixel][tamanho_borda-pixel-line]					= img[num_rows-1-pixel][pixel+line]

					# Linhas para baixo da diagonal inferior esquerda
					img_border[linha_atual+pixel+line][tamanho_borda-pixel]					= img[num_rows-1-pixel-line][pixel]

					# Linhas para a direita da diagonal inferior direita
					img_border[linha_atual+pixel][num_cols+(tamanho_borda-1)+pixel+line]	= img[num_rows-1-pixel][num_cols-1-pixel-line]

					# Linhas para baixo da diagonal inferior direita
					img_border[linha_atual+pixel+line][num_cols+(tamanho_borda-1)+pixel]	= img[num_rows-1-pixel-line][num_cols-1-pixel]

		diagonal_pixels -= 1


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
