from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog
from function import *

np.seterr(divide='ignore', invalid='ignore')
root = Tk()
root.geometry("1035x768+200+2")
root.title("Bóng Đá Plus")
root.resizable(width= False, height=True)
load= Image.open("background.jpg")
render=ImageTk.PhotoImage(load)
img= Label(root,image= render)
img.place(x=0, y= 0)
#root.iconbitmap("icon.ico")


def hiden_button():
    bT_result1.place_forget()
    bT_result2.place_forget()
    bT_result3.place_forget()
    bT_result4.place_forget()
    bT_result5.place_forget()
    my_text.delete("1.0", END)
    my_text.place_forget()
    tb_result.place_forget()


bT_clear = Button(root, text="Tìm Kiếm", width=8, font="Bold 10", command=hiden_button)
bT_clear.place(x=10, y=10)

entry1 = Entry(root , font= "Bold 10", width= 60)
entry1.place(x= 100, y= 10)

# def get_query():
#     query= entry1.get()
#     return query


def display_button():
    bT_result1.place_forget()
    bT_result2.place_forget()
    bT_result3.place_forget()
    bT_result4.place_forget()
    bT_result5.place_forget()
    my_text.delete("1.0", END)
    my_text.place_forget()
    tb_result.place_forget()
    query= entry1.get()
    titles, file_names = search(query)
    if len(titles)==1:
        bT_result1.place(x= 50 , y = 100)
        bT_result1.config(text = titles[0])
    elif len(titles)==2:
        bT_result1.place(x= 50 , y = 100)
        bT_result1.config(text = titles[0])
        bT_result2.place(x= 50 , y = 140 )
        bT_result2.config(text = titles[1])
    elif len(titles)==3:
        bT_result1.place(x= 50 , y = 100)
        bT_result1.config(text = titles[0])
        bT_result2.place(x= 50 , y = 140 )
        bT_result2.config(text = titles[1])
        bT_result3.place(x= 50 , y = 180 )
        bT_result3.config(text = titles[2])
    elif len(titles)==4:
        bT_result1.place(x= 50 , y = 100)
        bT_result1.config(text = titles[0])
        bT_result2.place(x= 50 , y = 140 )
        bT_result2.config(text = titles[1])
        bT_result3.place(x= 50 , y = 180 )
        bT_result3.config(text = titles[2])
        bT_result4.place(x= 50 , y = 220 )
        bT_result4.config(text = titles[3])
    elif len(titles)==5:
        bT_result1.place(x= 50 , y = 100)
        bT_result1.config(text = titles[0])
        bT_result2.place(x= 50 , y = 140 )
        bT_result2.config(text = titles[1])
        bT_result3.place(x= 50 , y = 180 )
        bT_result3.config(text = titles[2])
        bT_result4.place(x= 50 , y = 220 )
        bT_result4.config(text = titles[3])
        bT_result5.place(x= 50 , y = 260 )
        bT_result5.config(text = titles[4])
    else:
        tb_result.place(x= 50 , y = 100)

tb_result = Label(root,width = 50,height = 3, font = "Times 14", text = "Không tìm thấy kết quả nào")
def display_text1():
    my_text.delete("1.0",END)
    query= entry1.get()
    titles, file_names = search(query)
    path = file_names[0]
    news= open(path, "r",encoding="utf8")
    a=news.read()
    my_text.insert(END,a)
    my_text.place(x=30, y= 330)
    my_text.config(anchor=CENTER)
    a.close()

def display_text2():
    my_text.delete("1.0",END)
    query= entry1.get()
    titles, file_names = search(query)
    path = file_names[1]
    news= open(path, "r",encoding="utf8")
    a=news.read()
    my_text.insert(END,a)
    my_text.place(x=30, y= 330)
    my_text.config(anchor=CENTER)
    a.close()

def display_text3():
    my_text.delete("1.0",END)
    query= entry1.get()
    titles, file_names = search(query)
    path = file_names[2]
    news= open(path, "r",encoding="utf8")
    a=news.read()
    my_text.insert(END,a)
    my_text.place(x=30, y= 330)
    my_text.config(anchor=CENTER)
    a.close()

def display_text4():
    my_text.delete("1.0",END)
    query= entry1.get()
    titles, file_names = search(query)
    path = file_names[3]
    news= open(path, "r",encoding="utf8")
    a=news.read()
    my_text.insert(END,a)
    my_text.place(x=30, y= 330)
    my_text.config(anchor=CENTER)
    a.close()

def display_text5():
    my_text.delete("1.0",END)
    query= entry1.get()
    titles, file_names = search(query)
    path = file_names[4]
    news= open(path, "r",encoding="utf8")
    a=news.read()
    my_text.insert(END,a)
    my_text.place(x=30, y= 330)
    my_text.config(anchor=CENTER)
    a.close()

def open_txt():
   text_file= filedialog.askopenfilename(filetypes=(("Text_file", "*.txt"), ))
   stuff= open(text_file, "r",encoding="utf8")
   a=stuff.read()
   my_text.insert(END,a)
   stuff.close()
my_text= Text(root, width=118, height=28 )
#my_text.place(x=30, y= 380)
my_text2= Text(root, width=118, height=22 )
#my_text2.place(x=30, y= 750)

Bt1= Button(root, text= "Search", font= "Times 10",width= 10, command= display_button)
Bt1.place(x=600, y =10 )
    

bT_result1= Button(root,width= 80 ,font= "Times 12", command= display_text1)
bT_result2= Button(root, width= 80,font= "Times 12", command= display_text2)
bT_result3= Button(root, width= 80, font= "Times 12", command= display_text3)
bT_result4= Button(root,width= 80, font= "Times 12", command= display_text4)
bT_result5= Button(root,width= 80, font= "Times 12", command= display_text5)

# bt1= Button(root, text="Xem", command=open_txt)
# bt1. place(x=10, y=340)



lbl3 = Label(root, text="Kết Quả", width=7)
lbl3.place(x=10, y= 60)


# mytree=ttk.Treeview(root)
# mytree["columns"]= ("Headline", "Date")
# mytree.column("Headline", anchor=W, width= 600)
# mytree.column("#0", width=0)
# mytree.column("Date", anchor= W, width= 200)
# mytree.heading("Date",text="Date",anchor=W)
# mytree.heading("Headline",text="Headline",anchor=W)
# data=[
#     [ "Bale giúp Tottenham vào bán kết Cup Liên đoàn", "11/11/2020"],
#     ["Inter thắng trận thứ bảy liên tiếp tại Serie A","22/12/2020"], 
#     ["Vì sao HLV Park Hang Seo không dùng dàn sao mạnh nhất đội tuyển Việt Nam đấu U22?","23/12/2020"]
# ]
# count= 0
# for new in data:
#     mytree.insert(parent="", index="end",iid=count, text="",values=(new[0], new[1]) )
#     count+=1
# mytree.place(x=30, y =100 )

# news_text= Text(form1, width=118 , height=25 )
# news_text.place(x= 30 , y = 350)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# scrollbar= Scrollbar(news_text)
# scrollbar.pack(side="right",fill="y",expand=False)


root.mainloop() 


