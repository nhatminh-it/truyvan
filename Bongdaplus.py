from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog
import glob
import numpy as np
import re
import pickle
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
    with open(r"D:\Github\truyvan\contents.txt", "rb") as fp: 
        contents = pickle.load(fp)
    with open(r"D:\Github\truyvan\vocab.txt", "rb") as fp: 
        vocab = pickle.load(fp)
    with open(r"D:\Github\truyvan\paths.txt", "rb") as fp: 
        paths = pickle.load(fp)
    with open(r"D:\Github\truyvan\TF.txt", "rb") as fp: 
        TF = pickle.load(fp)  
    with open(r"D:\Github\truyvan\IDF.txt", "rb") as fp: 
        IDF = pickle.load(fp)  
    # TF = np.load(r'D:\Github\truyvan\TF.npy')
    # IDF = np.load(r'D:\Github\truyvan\IDF.npy')

    #query='Ronaldo hét lên mừng bàn thắng của Morata'
    #query = input()
    #print('query: ', query)
    requests = []
    regex = r"([\'\"])((\\\1|.)*?)\1"
    matches = re.finditer(regex, query, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            if groupNum == 2:
                requests.append(match.group(groupNum))
    #print('Từ khóa cứng: ', requests)
    query = query.replace('"', '')
    qcontent = query.split()
    qTF = calc_tf_weighting(vocab, [qcontent])

    # BUOC 4: Xay dung vector TF_IDF weighting cho
    # tap van ban va truy van
    TF_IDF = TF*IDF
    qTF_IDF = qTF*IDF
    # BUOC 5: Tinh do tuong dong cua query va cac van ban
    # su dung TF_IDF weighting
    dists = np.linalg.norm(qTF_IDF - TF_IDF, axis=0)
    # BUOC 6: Sap xep de sap hang va hien thi ket qua
    rank = np.argsort(dists)
    #print(rank)
    topK = 5
    count = 0
    titles = []
    file_names = []
    for i in range(topK):
        #print('Van ban gan thu ', i+1, ' la: ', ' '.join(contents[rank[i]]))
        kt = 0
        for request in requests:
            if request in ' '.join(contents[rank[i]]).lower():
                kt += 1
        if kt == len(requests):
            count += 1
            #print('file paths', paths[rank[i]][-5])
            file_names.append(paths[rank[i]][-5:])
            f = open(paths[rank[i]], encoding="utf-8")
            title = f.readline()
            #print("title",title)
            titles.append(title[:-1])

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
    with open(r"D:\Github\truyvan\contents.txt", "rb") as fp: 
        contents = pickle.load(fp)
    with open(r"D:\Github\truyvan\vocab.txt", "rb") as fp: 
        vocab = pickle.load(fp)
    with open(r"D:\Github\truyvan\paths.txt", "rb") as fp: 
        paths = pickle.load(fp)
    with open(r"D:\Github\truyvan\TF.txt", "rb") as fp: 
        TF = pickle.load(fp)  
    with open(r"D:\Github\truyvan\IDF.txt", "rb") as fp: 
        IDF = pickle.load(fp)  
    # TF = np.load(r'D:\Github\truyvan\TF.npy')
    # IDF = np.load(r'D:\Github\truyvan\IDF.npy')

    #query='Ronaldo hét lên mừng bàn thắng của Morata'
    #query = input()
    #print('query: ', query)
    requests = []
    regex = r"([\'\"])((\\\1|.)*?)\1"
    matches = re.finditer(regex, query, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            if groupNum == 2:
                requests.append(match.group(groupNum))
    #print('Từ khóa cứng: ', requests)
    query = query.replace('"', '')
    qcontent = query.split()
    qTF = calc_tf_weighting(vocab, [qcontent])

    # BUOC 4: Xay dung vector TF_IDF weighting cho
    # tap van ban va truy van

    TF_IDF = TF*IDF
    qTF_IDF = qTF*IDF
    # BUOC 5: Tinh do tuong dong cua query va cac van ban
    # su dung TF_IDF weighting
    dists = np.linalg.norm(qTF_IDF - TF_IDF, axis=0)
    # BUOC 6: Sap xep de sap hang va hien thi ket qua
    rank = np.argsort(dists)
    #print(rank)
    topK = 5
    count = 0
    titles = []
    file_names = []
    for i in range(topK):
        #print('Van ban gan thu ', i+1, ' la: ', ' '.join(contents[rank[i]]))
        kt = 0
        for request in requests:
            if request in ' '.join(contents[rank[i]]).lower():
                kt += 1
        if kt == len(requests):
            count += 1
            #print('file paths', paths[rank[i]][-5])
            file_names.append(paths[rank[i]][-5:])
            f = open(paths[rank[i]], encoding="utf-8")
            title = f.readline()
            #print("title",title)
            titles.append(title[:-1])
    path = "D:\\Github\\truyvan\\data\\" + file_names[0]
    news= open(path, "r",encoding="utf8")
    a=news.read()
    my_text.insert(END,a)
    my_text.place(x=30, y= 330)
    my_text.config(anchor=CENTER)
    a.close()

def display_text2():
    my_text.delete("1.0",END)
    query= entry1.get()
    with open(r"D:\Github\truyvan\contents.txt", "rb") as fp: 
        contents = pickle.load(fp)
    with open(r"D:\Github\truyvan\vocab.txt", "rb") as fp: 
        vocab = pickle.load(fp)
    with open(r"D:\Github\truyvan\paths.txt", "rb") as fp: 
        paths = pickle.load(fp)
    with open(r"D:\Github\truyvan\TF.txt", "rb") as fp: 
        TF = pickle.load(fp)  
    with open(r"D:\Github\truyvan\IDF.txt", "rb") as fp: 
        IDF = pickle.load(fp)  
    # TF = np.load(r'D:\Github\truyvan\TF.npy')
    # IDF = np.load(r'D:\Github\truyvan\IDF.npy')

    #query='Ronaldo hét lên mừng bàn thắng của Morata'
    #query = input()
    #print('query: ', query)
    requests = []
    regex = r"([\'\"])((\\\1|.)*?)\1"
    matches = re.finditer(regex, query, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            if groupNum == 2:
                requests.append(match.group(groupNum))
    #print('Từ khóa cứng: ', requests)
    query = query.replace('"', '')
    qcontent = query.split()
    qTF = calc_tf_weighting(vocab, [qcontent])

    # BUOC 4: Xay dung vector TF_IDF weighting cho
    # tap van ban va truy van

    TF_IDF = TF*IDF
    qTF_IDF = qTF*IDF
    # BUOC 5: Tinh do tuong dong cua query va cac van ban
    # su dung TF_IDF weighting
    dists = np.linalg.norm(qTF_IDF - TF_IDF, axis=0)
    # BUOC 6: Sap xep de sap hang va hien thi ket qua
    rank = np.argsort(dists)
    #print(rank)
    topK = 5
    count = 0
    titles = []
    file_names = []
    for i in range(topK):
        #print('Van ban gan thu ', i+1, ' la: ', ' '.join(contents[rank[i]]))
        kt = 0
        for request in requests:
            if request in ' '.join(contents[rank[i]]).lower():
                kt += 1
        if kt == len(requests):
            count += 1
            #print('file paths', paths[rank[i]][-5])
            file_names.append(paths[rank[i]][-5:])
            f = open(paths[rank[i]], encoding="utf-8")
            title = f.readline()
            #print("title",title)
            titles.append(title[:-1])
    path = "D:\\Github\\truyvan\\data\\" + file_names[1]
    news= open(path, "r",encoding="utf8")
    a=news.read()
    my_text.insert(END,a)
    my_text.place(x=30, y= 330)
    my_text.config(anchor=CENTER)
    a.close()

def display_text3():
    my_text.delete("1.0",END)
    query= entry1.get()
    with open(r"D:\Github\truyvan\contents.txt", "rb") as fp: 
        contents = pickle.load(fp)
    with open(r"D:\Github\truyvan\vocab.txt", "rb") as fp: 
        vocab = pickle.load(fp)
    with open(r"D:\Github\truyvan\paths.txt", "rb") as fp: 
        paths = pickle.load(fp)
    with open(r"D:\Github\truyvan\TF.txt", "rb") as fp: 
        TF = pickle.load(fp)  
    with open(r"D:\Github\truyvan\IDF.txt", "rb") as fp: 
        IDF = pickle.load(fp)  
    # TF = np.load(r'D:\Github\truyvan\TF.npy')
    # IDF = np.load(r'D:\Github\truyvan\IDF.npy')

    #query='Ronaldo hét lên mừng bàn thắng của Morata'
    #query = input()
    #print('query: ', query)
    requests = []
    regex = r"([\'\"])((\\\1|.)*?)\1"
    matches = re.finditer(regex, query, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            if groupNum == 2:
                requests.append(match.group(groupNum))
    #print('Từ khóa cứng: ', requests)
    query = query.replace('"', '')
    qcontent = query.split()
    qTF = calc_tf_weighting(vocab, [qcontent])

    # BUOC 4: Xay dung vector TF_IDF weighting cho
    # tap van ban va truy van

    TF_IDF = TF*IDF
    qTF_IDF = qTF*IDF
    # BUOC 5: Tinh do tuong dong cua query va cac van ban
    # su dung TF_IDF weighting
    dists = np.linalg.norm(qTF_IDF - TF_IDF, axis=0)
    # BUOC 6: Sap xep de sap hang va hien thi ket qua
    rank = np.argsort(dists)
    #print(rank)
    topK = 5
    count = 0
    titles = []
    file_names = []
    for i in range(topK):
        #print('Van ban gan thu ', i+1, ' la: ', ' '.join(contents[rank[i]]))
        kt = 0
        for request in requests:
            if request in ' '.join(contents[rank[i]]).lower():
                kt += 1
        if kt == len(requests):
            count += 1
            #print('file paths', paths[rank[i]][-5])
            file_names.append(paths[rank[i]][-5:])
            f = open(paths[rank[i]], encoding="utf-8")
            title = f.readline()
            #print("title",title)
            titles.append(title[:-1])
    path = "D:\\Github\\truyvan\\data\\" + file_names[2]
    news= open(path, "r",encoding="utf8")
    a=news.read()
    my_text.insert(END,a)
    my_text.place(x=30, y= 330)
    my_text.config(anchor=CENTER)
    a.close()

def display_text4():
    my_text.delete("1.0",END)
    query= entry1.get()
    with open(r"D:\Github\truyvan\contents.txt", "rb") as fp: 
        contents = pickle.load(fp)
    with open(r"D:\Github\truyvan\vocab.txt", "rb") as fp: 
        vocab = pickle.load(fp)
    with open(r"D:\Github\truyvan\paths.txt", "rb") as fp: 
        paths = pickle.load(fp)
    with open(r"D:\Github\truyvan\TF.txt", "rb") as fp: 
        TF = pickle.load(fp)  
    with open(r"D:\Github\truyvan\IDF.txt", "rb") as fp: 
        IDF = pickle.load(fp)  
    # TF = np.load(r'D:\Github\truyvan\TF.npy')
    # IDF = np.load(r'D:\Github\truyvan\IDF.npy')

    #query='Ronaldo hét lên mừng bàn thắng của Morata'
    #query = input()
    #print('query: ', query)
    requests = []
    regex = r"([\'\"])((\\\1|.)*?)\1"
    matches = re.finditer(regex, query, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            if groupNum == 2:
                requests.append(match.group(groupNum))
    #print('Từ khóa cứng: ', requests)
    query = query.replace('"', '')
    qcontent = query.split()
    qTF = calc_tf_weighting(vocab, [qcontent])

    # BUOC 4: Xay dung vector TF_IDF weighting cho
    # tap van ban va truy van

    TF_IDF = TF*IDF
    qTF_IDF = qTF*IDF
    # BUOC 5: Tinh do tuong dong cua query va cac van ban
    # su dung TF_IDF weighting
    dists = np.linalg.norm(qTF_IDF - TF_IDF, axis=0)
    # BUOC 6: Sap xep de sap hang va hien thi ket qua
    rank = np.argsort(dists)
    #print(rank)
    topK = 5
    count = 0
    titles = []
    file_names = []
    for i in range(topK):
        #print('Van ban gan thu ', i+1, ' la: ', ' '.join(contents[rank[i]]))
        kt = 0
        for request in requests:
            if request in ' '.join(contents[rank[i]]).lower():
                kt += 1
        if kt == len(requests):
            count += 1
            #print('file paths', paths[rank[i]][-5])
            file_names.append(paths[rank[i]][-5:])
            f = open(paths[rank[i]], encoding="utf-8")
            title = f.readline()
            #print("title",title)
            titles.append(title[:-1])
    path = "D:\\Github\\truyvan\\data\\" + file_names[3]
    news= open(path, "r",encoding="utf8")
    a=news.read()
    my_text.insert(END,a)
    my_text.place(x=30, y= 330)
    my_text.config(anchor=CENTER)
    a.close()

def display_text5():
    my_text.delete("1.0",END)
    query= entry1.get()
    with open(r"D:\Github\truyvan\contents.txt", "rb") as fp: 
        contents = pickle.load(fp)
    with open(r"D:\Github\truyvan\vocab.txt", "rb") as fp: 
        vocab = pickle.load(fp)
    with open(r"D:\Github\truyvan\paths.txt", "rb") as fp: 
        paths = pickle.load(fp)
    with open(r"D:\Github\truyvan\TF.txt", "rb") as fp: 
        TF = pickle.load(fp)  
    with open(r"D:\Github\truyvan\IDF.txt", "rb") as fp: 
        IDF = pickle.load(fp)  
    # TF = np.load(r'D:\Github\truyvan\TF.npy')
    # IDF = np.load(r'D:\Github\truyvan\IDF.npy')

    #query='Ronaldo hét lên mừng bàn thắng của Morata'
    #query = input()
    #print('query: ', query)
    requests = []
    regex = r"([\'\"])((\\\1|.)*?)\1"
    matches = re.finditer(regex, query, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            if groupNum == 2:
                requests.append(match.group(groupNum))
    #print('Từ khóa cứng: ', requests)
    query = query.replace('"', '')
    qcontent = query.split()
    qTF = calc_tf_weighting(vocab, [qcontent])

    # BUOC 4: Xay dung vector TF_IDF weighting cho
    # tap van ban va truy van

    TF_IDF = TF*IDF
    qTF_IDF = qTF*IDF
    # BUOC 5: Tinh do tuong dong cua query va cac van ban
    # su dung TF_IDF weighting
    dists = np.linalg.norm(qTF_IDF - TF_IDF, axis=0)
    # BUOC 6: Sap xep de sap hang va hien thi ket qua
    rank = np.argsort(dists)
    #print(rank)
    topK = 5
    count = 0
    titles = []
    file_names = []
    for i in range(topK):
        #print('Van ban gan thu ', i+1, ' la: ', ' '.join(contents[rank[i]]))
        kt = 0
        for request in requests:
            if request in ' '.join(contents[rank[i]]).lower():
                kt += 1
        if kt == len(requests):
            count += 1
            #print('file paths', paths[rank[i]][-5])
            file_names.append(paths[rank[i]][-5:])
            f = open(paths[rank[i]], encoding="utf-8")
            title = f.readline()
            #print("title",title)
            titles.append(title[:-1])
    path = "D:\\Github\\truyvan\\data\\" + file_names[4]
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


