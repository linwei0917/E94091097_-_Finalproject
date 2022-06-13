#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder

date_data = pd.read_csv('fordating.csv')

X = date_data.drop(columns=['姓名'])   #input data
y = date_data['姓名']                  #output data

#把文字定義成有序的數字
le_age = LabelEncoder()
le_gen = LabelEncoder()
le_music = LabelEncoder()
le_height = LabelEncoder()
le_flavor = LabelEncoder()
#X['age_n'] = le_age.fit_transform(X['年齡'])
X['gen_n'] = le_gen.fit_transform(X['性別'])
X['music_n'] = le_music.fit_transform(X['音樂'])
#X['height_n'] = le_height.fit_transform(X['身高'])
X['flavor_n'] = le_flavor.fit_transform(X['口味'])
X_new = X.drop(['性別','音樂','口味'],axis='columns')
X_new


# In[74]:


#model來訓練模型，測試集給定0.2
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_new,y,test_size=0.1)


# In[75]:


#決策樹
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

model = DecisionTreeClassifier()
model.fit(X_train,y_train)

predictions = model.predict(X_test)
score = accuracy_score(y_test,predictions)

#測試能否成功
#年齡,身高,性別,音樂,口味
what = model.predict([ [18,167,1,2,0] ])
print('你的預測適合對象為:',what)


# In[76]:


#創造GUI介面
import tkinter as tk
from PIL import ImageTk, Image

win = tk.Tk()
win.title("匹配交友 - 尋找你的另一半")
win.geometry("550x1000") #寬*高

#背景介面
image1 = Image.open("mybg.jpg")
test = ImageTk.PhotoImage(image1)
labelbg = tk.Label(image=test)
labelbg.image = test
labelbg.place(x=0, y=0)

#Label 顯示
label = tk.Label(win,relief="ridge",text="理想型年齡",bg='#ffc5cb',font=("Arial",12))
label.place(x=5,y=5)
labelQ = tk.Label(win,text="請輸入年齡 : ",bg='#fdff52',font=("Arial",10))
labelQ.place(x=130,y=5)

label2 = tk.Label(win,relief="ridge",text="想配對到的性別",bg='#ffc5cb',font=("Arial",12))
label2.place(x=0,y=40)

label3 = tk.Label(win,relief="ridge",text="偏好的身高",bg='#ffc5cb',font=("Arial",12))
label3.place(x=0,y=160)
labelQ = tk.Label(win,text="請輸入身高 : ",bg='#fdff52',font=("Arial",10))
labelQ.place(x=130,y=160)

label3 = tk.Label(win,relief="ridge",text="你喜歡的音樂類型",bg='#ffc5cb',font=("Arial",12))
label3.place(x=0,y=200)
label3 = tk.Label(win,relief="ridge",text="如果要約會，會選擇怎麼樣的食物味道",bg='#ffc5cb',font=("Arial",12))
label3.place(x=0,y=360)


#Entry 輸入
var1 = tk.StringVar()  #年齡
var4 = tk.StringVar()  #身高
#輸入年齡
e1 = tk.Entry(win,width=30,textvariable=var1)
e1.place(x=250,y=5,width=180,height=40)
#輸入身高
e2 = tk.Entry(win,width=30,textvariable=var4)
e2.place(x=250,y=160,width=180,height=40)


# In[77]:


#當按鈕按下去執行

#性別    
def pick_age():
    age=var1.get()
    global age_new
    age_new=int(age)
    
def pick_gen_men():
    global gen_new
    gen_new=1
    labelpick1 = tk.Label(win,text="你已選擇:男生",bg='#ffffd4',font=("Arial",12))
    labelpick1.place(x=200, y=120)

def pick_gen_women():
    global gen_new
    gen_new=0
    labelpick2 = tk.Label(win,text="你已選擇:女生",bg='#ffffd4',font=("Arial",12))
    labelpick2.place(x=200, y=120)
#音樂  
def pick_m1():
    global music_new
    music_new=2
    labelpickm1 = tk.Label(win,text="你已選擇:抒情音樂",bg='#ffffd4',font=("Arial",12))
    labelpickm1.place(x=200, y=320)
def pick_m2():
    global music_new
    music_new=3
    labelpickm2 = tk.Label(win,text="你已選擇:電子音樂",bg='#ffffd4',font=("Arial",12))
    labelpickm2.place(x=200, y=320)
def pick_m3():
    global music_new
    music_new=4
    labelpickm3 = tk.Label(win,text="你已選擇:鄉村音樂",bg='#ffffd4',font=("Arial",12))
    labelpickm3.place(x=200, y=320)
def pick_m4():
    global music_new
    music_new=5
    labelpickm4 = tk.Label(win,text="你已選擇:饒舌音樂",bg='#ffffd4',font=("Arial",12))
    labelpickm4.place(x=200, y=320)
