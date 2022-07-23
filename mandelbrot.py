try:  
    # Python v2
   from Tkinter import *
except ImportError:
    #Python v3
    from tkinter import *

cwidth=250 #width of the canvas
cheight=250 #height of the canvas
loops=5
w=256

def hex_list(k):
    d=[]
    for l in range(k+1):
        if k<=15:
            d.append(hex(0)[2:]+hex(k)[2:])
        else:
            d.append(hex(k)[2:])
    return d[k]


def mandel(cv,x1,y1,x2,y2):
    dx=float(abs(x2-x1))/cwidth  #calculate the x increment of each pixel
    dy=float(abs(y2-y1))/cheight #calculate the y increment of each pixel

    y=y1
    for j in range(0,cheight):
        x=x1
        for i in range(0,cwidth):
            x=x+dx
            c=complex(x,y)   #let each pixel on the screen represent a complex number
            z=0.0
            print(c)
            for k in range(0,loops):
              z=z**2 +c
              if abs(z)>2:
                 break
            if k==0:
                  cv.create_line(i,j,i,j+1,fill="#ffffff")
            if 0<k<=loops:
                c=int(w-k*w/loops)
                str1="#"
                str2=hex_list(c)+hex_list(c)+hex_list(c)
                newstr=str1+str2
                cv.create_line(i,j,i,j+1,fill=newstr)
            
                
            
           
            

            
        y=y - dy
        cv.update()

if __name__ == '__main__':
    root=Tk()
    c= Canvas(root,width=cwidth,height=cheight,bg='white')
    img=PhotoImage(mandel(c, -2,2, 2,-2))
    c.create_image(0,0, image=img)
    c.pack()
    root.mainloop()
