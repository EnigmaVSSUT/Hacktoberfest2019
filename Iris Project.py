
'''##predict for new flower
print(K.predict([[6,4,3,4]]))  ##[2] or [1]'''


from tkinter import *
import tkinter.messagebox as m
w=Tk()
#classifiaction of IRIS flower using machine learning
##load iris data to program

import warnings
warnings.simplefilter(action='ignore')

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris=load_iris()
print(iris)


##separating input and output

X=iris.data ##numpy array
Y=iris.target  ##numpy array
print(X) 
print(Y)  
print(X.shape)  #(150,4)
print(Y.shape)  #(150,)

##split dataset for training and testing
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

###  150*0.2=30 IS TESTED
### 150*0.8=120  IS TRAINED
print(X_train.shape)  #(120,4)
print(Y_train.shape)  #(120,)
print(X_test.shape)   #(30,4)
print(Y_test.shape)   #(30,)

acc_knn=0
acc_knn1=0
acc_knn2=0
acc_knn4=0

###CREATE A MODEL  ## KNN
##K Nearest Neighbors algorithm

from sklearn.neighbors import KNeighborsClassifier
K=KNeighborsClassifier(n_neighbors=5)
  
##Train the model BY training dataset
K.fit(X_train,Y_train)
 
##test the model by testing data
Y_pred=K.predict(X_test)

##find accuracy
from sklearn.metrics import accuracy_score
acc_knn=accuracy_score(Y_test,Y_pred)
acc_knn=round(acc_knn*100,2)


def knn():
    c=str(acc_knn) + " %"
    m.showinfo(title="KNN",message=c)    
    print("accuracy score in KNN is",acc_knn,"%")
    print(K.predict([[a,b,c,d]]))

    
def lg():
    c=str(acc_knn1) + " %"
    m.showinfo(title="LR",message=c)
    print("accuracy score in LG is",acc_knn1,"%")
    print(logreg.predict([[a,b,c,d]]))


##logistic regression
from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
logreg.fit(X_train,Y_train)
Y_pred1=logreg.predict(X_test)



from sklearn.metrics import accuracy_score
acc_knn1=accuracy_score(Y_test,Y_pred1)
acc_knn1=round(acc_knn1*100,2)


def dt():
    c="gini: "+ str(acc_knn2) + " %"
    c=c + " entropy: "+ str(acc_knn3) + " %"
    m.showinfo(title="DT ENTROPY",message=c)
    print("accuracy score in DT GINI is",acc_knn2,"%")
    print(dtgini.predict([[a,b,c,d]]))
    print("accuracy score in DT ENTROPY is",acc_knn3,"%")
    print(dtentropy.predict([[a,b,c,d]]))

    
###Decision Tree
from sklearn.tree import DecisionTreeClassifier
    
dtgini=DecisionTreeClassifier(criterion="gini")
dtgini.fit(X_train,Y_train)
Y_pred2=dtgini.predict(X_test)
from sklearn.metrics import accuracy_score
acc_knn2=accuracy_score(Y_test,Y_pred2)
acc_knn2=round(acc_knn2*100,2)
    
dtentropy=DecisionTreeClassifier(criterion="entropy")
dtentropy.fit(X_train,Y_train)
Y_pred3=dtentropy.predict(X_test)
from sklearn.metrics import accuracy_score
acc_knn3=accuracy_score(Y_test,Y_pred3)
acc_knn3=round(acc_knn3*100,2)

if acc_knn3>acc_knn2:
    acc_knndt=acc_knn3
else:
    acc_knndt=acc_knn2


    
def nb():
    c= str(acc_knn4) + " %"
    m.showinfo(title="NB",message=c)
    print("accuracy score in NB is",acc_knn4,"%")
    print(nbayes.predict([[a,b,c,d]]))
    

##naive bayes
from sklearn.naive_bayes import GaussianNB
nbayes=GaussianNB()
nbayes.fit(X_train,Y_train)
Y_pred4=nbayes.predict(X_test)
from sklearn.metrics import accuracy_score
acc_knn4=accuracy_score(Y_test,Y_pred4)
acc_knn4=round(acc_knn4*100,2)