def pick_m5():
    global music_new
    music_new=0
    labelpickm5 = tk.Label(win,text="你已選擇:K-pop",bg='#ffffd4',font=("Arial",12))
    labelpickm5.place(x=200, y=320)
def pick_m6():
    global music_new
    music_new=1
    labelpickm6 = tk.Label(win,text="你已選擇:古典音樂",bg='#ffffd4',font=("Arial",12))
    labelpickm6.place(x=200, y=320)

#身高
def pick_hieght():
    hieght=var4.get()
    global hieght_new
    hieght_new=int(hieght)
#口味
def pick_f1():
    global flavor_new
    flavor_new = 0
    labelpickf1 = tk.Label(win,text="你已選擇:甜",bg='#ffffd4',font=("Arial",12))
    labelpickf1.place(x=200, y=440)
def pick_f2():
    global flavor_new
    flavor_new = 1
    labelpickf2 = tk.Label(win,text="你已選擇:辣",bg='#ffffd4',font=("Arial",12))
    labelpickf2.place(x=200, y=440)
def pick_f3():
    global flavor_new
    flavor_new = 2
    labelpickf3 = tk.Label(win,text="你已選擇:鹹",bg='#ffffd4',font=("Arial",12))
    labelpickf3.place(x=200, y=440)


# In[78]:


#當按鈕按下去執行
def who():
    date_data = pd.read_csv('fordating.csv')
    X = date_data.drop(columns=['姓名'])
    y = date_data['姓名']

    le_age = LabelEncoder()
    le_gen = LabelEncoder()
    le_music = LabelEncoder()
    le_height = LabelEncoder()
    le_flavor = LabelEncoder()
    X['age_n'] = le_age.fit_transform(X['年齡'])
    X['gen_n'] = le_gen.fit_transform(X['性別'])
    X['music_n'] = le_music.fit_transform(X['音樂'])
    X['height_n'] = le_height.fit_transform(X['身高'])
    X['flavor_n'] = le_flavor.fit_transform(X['口味'])
    X_new = X.drop(['年齡','性別','音樂','身高','口味'],axis='columns')
    model = DecisionTreeClassifier()
    model.fit(X_train,y_train)


    predictions = model.predict(X_test)
    score = accuracy_score(y_test,predictions)
    score_new = str(score)
   
    what = model.predict([ [var1.get(),var4.get(),gen_new,music_new,flavor_new] ])
    label4 = tk.Label(win,relief="ridge",text="你的預測適合對象為:"+what,bg='white',font=("Arial",12))
    label4.place(x=0,y=540)
    label4 = tk.Label(win,relief="ridge",text="祝您早日找到有緣人^_^",bg='white',font=("Arial",12))
    label4.place(x=0,y=580)
    image2 = Image.open("hopeyoufindlove.jpg")
    test2 = ImageTk.PhotoImage(image2)
    labelbg = tk.Label(image=test2)
    labelbg.image = test2
    labelbg.place(x=250, y=500)


# In[79]:


#Button 按鈕

#性別
menbutton = tk.Button(win,width=5,height=1,text="男生",bg='lightblue',command=pick_gen_men,font=("Arial",12))
menbutton.place(x=200,y=80)
wonmenbutton = tk.Button(win,width=5,height=1,text="女生",bg='pink',command=pick_gen_women,font=("Arial",12))
wonmenbutton.place(x=300,y=80)
#音樂
m1 = tk.Button(win,width=8,height=1,text="抒情音樂",command=pick_m1,font=("Arial",12))
m1.place(x=100,y=240)
m1 = tk.Button(win,width=8,height=1,text="電子音樂",command=pick_m2,font=("Arial",12))
m1.place(x=200,y=240)
m1 = tk.Button(win,width=8,height=1,text="鄉村音樂",command=pick_m3,font=("Arial",12))
m1.place(x=300,y=240)
m1 = tk.Button(win,width=8,height=1,text="饒舌音樂",command=pick_m4,font=("Arial",12))
m1.place(x=400,y=240)
m1 = tk.Button(win,width=8,height=1,text="K-pop",command=pick_m5,font=("Arial",12))
m1.place(x=100,y=280)
m1 = tk.Button(win,width=8,height=1,text="古典音樂",command=pick_m6,font=("Arial",12))
m1.place(x=200,y=280)
#口味
m1 = tk.Button(win,width=5,height=1,text="甜",command=pick_f1,font=("Arial",12))
m1.place(x=100,y=400)
m1 = tk.Button(win,width=5,height=1,text="辣",command=pick_f2,font=("Arial",12))
m1.place(x=200,y=400)
m1 = tk.Button(win,width=5,height=1,text="鹹",command=pick_f3,font=("Arial",12))
m1.place(x=300,y=400)
#確認預測
result = tk.Button(win,width=8,height=1,text="開始匹配...",bg='yellow',command=who,font=("Arial",12))
result.place(x=0,y=500)


# In[80]:


win.mainloop()


# In[ ]:




