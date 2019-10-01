############CLASSIFICATION OF IRIS FLOWER USING MACHINE LEARNING################

##FOR HANDLING THE WARNINGS
import warnings
warnings.simplefilter(action='ignore')

##FOR PLOTING THE GRAPH
import matplotlib.pyplot as plt

##LOAD IRIS DATA TO PROGRAM
from sklearn.datasets import load_iris
iris=load_iris()
print(iris)


##separating input and output
X=iris.data ##numpy array
Y=iris.target  ##numpy array
print(X) 
print(Y)  


##split dataset for training and testing
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)


'''print(X_train.shape)  #(120,4)
print(Y_train.shape)  #(120,)
print(X_test.shape)   #(30,4)
print(Y_test.shape)   #(30,)'''

acc_knn=0
acc_lg=0
acc_dtgini=0
acc_nb=0

###CREATE A MODEL  
##K Nearest Neighbors Algorithm (KNN)

from sklearn.neighbors import KNeighborsClassifier
K=KNeighborsClassifier(n_neighbors=5)
  
##Train the model by training dataset
K.fit(X_train,Y_train)
 
##test the model by testing data
Y_pred=K.predict(X_test)

##find accuracy of KNN
from sklearn.metrics import accuracy_score
acc_knn=accuracy_score(Y_test,Y_pred)
acc_knn=round(acc_knn*100,2)


##Logistic Regression (LR)

from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()

##Train the model by training dataset
logreg.fit(X_train,Y_train)

##test the model by testing data
Y_pred1=logreg.predict(X_test)

##find accuracy of LR
acc_lg=accuracy_score(Y_test,Y_pred1)
acc_lg=round(acc_lg*100,2)

###Decision Tree
from sklearn.tree import DecisionTreeClassifier

##DT GINI
dtgini=DecisionTreeClassifier(criterion="gini")

##Train the model by training dataset
dtgini.fit(X_train,Y_train)

##test the model by testing data
Y_pred2=dtgini.predict(X_test)

##find accuracy  of DT GINI
acc_dtgini=accuracy_score(Y_test,Y_pred2)
acc_dtgini=round(acc_dtgini*100,2)
    
##DT ENTROPY
dtentropy=DecisionTreeClassifier(criterion="entropy")

##Train the model by training dataset
dtentropy.fit(X_train,Y_train)

##test the model by testing data
Y_pred3=dtentropy.predict(X_test)

##find accuracy  of DT ENTROPY
acc_dtentropy=accuracy_score(Y_test,Y_pred3)
acc_dtentropy=round(acc_dtentropy*100,2)

##GETTING THE ACCURACY MAX (DT GINI OR DT ENTROPY)
if acc_dtentropy>acc_dtgini:
    acc_knndt=acc_dtentropy
else:
    acc_knndt=acc_dtgini



##naive bayes
from sklearn.naive_bayes import GaussianNB
nbayes=GaussianNB()

##Train the model by training dataset
nbayes.fit(X_train,Y_train)

##test the model by testing data
Y_pred4=nbayes.predict(X_test)

##find accuracy  of DT ENTROPY
acc_nb=accuracy_score(Y_test,Y_pred4)
acc_nb=round(acc_nb*100,2)

##CALLING K-NEAREST NEIGHBORS MODEL
def knn():

    c="Accuracy score in KNN model is "+str(acc_knn) + " %."
    m.showinfo(title="KNN",message=c)    
    print("accuracy score in KNN is",acc_knn,"%")

##CALLING LOGISTIC REASON MODEL
def lg():
    
    c="Accuracy score in LG model is "+str(acc_lg) + " %,"
    m.showinfo(title="LR",message=c)
    print("accuracy score in LG is",acc_lg,"%")

##CALLING DESICION TREE MODEL (DT GINI AND DT ENTROPY)
def dt():
    
    c="Accuracy score in DT GINI model is "+ str(acc_dtgini) + " %."
    c=c + "\n Accuracy score in DT ENTROPY model is "+ str(acc_dtentropy) + " %."
    m.showinfo(title="DT ENTROPY",message=c)
    print("accuracy score in DT GINI is",acc_dtgini,"%")
    print("accuracy score in DT ENTROPY is",acc_dtentropy,"%")

##CALLING NAIVE BAYES MODEL
def nb():
    
    c="Accuracy score in NB model is "+ str(acc_nb) + " %"
    m.showinfo(title="NB",message=c)
    print("accuracy score in NB is",acc_nb,"%")

##DISPLAYS THE FLOWER TYPE
def display(b,a):
    
    if a[0]==0:
        s5.set(b+" SETOSA")
    elif a[0]==1:
        s5.set(b+" VERSICOLOR")
    else:
        s5.set(b+" VERGINICA")

##HANDELS THE USER INPUTS AND FINDS THE FLOWER 
def submit():
    
    ##HANDLES THE ERROR OCCURED DUE TO NOT ENTERING THE DATA OF SL,SW,PL,PW.
    try:
        a=s1.get()
        b=s2.get()
        c=s3.get()
        d=s4.get()

        ##FINDS THE BEST MODEL
        model=[acc_knn,acc_lg,acc_knndt,acc_nb]
        x=max(model)
        y=model.index(x)
        if y==0:
            display("KNN:",K.predict([[a,b,c,d]]))
        elif y==1:
            display("LG:",logreg.predict([[a,b,c,d]]))
        elif y==2:
            if acc_dtentropy>=acc_dtgini:
                display("DT GINI:",dtgini.predict([[a,b,c,d]]))
            else:
                display("DT ENTROPY:",dtentropy.predict([[a,b,c,d]]))
        else:
            display("NB:",nbayes.predict([[a,b,c,d]]))
        
    except:
        m.showinfo(title="ERROR",message="Enter data correctly")

##RESETS THE GUI 
def reset():

    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("Enter Data")

##COMPARES ALL THE MODEL AND SHOWS THE GRAPH BETWEEN MODELS-VS-ACCURACY
def compare():

    bottom=0

    #y-coordinate
    model=[acc_knn,acc_lg,acc_knndt,acc_nb]

    #x-coordinate
    label=['KNN','LR,','DT','NB']
    
    ##CALCULATING THE MODEL WITH MAX ACCURACY.
    x=max(model)
    y=model.index(x)
    if y==0:
        v=m.askyesno(title="KNN",message="KNN has the best accuracy. \n Wanna see graph.")
    elif y==1:
        v=m.askyesno(title="LR",message="LR has the best accuracy. \n Wanna see graph.")
    elif y==2:
        v=m.askyesno(title="DT",message="DT has the best accuracy. \n Wanna see graph.")
    else:
        v=m.askyesno(title="NB",message="NB has the best accuracy. \n Wantna see graph.")    


    #plotting graph
    plt.bar(label,model,width=0.8,color=['red','green'])

    #labeling axis
    plt.xlabel=('MODEL')
    plt.ylabel=('ACCURACY')
    plt.title('IRIS FLOWER ML')
    if v==True:
        plt.show()

##GUI
from tkinter import *
import tkinter.messagebox as m
w=Tk()

##SETTING THE VARIABLE FOR THE SL,SW,PL,PW.
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

##BUILDING THE GUI
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

##POSITIONING THE ICONS OF GUI IN CORRECT POSITION
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

