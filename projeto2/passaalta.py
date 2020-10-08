# Projeto 2 - Processamento Digital de Imagens
#
# Implementação da filtragem passa-alta utilizando o filtro Butterworth
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

# Read original image 
img = plt.imread("images/test_image.tiff")

# Plota a imagen original 
plt.subplot(1, 3, 1)
plt.imshow(img, 'gray')

# Default function for generate frequencies of rows and cols
def generate_frequencies(num_rows, num_cols):
    # Gera frequências do sinal tal que a frequência zero esteja no centro dos arrays
    freq_r = fftfreq(num_rows)
    freq_c = fftfreq(num_cols)
    freq_r = fftshift(freq_r)
    freq_c = fftshift(freq_c)  

    return freq_r, freq_c


num_rows, num_cols = img.shape
# Adiciona zeros ao final da imagem, para evitar interferência com as diversas cópias (virtuais) da imagem
img_padded = np.pad(img, ((0, num_rows), (0, num_cols)), mode='constant', constant_values=0)

# Transformada de Fourier
Fimg = fft2(img_padded)
Fimg = fftshift(Fimg)

# Filtro Passa-alta Butterworth
def high_pass_butterwoorth_filter(img, d0, n):

	num_rows, num_cols = img.shape
	freq_r, freq_c = generate_frequencies(num_rows, num_cols)

	high_pass_butterwoorth_filter = np.zeros([num_rows, num_cols])

	for row in range(num_rows):
		for col in range(num_cols):
			distance = np.sqrt(freq_r[row]**2 + freq_c[col]**2)
			high_pass_butterwoorth_filter[row, col] = 1/(1 + (d0/(distance+1e-10)**(2*n)))

	return high_pass_butterwoorth_filter

# passa-alta laplaciano -> d0=2 , n=1 
# passa-alta gaussiano -> d0=0.01 , n=1
highpass_filter = high_pass_butterwoorth_filter(img_padded, 0.01, 1)

# Plota o filtro para nivel de comparação 
plt.subplot(1, 3, 2)
plt.imshow(highpass_filter, cmap='gray')

# Aplicação do filtro na imagem 
Fimg_filtered = highpass_filter*Fimg

# fftshift é utilizado para retornar o espectro para as posições esperadas pela função ifft2
Fimg_filtered = fftshift(Fimg_filtered)
img_filtered = ifft2(Fimg_filtered)

# A transformação inversa de Fourier possui números complexos para niveis de precisão
# Aqui filtramos somente a parte real do resultado 
img_filtered = np.real(img_filtered)

# Seleciona imagem final no quadrante superior esquerdo
img_filtered = img_filtered[:num_rows, :num_cols]

# Plota a imagem final 
plt.subplot(1, 3, 3)
plt.imshow(img_filtered, 'gray')
plt.show()
