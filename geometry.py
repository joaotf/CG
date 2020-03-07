import turtle
import tkinter as tk

class Menu:
    def __init__(self,parent):
        self.menu = tk.Button(parent,text="Menu",width=10,height=2);
        self.menu.place(x=100,y=10)
        self.func_one = tk.Button(parent,command=self.Circle,text="Desenhar CÍRCULO",width=14,height=1);
        self.func_one.place(x=50,y=100)
        self.func_two = tk.Button(parent,command=self.Triangle,text="Desenhar TRIÂNGULO",width=16,height=1);
        self.func_two.place(x=50,y=140)
    def Circle(self):
        turtle.circle(50)
    def Triangle(self):
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Computação Gráfica")
    root.geometry("300x300")
    menu = Menu(root)
    root.mainloop()
    