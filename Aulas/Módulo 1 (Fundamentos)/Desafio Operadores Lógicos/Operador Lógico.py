trabalho_terca = True
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta #XOR
mais_saudavel = not sorvete

#print("tv50={} tv32={} Sorvete={} Saudavel={}".format(tv_50, tv_32, sorvete, mais_saudavel)) Método "antigo"

#Método mais dinâmico para formatar!
print(f'tv50{tv_50} tv32{tv_32} Sorvete{sorvete} Saudavel{mais_saudavel}')
