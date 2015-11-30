from Tkinter import Tk, Frame, BOTH

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent,background="lightgrey")
        
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        self.parent.title("TEST")
        self.pack(fill=BOTH, expand=1)
        
        
def main():
    
    root = Tk()
    root.geometry("500x500+300+300")
    
    app = Example(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()