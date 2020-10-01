# Projeto 2

### Implementação das filtragems passa-baixa e passa-alta utilizando o filtro Butterworth

<br>

Utilizando os parâmetros: ![d0](https://latex.codecogs.com/gif.latex?D_%7B0%7D) e ![n](https://latex.codecogs.com/gif.latex?n)	

temos:

![d](https://latex.codecogs.com/gif.latex?D%28u%2Cv%29%3D%20%5Csqrt%7Bu%5E%7B2%7D&plus;v%5E%7B2%7D%7D)

* Passa-baixa
 
![passaBaixa](https://latex.codecogs.com/gif.latex?H%28u%2Cv%29%3D%5Cfrac%20%7B1%7D%7B1&plus;%28%5Cfrac%7BD%28u%2Cv%29%7D%7BD_%7B0%7D%7D%29%5E%7B2n%7D%7D)

<br>

* Passa-alta

![passaAlta](https://latex.codecogs.com/gif.latex?H%28u%2Cv%29%3D%5Cfrac%20%7B1%7D%7B1&plus;%28%5Cfrac%7BD_%7B0%7D%7D%7BD%28u%2Cv%29%7D%29%5E%7B2n%7D%7D) 
