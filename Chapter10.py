
def hangman(word):
    wrong= 0
    stages=['','_____        ',
              '|    |       ',
              '|    o       ',
              '|   /|\      ',
              '|    |       ',
              '|   / \      ',
              '|            ']
    rletters = list(word.upper())
    board = ["__"] * len(word)
    win = False
    print('\n')
    print('Welcome to Hangman!')
    print('\n')
    print((' '.join(board)))
    while wrong < len(stages)-2:
        print("\n")
        msg="Guess a letter: "
        char=input(msg)
        char=char.upper()
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong+=1
        print('\n')
        print((' '.join(board)))
        e=wrong+1
        print('\n'.join(stages[0:e]))
        if "__" not in board:
            print('You win!')
            print(' '.join(board))
            win=True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('You lose! It was "{}".'.format(word))

hangman('kyon')
