Nosso algoritmo terá os seguintes passos:
1. Capture e armazene o quadro de fundo. Isso será feito durante alguns segundos.
2. Detecte o tecido vermelho usando algoritmos de Detecção de Cor e Segmentação.
3. Segmente o tecido vermelho gerando umamáscara. [usada no código]
4. Gere o resultado final aumentado para criar um efeito mágico. [vídeo.mp4]

# sobre o Flip:
O método flip() inverte o array ao longo do eixo fornecido. Aqui, ele inverte a imagem para obtermos a imagem adequada em vez da imagem espelhada dela

# Sobre HSV
1. Matiz (Hue): este canal codifica as informações das cores. A matiz (ou tonalidade) é medida em graus, de 0 a 360 ao longo da circunferência da base do cilindro. A cor vermelha fica entre 0-10 graus e 170-180 graus.
2. Saturação: isso codifica a intensidade da cor. Mais saturação significa mais brilho na sua cor. O raio do cilindro representa a saturação.
3. Valor de brilho: isso codifica o brilho da cor, ou seja, os componentes de sombreamento e brilho de uma imagem. A altura representa o valor de brilho.


# parâmetros  **do mask_1 = cv2.inRange** são:
● array_origem - é o array que temos que comparar
para verificar se está em um determinado intervalo.
● limite_superior_array - é o array que consiste no
limite superior.
● limite_inferior_array - é o array que consiste no
limite inferior.

resultado:
mask_1 = cv2.inRange(hsv, lower_red, upper_red)
A mask1 detecta a cor vermelha na faixa de matiz 0 a 10.

# Sobre: método morphologyEx() para nossa transformação morfológica.
Este método espera 3 argumentos:
● O primeiro argumento é a imagem à qual
queremos aplicar a operação morfológica.
Neste caso, a imagem é armazenada na
variável mask_1.
● O segundo argumento é o tipo real de
operação morfológica. Usaremos
cv2.MORPH_OPEN. É útil para remover
ruído (variação aleatória de brilho) da
imagem.

O último argumento obrigatório é o elemento
kernel/estruturante que estamos usando.
Vamos passá-lo como:

**np.ones((3, 3), np.uint8)**
● Aqui, np.ones((3,3), np.uint8) retorna um
array de determinada forma e tipo,
preenchido com números 1. Neste caso, ele
retornará um array de formato 3x3 que
consistirá em números 1.

A função *bitwise_not do OpenCV.* A função bitwise_not inverte os valores dos pixels. Todos os pixels maiores que zero são definidos com zero e todos os pixels iguais a zero são definidos com 255.
