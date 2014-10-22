#!/usr/bin/ python2      
from Tkinter import *  
import math
import random

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master) 
		self.grid(sticky=N+S+E+W)
		self.createWidgets()
	def createWidgets(self):
		top=self.winfo_toplevel()
		top.rowconfigure(0, weight=1)
		top.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		Test = Button(self,text='Test',command = self.run)
		Test.grid(row=0, column=0,sticky=N+S)
		self.result = Text(self,width=80,height=5,wrap=WORD)
		self.result.grid(row=1, column=0,sticky=N+S+E+W)
		self.quit = Button(self, text='Quit', command=self.quit)
		self.quit.grid(row=2, column=0,sticky=N+S)
	def run(self):
		curtains = ['A','B','C']
		NumOfWinsIfKeep = 0
		NumOfWinsIfChange = 0
		for x in range (0,10000):
			Ferrari = random.choice(curtains)
			PlayerChoice = random.choice(curtains)
			curtains.remove(PlayerChoice)
			Discard = random.choice(curtains)
			while Discard == Ferrari:
				Discard = random.choice(curtains)
			curtains.remove(Discard)
			RemainingCurtain = curtains[0]
			if RemainingCurtain == Ferrari:
				NumOfWinsIfChange += 1
			else :
				NumOfWinsIfKeep += 1
			curtains = ['A','B','C']
		self.result.delete(0.0,END)
		self.result.insert(0.0,'In 10000 Tests: \nIf player keeps his choice, he wins '+str(NumOfWinsIfKeep) + ' times('+str(float(NumOfWinsIfKeep)/float(100))+'%)\nIf he changes his option he wins: '+ str(NumOfWinsIfChange)+' times('+str(float(NumOfWinsIfChange)/float(100))+'%)')
app = Application()
app.master.title('Monty Hall problem test')
app.mainloop() 
