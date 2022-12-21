print("ATENÇÃO:Todas as opções devem ser escritas com letra minúscula e sem acentuação!")

print ("História: Você é um jovem aventureiro e deseja explorar antigas ruinas ao norte da vila em que você mora. Deseja mesmo fazer isso? Sim ou nao?")

#Escolher se quer continuar a jornada ou não
do = input("")

if do == "sim":
    print("Você seguiu adiante na sua jornada e chegou as ruínas!")
    print("Qual será o seu proximo passo? Esquerda ou direita?")
elif do == "nao":
    print("Você resolveu ficar em casa. Obrigado por me fazer perder tempo narrando essa @#$%&!!!\n")
    print("GAME OVER.")

#Jogador escolhe ir pela direita.
do = input("")
if do == "direita":
    print("Você decidiu ir pela direita e, ao chegar no corredor, ouviu um barulho estranho vindo de um baú abandondo. Deseja investigar? Sim ou nao?")
    
#Jogador decide investigar.
do = input("")
if do == "sim":
    print("Você decidiu investigar o baú e é subitamente atacado por um monstro! Qual é a sua ação? Lutar ou fugir?")
#Jogador decide não investigar.
elif do == "nao":
    print("Você optou por não investigar e resolveu voltar para casa! Tudo isso te deixou muito assustado! Cagão...\n")
    print("GAME OVER.")
    
#Batalha no corredor da direita (Investigou o baú).
do = input("")
if do == "lutar":
    print("Você lutou bravamente e venceu o monstro! Parace que ele deixou cair uma espada! Deseja levá-la? Sim ou não?")
#Jogador decide fugir(Final Piada da vila).
elif do == "fugir":
    print("Você conseguiu fugir, mas logo todos souberam o quão medroso você é e logo você se tornou o motivo de piada da vila...\n")
    print("Fim da aventura! Obrigado por jogar!")
    
#Jogador pega a espada.
do = input("")
if do == "sim":
    print("Você decidiu pegar a espada e logo viu que ela lhe seria muito útil nas próximas aventuras!")
    print("Logo adiante, existe uma enorme porta. Você consegue sentir uma estranha presença vindo do outro lado...")
    print("Chegou a hora da sua última decisão: Vai seguir adiante? Ou vai voltar para casa levando esta magnífica espada com você? Adiante ou casa?")

#Jogador opta por seguir adiante
do = input("")
if do == "adiante":
    print("Você escolheu ir adiante e atravessou a porta.")
    print("Ao entrar no salão, você consegue ver aquele que um dia foi o antigo dono destas ruínas. Agora uma mera sombra do homem que ele já foi...")
    print("Ele lhe oferece poder e muito mais caso resolva entregar a espada para ele.")
    print("Entregar a espada? Sim ou não?")
#Jogador não entrega a espada.
do = input("")
if do == "nao":
    print("É claro que é uma armadilha e ao invés de lhe entregar a espada, você o atinge encheio no peito acabando com a criatura!")
    print("Satisfeito com a aventura e sabendo que nenhum monstro pertubaria as ruínas você resolve voltar para casa!")
    print("Fim da aventura! Obrigado por jogar!\n")
    print("GAME OVER.")
#Jogador entrega a espada (Final ruim).
elif do == "sim":
    print("Você resolveu entregar a espada, mas quando se deu conta já era tarde demais!")
    print("Seu corpo logo se transformou em uma terrível criatura, se tornando assim um lacaio do vilão!")
    print("GAME OVER.")
    
#Jogador decide ir para casa.(Final meia boca).
do = input("")
if do == "casa":
    print("Você está satisfeito com a sua aventura e decidiu voltar para sua casa")
    print("Ao chegar, contou a todos a sua aventura e resolveu vender a espada por um bom preço, o que lhe permitiu comprar o tão sonhado MccGuffin!")
    print("Fim do jogo! Obrigado por jogar!!\n")
    print("GAME OVER.")
    
#Jogador escolhe ir pela esquerda.
do = input("")
if do == "esquerda":
    print("Voce encontrou um mostro e iniciou uma batalha feroz contra ele! O que vai escolher? Lutar ou fugir?")

#Batalha com dois finais possíveis (Esquerda).
do = input("")
if do == "lutar":
    print("Você derrotou o monstro! Ele deixou cair um item! Deseja pega-lo? Sim ou não?")
elif do == "fugir":
    print("Infelizmente você não consegui escapar do monstro!\n")
    print("GAME OVER.")
    
#Caso o jogador pegue o item.
do = input("")
if do == "sim":
    print("Você decidiu pegar o item, porém, não sabia que era amaldiçoado e acabaria por fim se tornando o monstro que você acabou de derrotar!\n")
    print("GAME OVER.")
#Jogador não pegou o item (Final meia boca).  
elif do == "nao":
    print("Você decidiu não pegar o item e resolveu voltar para casa. Você não nasceu para este tipo de coisa...")
    print("Fim da aventura! Obrigado por jogar!")