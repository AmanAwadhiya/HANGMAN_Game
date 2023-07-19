# HANGMAN GAME
import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True

while run:
    root = Tk()
    root.geometry('1400x800')
    root.title('HANGMAN GAME')
    root.config(bg = '#E7FFFF')
    count = 0
    win_count = 0

    title=PhotoImage(file="Hang_Man\HangMan\hangman.png")
    e2 = Label(root,bd= 0,bg="#E7FFFF",image=title)
    e2.place(x=20,y=20)

    # choosing word
    index = random.randint(0,840)
    file = open('Hang_Man\Program\words.txt','r')
    l = file.readlines()
    selected_word = l[index].strip('\n')

    # creation of word dashes variables
    x = 250
    for i in range(0,len(selected_word)):
        x += 50
        exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,400))
        
    #letters icon
    a1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in a1:
        exec('{}=PhotoImage(file="HangMan\keyLetter\{}.png")'.format(letter,letter))
        
    # hangman images
    h123 = ['h1','h2','h3','h4','h5','h6','h7']
    for hangman in h123:
        exec('{}=PhotoImage(file="Hang_Man\HangMan\{}.png")'.format(hangman,hangman))
   
    # Display Score
    s2 = 'SCORE: '+str(score)
    s1 = Label(root,text = s2,bg = "#E7FFFF",font = ("arial",25))
    s1.place(x = 50,y = 300)

    #letters placement
    button = [['b1','a',50,550],['b2','b',150,550],['b3','c',250,550],['b4','d',350,550],['b5','e',450,550],['b6','f',550,550],['b7','g',650,550],['b8','h',750,550],['b9','i',850,550],['b10','j',950,550],['b11','k',1050,550],['b12','l',1150,550],['b13','m',1250,550],['b14','n',50,645],['b15','o',150,645],['b16','p',250,645],['b17','q',350,645],['b18','r',450,645],['b19','s',550,645],['b20','t',650,645],['b21','u',750,645],['b22','v',850,645],['b23','w',950,645],['b24','x',1050,645],['b25','y',1150,645],['b26','z',1250,645]]
    
    for qq in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",image={})'.format(qq[0],qq[1],qq[0],qq[1]))
        exec('{}.place(x={},y={})'.format(qq[0],qq[2],qq[3]))
        
    #hangman placement
    han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
    for pp in han:
        exec('{}=Label(root,bg="#E7FFFF",image={})'.format(pp[0],pp[1]))

    # place of first hangman image
    c1.place(x = 1000,y = 250)
    
    # exit button
    def close():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()
            
    exit = PhotoImage(file = 'HangMan\KeyLetter\exit.png')
    ex = Button(root,bd = 0,command = close,bg="#E7FFFF",activebackground = "#E7FFFF",image = exit)
    ex.place(x=1250,y=20)

    # button press check function
    def check(letter,button):
        global count,win_count,run,score
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))
            if win_count == len(selected_word):
                score += 1
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()   
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count+1,1000,250))
            if count == 6:
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()         
    root.mainloop()