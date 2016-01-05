# -*- coding:utf-8 -*- 
import tkinter

class Application(Frame):
	"""docstring for Frame"""
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLable = Lable(self,text='hello,python')
		self.helloLable.pack()
		self.quitButton = Button(self,text='退出',command=self.quit)
		self.quitButton.pack()

app = Application()
app.master.title('Hello,python')
app.mainloop()
		
		