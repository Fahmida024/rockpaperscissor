from tkinter import*
import tkinter.font as font
import random

game_window=Tk()
game_window.title('Rock paper scissors')

titlelable=Label(game_window, text='Rock Paper Scissors', font='Times 15')
titlelable.pack()
winnermessage=Label(game_window, text='Lets start the game', font='Times 10')
winnermessage.pack()

input_frame=Frame(game_window)
input_frame.pack()
optionlable=Label(input_frame, text='Youre options;',fg='LavenderBlush4', font='Times 10')
rockbutton=Button(input_frame, text=' Rock', width=15, bg='MediumPurple1', font='Times 10')
paperbutton=Button(input_frame, text='Paper', width=15, bg='LightSkyBlue1', font='Times 10')
scissorbutton=Button(input_frame, text='Scissor', width=15, bg='plum2', font='Times 10')
scorelabel=Label(input_frame, text='Score;',fg='LavenderBlush4',font='Times 10' )
userselect=Label(input_frame, text='You selected;', font='Times 10')
computerselect=Label(input_frame, text='Computer selected;', font='Times 10')
playerscore=Label(input_frame, text='Youre score is;', font='Times 10')
computerscore=Label(input_frame, text='Computer score is;', font='Times 10')



optionlable.grid(row=0, column=0)
rockbutton.grid(row=1, column=1, padx=15, pady=5)
paperbutton.grid(row=1, column=2, padx=15, pady=5)
scissorbutton.grid(row=1, column=3, padx=15, pady=5)
scorelabel.grid(row=2, column=0)
userselect.grid(row=3, column=1)
computerselect.grid(row=4, column=1)
playerscore.grid(row=3, column=2)
computerscore.grid(row=4, column=2)








game_window.mainloop()






