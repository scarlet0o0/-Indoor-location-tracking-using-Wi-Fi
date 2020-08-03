import time
from tkinter import*

#현실크기
real_width=159550
real_height=44200

#사진크기
picture_width=798
picture_height=231

#원크기
x1=0
y1=0
x2=10
y2=10

#사진 속 내 위치
my_picture_width2=0
my_picture_height2=0

#현실 좌표를 받으면 사진 속 이동해야할 거리를 리턴하는 함수
def location(x,y):
    global my_picture_width2
    global my_picture_height2
    
    my_real_width=x
    my_real_height=y

    #현실좌표를 사진속 좌표로 바꾸기
    my_picture_width=my_real_width*picture_width//real_width
    my_picture_height=my_real_height*picture_height//real_height

    #이동거리 계산
    move_width=my_picture_width-my_picture_width2
    move_height=my_picture_height-my_picture_height2

    #사진 속 내 위치 수정
    my_picture_width2=my_picture_width
    my_picture_height2=my_picture_height

    return move_width,move_height


def main():
    #gul 소환
    root = Tk()
    root.title("gul")
    canvas = Canvas(root,width=picture_width,height=picture_height)
    img = PhotoImage(file='EngrBldg1stFloor2.png')
    canvas.create_image(0,0,anchor=NW,image=img)
    canvas.pack()
    oval=canvas.create_oval(x1,y1,x2,y2,fill='red')

    #gul속 내위치 이동 하는 함수 
    def func(event):
        x,y=location(int(Entry.get(display_width)),int(Entry.get(display_height)))

        #공을 이동 시킨다.
        canvas.move(oval,x,y)
        root.update()

    #나의 현실속 가로 좌표를 입력하는 칸
    display_width= Entry(root, width=20) 
    display_width.pack()
    #나의 현실속 세로 좌표를 입력하는 칸
    display_height= Entry(root, width=20) 
    display_height.pack()

    #엔터를 누르면 발생하는 func함수 실행
    root.bind('<Return>', func)

    #종료
    def quit():
        root.destroy()

    while True:
        Button(root, text="Quit", command=quit).pack()
        root.mainloop()


main()