def display(a):
    if a[0]==0:
        s5.set("SETOSA")
    elif a[0]==1:
        s5.set("VERSICOLOR")
    else:
        s5.set("VERGINICA")
        


def submit():
    a=s1.get()
    b=s2.get()
    c=s3.get()
    d=s4.get()
    
    if acc_knn>=acc_knn1 and (acc_knn>=acc_knndt and acc_knn>=acc_knn4):
        print("KNN: ",K.predict([[a,b,c,d]]))
        display(K.predict([[a,b,c,d]]))
    elif acc_knn1>=acc_knndt and acc_knn1>=acc_knn4:
        print("LG: ",logreg.predict([[a,b,c,d]]))
        display(logreg.predict([[a,b,c,d]]))
    elif acc_knndt>=acc_knn4:
        if acc_knn3>=acc_knn2:
            print("DT GINI: ",dtgini.predict([[a,b,c,d]]))
            display(dtgini.predict([[a,b,c,d]]))
        else:
            print("DT ENTROPY: ",dtentropy.predict([[a,b,c,d]]))
            display(dtentropy.predict([[a,b,c,d]]))
    else:
        print("NB: ",nbayes.predict([[a,b,c,d]]))
        display(nbayes.predict([[a,b,c,d]]))


def reset():
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("Enter Data")

def compare():
    bottom=0
    # x-cordinate
    left=[1,2,3,4]

    #y-coordinate
    height=[acc_knn,acc_knn1,acc_knndt,acc_knn4]

    #label bar
    tick_label=['KNN','LR,','DT','NB']

    #plotting graph
    plt.bar(left,height,tick_label=tick_label,width=0.8,color=['red','green'])

    #labeling axis
    plt.xlabel=('MODEL')
    plt.ylabel=('ACCURACY')
    plt.title('FLOWER ML')
    plt.show()






s1=IntVar()
s2=IntVar()
s3=IntVar()
s4=IntVar()
s5=StringVar()

s1.set("")
s2.set("")
s3.set("")
s4.set("")
s5.set("Enter Data")
b1=Button(w,text="KNN",font=("arial",20,"bold"),width=8,command=knn)
b2=Button(w,text="LG",font=("arial",20,"bold"),width=8,command=lg)
b3=Button(w,text="DT",font=("arial",20,"bold"),width=8,command=dt)
b4=Button(w,text="NB",font=("arial",20,"bold"),width=8,command=nb)
b5=Button(w,text="COMPARE",font=("arial",20,"bold"),width=8,command=compare)
b6=Button(w,text="SUBMIT",font=("arial",20,"bold"),width=7,command=submit)
b7=Button(w,text="RESET",font=("arial",20,"bold"),width=7,command=reset)
l1=Label(w,text="ENTER FLOWER DATA",font=("arial",20,"bold"))
l2=Label(w,text="SL",font=("arial",20,"bold"))
l3=Label(w,text="SW",font=("arial",20,"bold"))
l4=Label(w,text="PL",font=("arial",20,"bold"))
l5=Label(w,text="PW",font=("arial",20,"bold"))
l6=Label(w,textvariable=s5,font=("arial",20,"bold"))
e1=Entry(w,font=("arial",20,"bold"),textvariable=s1)
e2=Entry(w,font=("arial",20,"bold"),textvariable=s2)
e3=Entry(w,font=("arial",20,"bold"),textvariable=s3)
e4=Entry(w,font=("arial",20,"bold"),textvariable=s4)
l1.grid(row=1,columnspan=5,ipadx=100)
b1.grid(row=2,column=1)
b2.grid(row=3,column=1)
b3.grid(row=4,column=1)
b4.grid(row=5,column=1)
b5.grid(row=6,column=1)
b6.grid(row=6,column=2)
b7.grid(row=6,column=3)
l2.grid(row=2,column=2)
l3.grid(row=3,column=2)
l4.grid(row=4,column=2)
l5.grid(row=5,column=2)
l6.grid(row=7,columnspan=5,ipadx=100)
e1.grid(row=2,column=3)
e2.grid(row=3,column=3)
e3.grid(row=4,column=3)
e4.grid(row=5,column=3)
w.mainloop()

