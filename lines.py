from Tkinter import *

cwidth=500
cheight=500
loops=10


def square(cv,x1,y1,x2,y2):
    cv.create_line(10,10,100,100)
    print(x1)

if __name__ == '__main__':
    root=Tk()
    c= Canvas(root,width=cwidth,height=cheight,bg='white')
    img=PhotoImage(width=cwidth,height=cheight)
    c.create_image((0,0), image=img,state= "normal", anchor=NW)
    square(c, -2,2, 2,-2)
    c.pack()
    root.mainloop()
