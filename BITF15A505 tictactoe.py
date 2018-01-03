#Python: Tic Tac Toe Game


box=['0','1','2','3','4','5','6','7','8']
def show():
    print (box[0],'|',box[1],'|',box[2])
    print('----------')
    print (box[3],'|',box[4],'|',box[5])
    print('----------')
    print (box[6],'|',box[7],'|',box[8])



def checkAll():
    if box[0] == 'X' and box[1] == 'X' and box[2] == 'X':
        return 1
    elif box[0] == 'O' and box[1] == 'O' and box[2] == 'O':
            return 2
    elif box[3] == 'X' and box[4] == 'X' and box[5] == 'X':
            return 1
    elif box[3] == 'O' and box[4] == 'O' and box[5] == 'O':
            return 2
    elif box[6] == 'X' and box[7] == 'X' and box[8] == 'X':
            return 1
    elif box[6] == 'O' and box[7] == 'O' and box[8] == 'O':
            return 2
    elif box[0] == 'X' and box[3] == 'X' and box[6] == 'X':
            return 1
    elif box[0] == 'O' and box[3] == 'O' and box[6] == 'O':
            return 2
    elif box[1] == 'X' and box[4] == 'X' and box[7] == 'X':
            return 1
    elif box[1] == 'O' and box[4] == 'O' and box[7] == 'O':
            return 2
    elif box[2] == 'X' and box[5] == 'X' and box[8] == 'X':
            return 1
    elif box[2] == 'O' and box[5] == 'O' and box[8] == 'O':
            return 2
    elif box[0] == 'X' and box[4] == 'X' and box[8] == 'X':
            return 1
    elif box[0] == 'O' and box[4] == 'O' and box[8] == 'O':
            return 2
    elif box[2] == 'X' and box[4] == 'X' and box[6] == 'X':
            return 1
    elif box[2] == 'O' and box[4] == 'O' and box[6] == 'O':
            return 2


        

def main():
    player=1
    start=1
    while start==1:
        board=int(input("\nEnter any box: "))
        if player == 1:
            if board>=0 and board<=8:
                box[board]='X'
                player = 2
                show()
            if checkAll()==1:
                print ("Winner is Player1")
                
            
                
        elif player== 2:
            if board>=0 and board<=8:
                box[board]='O'
                player = 1
                show()
            if checkAll() == 2:
                print ("Winner is Player2")
       
show()
main()


