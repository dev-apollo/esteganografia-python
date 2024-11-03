import numpy as np

def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]

def gerar_mensagem(mensagem):
    lista = []
    for m in mensagem:
        val = ord(m)
        bits = bitfield(val)
        if len(bits) < 8:
            bits = [0] * (8 - len(bits)) + bits
        lista.extend(bits)
    return np.array(lista)

def converter_mensagem(saida):
    bits = np.array(saida)
    mensagem_out = ''
    bits = bits.reshape((len(saida) // 8, 8))
    for b in bits:
        val = sum(b[i] * (2 ** (7 - i)) for i in range(8))
        mensagem_out += chr(val)
    return mensagem_out

def esconder_msg(img, listaBitsMsg):
    cont = 0
    for altura in range(img.shape[0]):
        for largura in range(img.shape[1]):
            if cont < len(listaBitsMsg):
                img[altura, largura, 2] = (img[altura, largura, 2] & 0xFE) | listaBitsMsg[cont]
                cont += 1
            else:
                break
    return img

def encontrar_msg(img, bits_msg_org):
    bits = []
    for altura in range(img.shape[0]):
        for largura in range(img.shape[1]):
            if len(bits) < bits_msg_org:
                bits.append(img[altura, largura, 2] & 1)
            else:
                break
    return converter_mensagem(bits)