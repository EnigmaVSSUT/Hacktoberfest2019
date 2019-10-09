"""
Created on Tue Sep  4 22:40:23 2018
@author: rockngsho
"""
import random
movies = ['interstellar', 'matrix', 'avengers', 'x men', 'batman', 'inception', 'shutter island', 'the prestige', 'incredibles', 'mad max fury road', 'justice league']

def create_question(movie):
    '''
    This will create question from movie name
    @param movie(str) : Name of the movie
    @return (str)     : Question 
    '''
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn="".join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    '''
    Search for the letter in the movie name
    @param letter(char) : Letter to be searched
    @param movie(str)   : Movie name in which to be searched for
    @return(bool)       : Present or not
    '''
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True

def unlock(qn,movie,letter):
    '''
    This will revail the movie name
    @param qn(str)      : Question string
    @param movie(str)   : Actual movie name
    @param letter(char) : Letter said by the player
    @return(str)        : New question with added char
    '''
    ref=list(movie)
    qn_list=list(qn)
    n=len(movie)
    temp=[];
    temp=[]
    for i in range(n):
        if ref[i]==letter:
            temp.append(letter)
        else:
            temp.append(qn_list[i])
    qn_new="".join(str(x) for x in temp)   
    return qn_new

def play():
    '''
    Kind of encapsulate all the functions to start the game
    @param  : None
    @return : None
    '''
    p1name=input("player 1 please enter your name:")
    p2name=input("player 2 please enter your name:")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while(willing):
        if(turn%2==0):
            #player 1
            print(p1name, "its your turn")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            modified_qn=qn
            print(qn)
            
            not_said=True
            while(not_said):
                letter=input("Your letter: ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("press 1 to guess the movie or 2 to unlock another character"))
                    if d==1:
                        ans=input("Your answer: ")
                        if ans==picked_movie:
                            pp1=pp1+1
                            print("correct")
                            not_said=False
                            print(p1name, "your score is ", pp1)
                        else:
                            print("wrong answer try again")
                else:
                    print(letter, "not found")
            c=int(input("press 1 to continue 0 to quit"))
            if c==0:
                print(p1, "your score: ",pp1)
                print(p2, "your score: ",pp2)
                print("thank you!!!!")
                break
        else:
            #player2
            print(p2name, "its your turn")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            modified_qn=qn
            print(qn)
            
            not_said=True
            while(not_said):
                letter=input("Your letter: ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("press 1 to guess the movie or 2 to unlock another character"))
                    if d==1:
                        ans=input("Your answer")
                        if ans==picked_movie:
                            pp2=pp2+1
                            print("correct")
                            not_said=False
                            print(p2name, "your score is ", pp2)
                        else:
                            print("wrong answer try again")
                else:
                    print(letter, "not found")
            c=int(input("press 1 to continue 0 to quit"))
            if c==0:
                print(p1name, "your score: ",pp1)
                print(p2name, "your score: ",pp2)
                print("thank you!!!!")
                break
        turn=turn+1
play()