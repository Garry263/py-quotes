import tkMessageBox,time
from Tkinter import *

data = []  #global declaration of list

class App():

    def __init__(self):
        self.root = Tk()
        self.root.overrideredirect(1)
        self.root.attributes("-alpha", 0.5) #sets the transparency
        w = 450 # width for the Tk root
        h = 150 # height for the Tk root
        self.frame = Frame(self.root, width=w, height=h,
                           borderwidth=2, relief=FLAT,bg = 'light sky blue')
        self.frame.pack_propagate(False)
        self.frame.pack()
        self.bQuit = Button(self.frame, text="Quit",
                            command=self.root.destroy) #quit button
        self.bQuit.pack(pady=10)
        self.label = Message(self.frame,text='100 Pushups!',font=(None,15,'italic')
                             ,bg = 'light sky blue',width = 400)
        self.label.pack()
        ws = self.root.winfo_screenwidth() # width of the screen
        hs = self.root.winfo_screenheight() # height of the screen
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, 900, 15)) #setting the window position
       

    def readData(self):
        f = open("data.txt","r") #opens data file that contains our quotes
        for line in f:        #iterating through the lines 
            data.append(line)  #adding those line (quotes) to the list
        f.close()            #closing file after appending is done
     #   for fk in data:         
      #     print(fk)      #For Testing purposes
       # print(len(data))        

    def task(self):  
        if len(data)>0:         #we dont want to display null
            self.label.configure(text=data[0])  #display 1st item from the list
            data.pop(0)   #remove the 1st element of the list so the next element becomes first element
           # print("updated " )  
            self.root.after(20000,self.task)  # reschedule event in 2 seconds
            self.label.update() 
        else:
            #print("Data Ended!")
            self.label.configure(text='Data Ended!')

app = App()
App.readData(app)
app.root.after(1000, App.task(app))
app.root.mainloop()



