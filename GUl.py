from tkinter import*
from PIL import Image,ImageTk
def main():
    
    id_arr=[]#유저 모임
    #현실크기
    real_width=159550
    real_height=44200
    
    #GUI
    root = Tk()
    root.title("GUI")#타이틀 이름
    root.resizable(True,True)#창의 크기 조절가능여부
    
    image = Image.open("EngrBldg1stFloor.png")#이미지 오픈
    copy_of_image = image.copy()#카피 본 저장
    photo = ImageTk.PhotoImage(image)
    
    picture_width,picture_height=image.size#사진 크기 저장
    root.geometry(str(image.size[0])+"x"+str(image.size[1]+60))#GUI크기
    canvas = Canvas(root,width=picture_width,height=picture_height)#캔버스
    canvas.pack(fill="both",expand=True)

    image1=canvas.create_image(0,0,anchor=NW,image=photo)#캔버스에 이미지 추가

    #유저 클래스
    class usar:

        def __init__(self,width,height,name):
            self.myrealwidth,self.myrealheight=width,height#현실좌표
            self.id=name
            x,y=location(width,height)
            self.text=canvas.create_text(x,y, text =name, font = ("나눔고딕코딩", 10), fill = "red")
        
        def setLocation(self,width,height):
            self.myrealwidth,self.myrealheight=width,height

        def getLocation(self):
            return self.myrealwidth,self.myrealheight

        def getId(self):
            return self.id
    
        def getText(self):
            return self.text

    #현실 좌표를 받으면 사진좌표를 리턴하는 함수
    def location(x,y):
        global picture_width
        global picture_height
        my_real_width=x
        my_real_height=y
    
        #현실좌표를 사진속 좌표로 바꾸기
        my_picture_width=my_real_width*picture_width//real_width
        my_picture_height=my_real_height*picture_height//real_height
        print(picture_width,picture_height)
        return my_picture_width,my_picture_height#사진 속 좌표 리턴

    #이미지 크기 조정 함수
    def resize_image(event):
        global picture_width
        global picture_height
        image = copy_of_image.resize((event.width, event.height))
        photo = ImageTk.PhotoImage(image)
        canvas.itemconfig(image1,image = photo)
        canvas.image = photo
        
        windowWidth = canvas.winfo_width()#창의 가로길이
        windowHeight = canvas.winfo_height()#창의 세로길이
        picture_width,picture_height=windowWidth,windowHeight-6
        print(picture_width,picture_height)
        for us in id_arr:
            x,y=location(us.getLocation()[0],us.getLocation()[1])   
            move_width=x-int(canvas.coords(us.getText())[0])#x축 이동거리 계산
            move_height=y-int(canvas.coords(us.getText())[1])#y축 이동거리 계산 
            canvas.move(us.getText(),move_width,move_height)#공을 이동
            root.update()

    #마우스의 좌표를 출력 함수
    def click(event):
        print("클릭위치",event.x,event.y)
        my_real_width=event.x*real_width//picture_width
        my_real_height=event.y*real_height//picture_height
        print("현실위치",my_real_width,my_real_height)
        root.update()

        
    #gul속 빨간공을 이동시키는  함수 
    def move(event):
        x,y=location(int(Entry.get(display_width)),int(Entry.get(display_height)))
        
        for us in id_arr:
            if us.getId()==Entry.get(display_id):
                x1,y1=location(us.getLocation()[0],us.getLocation()[1])
                
                move_width=x-x1#x축 이동거리 계산
                move_height=y-y1#y축 이동거리 계산
                
                us.setLocation(int(Entry.get(display_width)),int(Entry.get(display_height)))
                canvas.move(us.getText(),move_width,move_height)#공을 이동
                root.update()
    
    #유저생성함수
    def idarr():
        id_arr.append(usar(int(Entry.get(display_width)),int(Entry.get(display_height)),(Entry.get(display_id))))
        
    #유저삭제함수
    def delete():
        num=0
        for us in id_arr:
            if us.getId()==Entry.get(display_id):
                canvas.delete(us.getText())
                del id_arr[num]
            num=num+1

    #유저 이름  칸
    display_id= Entry(root, width=20) 
    display_id.pack()
    
    #add 버튼
    btn = Button(root, text="add",command=idarr)
    btn.pack(side=RIGHT)
    
    #Delete버튼
    btn2 = Button(root, text="delete",command=delete)
    btn2.pack(side=RIGHT)
    
    #나의 현실 가로 좌표를 입력하는 칸
    display_width= Entry(root, width=20) 
    display_width.pack()
    
    #나의 현실 세로 좌표를 입력하는 칸
    display_height= Entry(root, width=20) 
    display_height.pack()
    
    #위젯의 모양이 수정되었을 때 resize_image함수 실행
    canvas.bind('<Configure>', resize_image)
        
    #엔터를 누르면 move함수 실행
    root.bind('<Return>', move)
    
    #마우스 왼쪽클릭 click함수 실행
    root.bind("<Button-1>",click)
    
    root.mainloop()
    

main()
