# Projeto 3 - Processamento Digital de Imagens
#
# Implementação de dilatação, erosão, abertura, fechamento e transformada top-hat em nível de cinza, utilizando um elemento estruturante uniforme "flat"
#
# Grupo:
# Agustin Gabriel Amaral Castillo
# Jorge Vinicius Gonçalves
# Thiago de Moraes Teixeira
# Victoria de Martini de Souza

# Bibliotecas
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft2, ifft2, fftfreq, fftshift


# Função de erosão
def erosion(img, elem_est):
	num_rows, num_cols = img.shape
	num_rows_ee, num_cols_ee = elem_est.shape

	half_r_ee = num_rows_ee//2
	half_c_ee = num_cols_ee//2

	# Imagem rodeada de 0, para não haver erro com o elemento estrutural 3x3
	img_padded = np.pad(img, ((half_r_ee,half_r_ee),(half_c_ee,half_c_ee)), mode='constant')

	# Imagem resultante
	img_res = np.zeros_like(img)

	# Varre a imagem com borda e aplica o menor valor da vizinhança ao pixel central do elemento estrutural 
	# na imagem_res que será a saída
	# Valor de minimum inicia com 300 para qualquer pixel ser menor do que ele, assim comparando com todos
	# pois o valor máximo de um pixel é 255
	for row in range(1, num_rows+1):
		for col in range(1, num_cols+1):
			minimum = 300
			for s in range(num_rows_ee):
				for t in range(num_cols_ee):
					current = img_padded[row-1+s, col-1+t] * elem_est[s, t]
					if current < minimum and current>0:
						minimum = current
			img_res[row-1, col-1] = minimum

	return img_res


# Função de dilatação
def dilation(img, elem_est):
	num_rows, num_cols = img.shape
	num_rows_ee, num_cols_ee = elem_est.shape

	half_r_ee = num_rows_ee//2
	half_c_ee = num_cols_ee//2

	# Imagem rodeada de 0, para não haver erro com o elemento estrutural 3x3
	img_padded = np.pad(img, ((half_r_ee,half_r_ee),(half_c_ee,half_c_ee)), mode='constant')

	# Imagem resultante
	img_res = np.zeros_like(img)

	# Varre a imagem com borda e aplica o maior valor da vizinhança ao pixel central do elemento estrutural 
	# na imagem_res que será a saída
	# Valor de maximo inicia com -1 para qualquer pixel ser maior do que ele, assim comparando com todos
	# pois o valor mínimo de um pixel é 0
	for row in range(1, num_rows+1):
		for col in range(1, num_cols+1):
			maximum = -1
			for s in range(num_rows_ee):
				for t in range(num_cols_ee):
					current = img_padded[row-1+s, col-1+t] * elem_est[s, t]
					if current > maximum:
						maximum = current
			img_res[row-1, col-1] = maximum

	return img_res


# Função de abertura
def abertura(img, elem_est):

	# Imagem resultante
	img_res = np.zeros_like(img)

	# Abertura - aplica-se a erosão e a dilatação logo após 
	img_res = erosion(img, elem_est)
	img_res = dilation(img_res, elem_est)

	return img_res


# Função de fechamento
def fechamento(img, elem_est):

	# Imagem resultante
	img_res = np.zeros_like(img)

	# Fechamento - aplica-se a dilatação e a erosão logo após 
	img_res = dilation(img, elem_est)
	img_res = erosion(img_res, elem_est)

	return img_res


# Função da transformada top-hat
def top_hat(img, elem_est):

	img_opened = np.zeros_like(img)

	# Transformada Top-Hat - aplica-se a abertura e logo após subtrai a imagem original da 'imagem aberta'
	img_opened = abertura(img, elem_est)
	img_top_hat = img - img_opened

	return img_top_hat


def main():
	# Elementro estruturante uniforme
	elemento_estruturante = np.array([[1, 1, 1],
							 		  [1, 1, 1],
							 		  [1, 1, 1]])

	# Imagem padrão usada
	img = plt.imread('images/cameraman.tiff')

	# Funções construídas 
	img_erosion = erosion(img, elemento_estruturante)
	img_dilation = dilation(img, elemento_estruturante)
	img_abertura = abertura(img, elemento_estruturante)
	img_fechamento = fechamento(img, elemento_estruturante)
	img_top_hat = top_hat(img, elemento_estruturante)

	# Plota todos os resultados lado a lado 
	plt.subplot(1, 6, 1)
	plt.imshow(img, 'gray')
	plt.xlabel('Original')
	plt.subplot(1, 6, 2)
	plt.imshow(img_erosion, 'gray')
	plt.xlabel('Erosão')
	plt.subplot(1, 6, 3)
	plt.imshow(img_dilation, 'gray')
	plt.xlabel('Dilatação')
	plt.subplot(1, 6, 4)
	plt.imshow(img_abertura, 'gray')
	plt.xlabel('Abertura')
	plt.subplot(1, 6, 5)
	plt.imshow(img_fechamento, 'gray')
	plt.xlabel('Fechamento')
	plt.subplot(1, 6, 6)
	plt.imshow(img_top_hat, 'gray')
	plt.xlabel('Transformada Top-Hat')
	plt.show()

if __name__ == "__main__":
	main()