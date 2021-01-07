import random as rand

def updateLifeBars(Life,LifeBar,LifeBarLentgh,id):
    if id == 1:
        segmentedLife=10
    else:
        segmentedLife=15
    for i in  range(LifeBarLentgh):
        if Life>=LifeBarLentgh:
            Life-=segmentedLife
            LifeBar[i] = '-'
        else:
            LifeBar[i] = ' '
    if id==1:
        print("\nVIDA: ",LifeBar)
    else:
        print("\nVIDA DO MONSTRO: ",LifeBar)

def updateCritRate(critRate):
    critRate = rand.randint(0,100)
    return critRate

playerLife = 100
playerLifeBar = ['-','-','-','-','-','-','-','-','-','-']
monsterLife = 150
monsterLifeBar = ['-','-','-','-','-','-','-','-','-','-']
LifeBarLentgh=10
rounds=0

print("Objetivo: derrotar o monstro!")

while playerLife > 0 and monsterLife > 0:
    playerStrength = rand.randint(1,10)
    playerDefense = 0
    monsterStrength = rand.randint(1,15)
    monsterChoice = rand.randint(0,100)
    critic = False
    critRate = rand.randint(0,100)
    critDMG = 50  
    evasion= 0
    print(f"\n=== Round  {rounds}===")
    updateLifeBars(playerLife,playerLifeBar,LifeBarLentgh,1)
    print("Dano atual: ",playerStrength)
    updateLifeBars(monsterLife,monsterLifeBar,LifeBarLentgh,2)

    print(" _____________________________")
    print("|   ____             <------> |")
    print("|  / ' '\\            | <>  |  |")
    print("|  |    |             \\    /  |")
    print("|_____________________________|")

    print("=== Ações ===")
    print("1 = Atacar\n2 = Defender\n3 = Desviar")
    resp = int(input("O que você deseja fazer?"))
    
    if resp == 1:
        if critRate<=50:
            playerStrength=(playerStrength*100)/critDMG
            monsterLife-=playerStrength
            print("Dano crítico ao oponente: ",playerStrength)
        else:
            monsterLife-=playerStrength
            print("Dano ao oponente: ",playerStrength)
    elif resp == 2:
        monsterStrength/=2
        print("Defesa aumentada!")
    elif resp == 3:
        evasion= rand.randint(0,101)
        print("Evasão aumentada!")

    critRate = updateCritRate(critRate)

    if monsterChoice>70:
        if evasion<=50:
            if critRate<=20:
                monsterStrength=(monsterStrength*100)/critDMG
                playerLife-=monsterStrength
                print("Dano crítico á você: ",monsterStrength)
            else:
                playerLife-=monsterStrength
                print("Dano á você: ",monsterStrength)
        else:
            print("Você desviou do ataque!")
    elif 70>=monsterChoice:
        print("O monstro não fez nada!")

    rounds+=1

if monsterLife<=0:
    print("Parabèns, você venceu!")
elif playerLife <= 0:
    print("Você perdeu!")
