print("Olá, você está para jogar um pequeno jogo de escolhas!")
print("Todas as opções devem ser escritas em maiúsculas ok?")

print("A história:\n")

print("Você está prese em um deserto árido perto de um antigo helicóptero\n")
print("O que você vai fazer? Vai investigar os destroços dele ou vai esperar a ajuda chegar?")
print("Responda: SIM para esperar ou NÃO para investigar.")

do = input("")

if do == "SIM":
    print("Pelo visto você decidiu esperar pela ajuda...\n")
    print("Infelizmente ela nunca veio, e você acabou morrendo!\n")
    print("GAME OVER")
    
if do == "NÃO":
    print("Você decidiu investigar o helicóptero e descobriu que o rádio ainda funciona!\n")
    print("Você consegui contatar a base e seu resgate veio imediatamente!")
    print("Parabéns você sobreviveu!!!\n")
    print("GAME OVER")