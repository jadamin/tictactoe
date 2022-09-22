
from aidecode import draw_board, check_turn , win1
import os 
spots  = {1 :'1', 2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
draw_board(spots)

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:

    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    if prev_turn == turn:
        print("Desole, Entrez un nombre valide entre 1 et 9")
    prev_turn = turn
    print('Joueur' + str ((turn %2 )+1 )+ "tour: veuillez choisir un nombre ou Q pour Quitter")
    choice = input()
    if choice == 'q' :
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {"X","O"}:
            turn +=1
            spots[int(choice)] = check_turn(turn)
    if win1(spots): playing , complete = False,True
    if turn > 8: playing = False

os.system('cls' if os.name == 'nt' else 'clear') 
draw_board(spots)   

if complete:
    if check_turn(turn) == 'x': print("Joueur 1 gagne : Felicitations")
    else: print("Joueur 2 gagne : Felicitations")
else: 
    print("Pas de gagnant")
    print("Merci et a bientot")
    