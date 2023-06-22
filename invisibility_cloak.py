import cv2
import time
import numpy as np

#Detecção de Cor e Segmentação

#*Para salvar o resultado em um arquivo chamado output.avi
#O FourCC é um código usado para especificar o codec de vídeo. Os codecs são usados para compactar dados.
fourcc = cv2.VideoWriter_fourcc(*'XVID')

output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

#Iniciando a webcam
cap = cv2.VideoCapture(0)

#Permitindo que a webcam inicie fazendo o código aguardar 2 segundos
time.sleep(2)
bg = 0

#Capturando o plano de fundo durante 60 quadros
for i in range(60):
    ret, bg = cap.read()
#Invertendo o plano de fundo
bg = np.flip(bg, axis=1)

#Lendo o quadro capturado até que a câmera esteja aberta
#: O método cap.read() obtém o próximo quadro da câmera. Ele retorna 2 valores:
#1. ret - retorna verdadeiro se o quadro estiver disponível. Caso contrário, será falso.
#2. img - contém um array de imagens.
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    #Invertendo a imagem por motivo de consistência
    img = np.flip(img, axis=1)

    #Convertendo a cor de RGB para HSV 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ##*oBS.: VERMELHO ESTÁ ENTRE 0-10 E 170-180

    #Gerando máscara para detectar a cor vermelha (os valores podem ser alterados)
    lower_red = np.array([0, 120, 50])
#* variável chamada lower_red (vermelho inferior) e criamos um array usando o método np.array() que contém [0 , 120, 50]. Os 3 valores no arrayrepresentam matiz,
    upper_red = np.array([10, 255,255])
    mask_1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask_2 = cv2.inRange(hsv, lower_red, upper_red)
    
    ##MENSACLANDO OS TONS DA MÁSCARA
    mask_1 = mask_1 + mask_2
  #* escrever resultado da máscara:
    cv2.imshow("mask_1", mask_1)

   # * Segementando
   #Vamos fazer uma transformação morfológica na imagem. Morfologia significa relativo à forma. As transformações morfológicas são operações
   #Esta linha de código removerá o ruído da nossa imagem.
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    #Abrindo e expandindo a imagem onde há a máscara 1 (cor)
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
  
   # máscara invertida para segmentar a cor vermelha do quadro.
    mask_2 = cv2.bitwise_not(mask_1)

    #Selecionando apenas a parte que não possui máscara 1 e salvando-a na máscara 2
    
   

    #Mantendo apenas a parte das imagens sem a cor vermelha
    #(ou qualquer outra cor que você escolher)
   

    #Mantendo apenas a parte das imagens com a cor vermelha
   

    # 1. Gerando o resultado final mesclando res_1 e res_2 #continuar....
    final_output = img
    output_file.write(img)
    #Displaying the output to the user
    # exibe o resultado na tela usando o método cv2.imshow().
    cv2.imshow("magica", final_output)
    cv2.waitKey(1)
    
    #Exibindo o resultado para o usuário
    
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()

#iberamos a câmera. Usamos cv2.destroyAllWindows() para fechar todas asjanelas abertas pelo cv2.

