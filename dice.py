from random import randint

default_dice = randint(1, 6)

while True:

    roll = input('Deseja rolar o dado? ')

    if roll.isalpha() != True:
        print("Digite apenas 'sim' ou 'não'.")
        continue
 
    elif roll[0].lower() == 'n':
        print('Ok, o programa será fechado.')
        break
    
    elif roll[0].lower() == 's':

        while True:
            default_roll = input('Deseja rolar o dado default (6)? ')

            if default_roll.isalpha() != True:
                print("Digite apenas 'sim' ou 'não'.")
                continue

            elif default_roll[0].lower() == 's':
                print(f'O resultado foi {default_dice}.')
                break
            
            elif default_roll[0].lower() == 'n':

                while True:

                    new_dice = input('Você deseja rolar um dado de quantos lados? ')

                    if new_dice.isnumeric() == True:
                        print(f'O resultado foi {randint(1, int(new_dice))}.')
                        break        

                    else:
                        print('Digite um número.')
                        continue

            break
