import functions as func
import cv2 as cv

img = cv.imread("bibble.png")

mensagem = "samalako"
mensagem_codificada = func.gerar_mensagem(mensagem)

img_codificada = func.esconder_msg(img.copy(), mensagem_codificada)

mensagem_decoficada = func.encontrar_msg(img_codificada, len(mensagem_codificada))
print(mensagem_decoficada)