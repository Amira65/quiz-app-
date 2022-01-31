from tkinter import *
from tkinter import messagebox as mb
import json
from turtle import bgpic
class Quiz:

	def __init__(self):
		self.q_no=0
		self.display_title()
		self.display_question()
		self.opt_selected=IntVar()
		self.opts=self.radio_buttons()
		self.display_options()
		self.buttons()
		self.data_size=len(question)
		self.correct=0

	def display_result(self):
		
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	def check_ans(self, q_no):
	
		if self.opt_selected.get() == answer[q_no]:
			
			return True

	
	def next_btn(self):
		
		if self.check_ans(self.q_no):
			
			self.correct += 1
		
		self.q_no += 1
		
		if self.q_no==self.data_size:
			self.display_result()
		
			gui.destroy()
		else:
			self.display_question()
			self.display_options()



	def buttons(self):
		
		next_button = Button(gui, text="Next",command=self.next_btn,
		width=10,bg="black",fg="white",font=("sans-serif",16,"bold"))
		next_button.place(x=350,y=380)
		
		
	def display_options(self):
		val=0
		self.opt_selected.set(0)
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1


	# This method shows the current Question on the screen
	def display_question(self):
		
		# setting the Question properties
		q_no = Label(gui, text=question[self.q_no], width=60,fg="white" ,bg="black",
		font=( 'sans-serif' ,16, 'bold' ), anchor= 'w' )
	
		q_no.place(x=70, y=100)
	 
	# This method is used to Display Title
	def display_title(self):
	
		title = Label(gui, text="Choose your answer",bg="black",
		width=50, fg="white", font=("ariel", 20, "bold"))
		
		# place of the title
		title.place(x=-30, y=10)
	
	
	def radio_buttons(self):
		
		q_list = []
		
		y_pos = 150
		
		
		while len(q_list) < 4:
			
			radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,background=None,fg="white",
			bg="black",value = len(q_list)+1,font = ("sans-serif",15))
			
			q_list.append(radio_btn)
			radio_btn.place(x = 100, y = y_pos)
			
			y_pos += 40
		
		return q_list


gui = Tk()
gui.geometry("800x450")
gui.title("BIG UP GYM")



# Add image file
bg = PhotoImage( file = "h.png")
label1 = Label( gui, image = bg)
label1.place(x = 0,y = 0)

with open('data.json') as f:
	data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])

quiz = Quiz()
gui.mainloop()