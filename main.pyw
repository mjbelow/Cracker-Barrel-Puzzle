import tkinter, math, copy, sys


def update():
    lbl.configure(text=str(p[0].get())+", "+str(p[1].get())+", "+str(p[2].get())+", "+str(p[3].get())+", "+str(p[4].get())+", "+str(p[5].get())+", "+str(p[6].get())+", "+str(p[7].get())+", "+str(p[8].get())+", "+str(p[9].get())+", "+str(p[10].get())+", "+str(p[11].get())+", "+str(p[12].get())+", "+str(p[13].get())+", "+str(p[14].get()))

def start():
    global found
    found=False
    pieces=[0]*15
    for i in range(15):
        pieces[i]=p[i].get()
    move(pieces, [])

found=False

def move(pieces, move_history):
    global found
    moved=False
    count=0
    for i in range(15):
        if(found):
            return
        if(pieces[i]==1):
            for j in range(len(valid_moves[i])):
                piece_jump=pieces[valid_moves[i][j][0]]
                piece_dest=pieces[valid_moves[i][j][1]]
                if(piece_jump==1 and piece_dest==0):
                    moved=True
                    pieces_adjust=copy.copy(pieces)

                    # make the move
                    pieces_adjust[i]=0
                    pieces_adjust[valid_moves[i][j][0]]=0
                    pieces_adjust[valid_moves[i][j][1]]=1

                    # record the move
                    my_move=[i]
                    my_move.append(valid_moves[i][j])
                    my_move_history=copy.copy(move_history)
                    my_move_history.append(my_move)
                    
                    # find more available moves
                    move(pieces_adjust,my_move_history)
    if(not moved):
        for i in range(15):
            if(pieces[i]==1):
                count+=1
        # print(move_history)
        # print("remaining pieces",count)
        if(count==1):
            print(move_history)
            print("remaining pieces",count)
            found=True
        move_history=[]


valid_moves=[
    # 0
    [[1,3],[2,5]],
    # 1
    [[3,6],[4,8]],
    # 2
    [[4,7],[5,9]],
    # 3
    [[1,0],[4,5],[7,12],[6,10]],
    # 4
    [[7,11],[8,13]],
    # 5
    [[4,3],[8,12],[2,0],[9,14]],
    # 6
    [[3,1],[7,8]],
    # 7
    [[4,2],[8,9]],
    # 8
    [[7,6],[4,1]],
    # 9
    [[5,2],[8,7]],
    # 10
    [[6,3],[11,12]],
    # 11
    [[7,4],[12,13]],
    # 12
    [[11,10],[7,3],[8,5],[13,14]],
    # 13
    [[12,11],[8,4]],
    # 14
    [[13,12],[9,5]]
]

window = tkinter.Tk()
window.geometry("550x550")
window.title("Cracker Barrel Puzzle")


p=[0]*15;

for i in range(15):
    p[i]=tkinter.IntVar(value=1)

top=50
vert_dist=horz_dist=100

tkinter.Checkbutton(window, relief="sunken", variable=p[0], command=update, text=0).place(relx=0.5, rely=0, x=-25, y=top, height=50, width=50)


tkinter.Checkbutton(window, relief="sunken", variable=p[1], command=update, text=1).place(relx=0.5, rely=0, x=-25-horz_dist/2, y=top+vert_dist, height=50, width=50)
tkinter.Checkbutton(window, relief="sunken", variable=p[2], command=update, text=2).place(relx=0.5, rely=0, x=-25+horz_dist/2, y=top+vert_dist, height=50, width=50)


tkinter.Checkbutton(window, relief="sunken", variable=p[3], command=update, text=3).place(relx=0.5, rely=0, x=-25-horz_dist, y=top+vert_dist*2, height=50, width=50)
tkinter.Checkbutton(window, relief="sunken", variable=p[4], command=update, text=4).place(relx=0.5, rely=0, x=-25, y=top+vert_dist*2, height=50, width=50)
tkinter.Checkbutton(window, relief="sunken", variable=p[5], command=update, text=5).place(relx=0.5, rely=0, x=-25+horz_dist, y=top+vert_dist*2, height=50, width=50)


tkinter.Checkbutton(window, relief="sunken", variable=p[6], command=update, text=6).place(relx=0.5, rely=0, x=-25-horz_dist/2-horz_dist, y=top+vert_dist*3, height=50, width=50)
tkinter.Checkbutton(window, relief="sunken", variable=p[7], command=update, text=7).place(relx=0.5, rely=0, x=-25-horz_dist/2, y=top+vert_dist*3, height=50, width=50)
tkinter.Checkbutton(window, relief="sunken", variable=p[8], command=update, text=8).place(relx=0.5, rely=0, x=-25+horz_dist/2, y=top+vert_dist*3, height=50, width=50)
tkinter.Checkbutton(window, relief="sunken", variable=p[9], command=update, text=9).place(relx=0.5, rely=0, x=-25+horz_dist/2+horz_dist, y=top+vert_dist*3, height=50, width=50)


tkinter.Checkbutton(window, relief="sunken", variable=p[10], command=update, text=10).place(relx=0.5, rely=0, x=-25-horz_dist*2, y=top+vert_dist*4, height=50, width=50)
tkinter.Checkbutton(window, relief="sunken", variable=p[11], command=update, text=11).place(relx=0.5, rely=0, x=-25-horz_dist, y=top+vert_dist*4, height=50, width=50)
tkinter.Checkbutton(window, relief="sunken", variable=p[12], command=update, text=12).place(relx=0.5, rely=0, x=-25, y=top+vert_dist*4, height=50, width=50)
tkinter.Checkbutton(window, relief="sunken", variable=p[13], command=update, text=13).place(relx=0.5, rely=0, x=-25+horz_dist, y=top+vert_dist*4, height=50, width=50)
tkinter.Checkbutton(window, relief="sunken", variable=p[14], command=update, text=14).place(relx=0.5, rely=0, x=-25+horz_dist*2, y=top+vert_dist*4, height=50, width=50)

lbl = tkinter.Label(window,text=str(p[0].get())+", "+str(p[1].get())+", "+str(p[2].get())+", "+str(p[3].get())+", "+str(p[4].get())+", "+str(p[5].get())+", "+str(p[6].get())+", "+str(p[7].get())+", "+str(p[8].get())+", "+str(p[9].get())+", "+str(p[10].get())+", "+str(p[11].get())+", "+str(p[12].get())+", "+str(p[13].get())+", "+str(p[14].get()))
lbl.pack()

# canvas = tkinter.Canvas()
# canvas.create_line(100, 600, 600, 600, 350, 600-math.sqrt(3)*250, 100, 600)
# canvas.pack(fill=tkinter.BOTH, expand=1)

# canvas = tkinter.Canvas()
# canvas.create_line(0, 0, 500, 500, 500, 250)
# canvas.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

tkinter.Button(window, command=start, text="Solve").pack()

window.mainloop()