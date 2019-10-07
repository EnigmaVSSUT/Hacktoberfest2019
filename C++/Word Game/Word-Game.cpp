			/* 	THE WORD-GAME 	   */

		   /*	     HEADER FILES' INCLUSION	    */

#include<fstream.h>
#include<conio.h>
#include<string.h>
#include<process.h>
#include<stdio.h>
#include<dos.h>
#include<ctype.h>

		   /*	     PROTOTYPE  DECLEARATION	    */

void play();                        // To play game
int tell(int);			    // To resirst the repeatation of words
void selection(int);                // User's selection (logic)
void about();                       // Introduction to the game
void credit();		            // About the developer
void winner();                      // Last 5 winners
void summery(int,int);              // Summery of words entered by players
void win_update(char Winner[25]);

			     /* CLASS */

			/*  FOR MAIN-MENU */

class Begin
{
  private:
	char option;

  public:
	void Menu()
	{

	    textcolor(1);
		cout<<"\n\n\t\t";
		cprintf("MAIN - MENU\n\n");
		cout<<"\n\t\tEnter any one of the following:\n"
		    <<"\n\t\t\'1\' to PLAY"
		    <<"\n\t\t\'2\' to know about the WORD-GAME"
		    <<"\n\t\t\'3\' for Credit"
		    <<"\n\t\t\'4\' for last 5 Winners"
		    <<"\n\t\t\'5\' to exit";

		cprintf("\n____________________\n");
		cout<<"\n\n\t\t";
	    textcolor(14);
		cprintf("*");
		cout<<" Please do not input any key other then 1, 2, 3, 4 "
		    <<"or 5 ";
		cprintf("*");
		cout<<"\n\t";
		cout<<"\n\n\t\t  Enter your choice: ";
		cin>>option;

	    selection(option);

	    clrscr();
	}

	void Choice(char a)
	{
	   if(a!='0')
		{
		   clrscr();
		   Menu();
		}
		else
		{
		   clrscr();
		   cout<<"\n\tThanks for giving a look.";
		   delay(2000);
		   exit(0);
		}
	}
}Main;

		   /*    GLOBAL  VARIABLES' DECLEARATION    */

char p1[80],p2[80],word[80][80];

		   /*		THE MAIN FUNCTION	    */

int main()
{
clrscr();

     textcolor(2);
	cout<<"\n\t\t";
	cprintf("WELCOME TO WORD-GAME");
	cout<<"\n\t       ";
	cprintf("_______________________");

     Main.Menu();
     return 0;
}

		      /* SWITCH FOR USER PREFERANCE (LOGIC) FOR MENU */

void selection(char a)
{
     do
     {
	switch(a)
	{
		case '1': play();
			break;
		case '2': about();
			break;
		case '3': credit();
			break;
		case '4': winner();
			break;
		case '5':{
			      clrscr();
			      cout<<"\n\tThanks for giving a look.";
			      delay(2000);
			      exit(0);
			 }
			 break;
		default: {
			      clrscr();
			      cout<<"\n\n\tSorry! It seems that you have "
				  <<"entered an incorrect key!!"
				  <<"\n\tWe should get exit...";
			      delay(4500);
			      exit(0);
			  }
	}
     }while(a!=4);
}
		       /* TO PLAY/START NEW GAME */

void play()
{
clrscr();
     int j,x,i,num=0;

		cout<<"\n\t";
	textcolor(5);
		cprintf("RULES:-");
		cout<<"\n\t\b";
		cprintf("_________\n");
		cout<<"\n\t1) Players must have to enter the word within "
		    <<"a fixed time-limit i.e. \n\t   30 seconds.";
		cout<<"\n\t2) One who leaves game first would be considered"
		    <<" defeated.";
		cout<<"\n\t3) Player can accept defeat by entering \'*\' "
		    <<"instead of the word.";
		cout<<"\n\t4) All words must be in small letter.";
		cout<<"\n\t\t\t\t";
		cprintf("____________________\n");
		cout<<"\n\n\n";

		cout<<"\tPress any key to proceed.";
		getch();
		clrscr();

	int e,d;
	textcolor(8);
		cprintf("\n\nLet\'s Begin:-\n");
		cout<<"\nName of first player: ";
		gets(p1); e=strlen(p1);for(d=0;d<e;d++)p1[d]=toupper(p1[d]);
		cout<<"Name of second player: ";
		gets(p2); e=strlen(p2);for(d=0;d<e;d++)p2[d]=toupper(p2[d]);
		cout<<"Number of words that each player\'d enter (max 40): ";
		cin>>j;
			if((j<1)||(j>40))
			{
			  clrscr();
			  cout<<"\n\tSorry!! Wrong input. Try next time.";
			  delay(2000);
			  exit(0);
			}

		cout<<"\t\t\t";
		cprintf("\n____________________\n");
		j*=2;

	textcolor(3);
		cout<<"\n\n\t";
		cprintf(p1);
		cout<<"! Enter first word: ";
		gets(word[0]);

		x=strlen(word[0]);
		   for(i=1;i<j;i++)
		   {
		      if(i%2==0)
		      { clrscr();
			cout<<"\n\n\t";
			cprintf(p1);
			cout<<"! Enter next word starting with"
			    <<" \'"<<word[i-1][x-1]<<"\', "
			    <<"\n\t(within 30 seconds) : \t\t\t";
			gets(word[i]);

			  if((word[i][0]!=word[i-1][x-1])||(tell(i)==0))
			  {
			      do
			      {
				if(word[i][0]=='*')
				{
				 cout<<"\n\t";
				 cprintf("__________________________________");
				 cprintf("___________________________________");
				  cout<<"\n\t\t\a";cprintf(p2);
				  cout<<"! Your opponent has knelt in front"
				      <<" of you! You Won!!!";
				  goto MATCH;
				}
				else
				{
				  cout<<"\n\tWord should start with \'"
				      <<word[i-1][x-1]<<"\' & should not"
				      <<" be repeted! \n\t";
	textcolor(8);
				  cprintf("Either enter \'*\' if you have no");
				  cprintf(" words, or enter the word again: ");
				  gets(word[i]);
				}

				if(word[i][0]==word[i-1][x-1])
				break;
				num++;
			      }while(num!=2);
			  }

			  if(num==2)
			  {
	textcolor(3);
			      cout<<"\n\t";
			      cprintf("___________________________________");
			      cprintf("__________________________________\n");
			      cout<<"\t\tSorry! "
				  <<"You\'ve crossed limit. You are lost!!";
			      cout<<"\n\t\a";
			      cprintf(p2);
			      cout<<"! You won, "
				  <<"as you are a living dictionary!!";
			      goto MATCH;
			  }
			  else
			  num=0;
		      }

		      else
		      {
			cout<<"\n\n\t";
			cprintf(p2);
			cout<<"! Enter next word starting with \'"
			    <<word[i-1][x-1]
			    <<"\', \n\t(within 30 seconds) : \t\t\t";
			gets(word[i]);

			  if((word[i][0]!=word[i-1][x-1])||(tell(i)==0))
			  {
			      do
			      {
				if(word[i][0]=='*')
				{
				 cout<<"\n\t";
				 cprintf("__________________________________");
				 cprintf("___________________________________");
				  cout<<"\n\t\t\a";cprintf(p1);
				  cout<<"! Your opponent has knelt in front"
				      <<" of you! You Won!!!";
				  goto MATCH;
				}
				else
				{
				  cout<<"\n\tWord should start with \'"
				      <<word[i-1][x-1]<<"\' & should not"
				      <<" be repeated!\n\t";
	textcolor(8);
				  cprintf("Either enter \'*\' if you have no");
				  cprintf(" words, or enter the word again: ");
				  gets(word[i]);
				}
				if(word[i][0]==word[i-1][x-1])
				break;
				num++;
			      }while(num!=2);
			  }

			  if(num==2)
			  {
	textcolor(3);
			     cout<<"\n\t";
			     cprintf("___________________________________");
			     cprintf("__________________________________\n");
			      cout<<"\t\t\aSorry! "
				  <<"You\'ve crossed limit. You are lost!!";
			      cout<<"\n\t";cprintf(p1);cout<<"! You won, "
				  <<"as you are a living dictionary!!";
				 goto MATCH;
			  }
			  else
			  num=0;
		      }

		      x=strlen(word[i]);
		   }

		MATCH:

		   if(i==j)
		   {
		      cout<<"\n\t\a";
		      cprintf("___________________________________");
		      cprintf("__________________________________\n");
		      cout<<"\n\n\t";
		      cprintf("How great players you are! ");
		      cprintf("The match is draw!!!");
		      cout<<"\t";
		   }
		   else
		   {
		      cout<<"\n\n\t";
			  if(i%2==0)
			  {
			      cprintf("Winner is: ");cprintf(p2);
			      win_update(p2);
			  }
			  else
			  {
			      cprintf("Winner is: ");cprintf(p1);
			      win_update(p1);
			  }
		   }

     int copy=j;
     j=i;

	cout<<"\n\n\n\t";
	char choice;
	   textcolor(10);
		cprintf("*");
		cout<<" Enter any key to go back to Main Menu, \'s\' "
		    <<"to see the summery \n\t  or \'0\' to get exit.\n";
		cout<<"\n\t  Enter Your choice: ";
		cin>>choice;

		switch(choice)
		   {
		      case '0': {
				   clrscr();
				   cout<<"\n\tThanks for giving a look.";
				   delay(2000);
				   exit(0);
				}
				break;
		      case 's': summery(j,copy);
				break;
		      case 'S': summery(j,copy);
				break;
		      default : {
				   clrscr();
				   Main.Menu();
				}
		   }

}

		 /*     To resist the words from being repeated    */

int tell(int i)
{
 int x=1;

 for(int j=0;j<i;j++)
 {
   if(strcmpi(word[j],word[i])==0)
   {
    x=0;
    break;
   }
 }

 return x;
}
			 /* INTRODUCTION TO WORD-GAME
			      & HOW TO PLAY  */

void about()
{
clrscr();
     char choice;
     textcolor(4);
	cout<<"\n\t";
	cprintf("WORD-GAME");
	cout<<"\n\t\b";
	cprintf("____________\n");
	cout<<"\n\t    This game is for two players, that tests your "
	    <<"vocabulary and "
	    <<"\n\tstrengthens your command on the words of English "
	    <<"language."
	    <<"\n\tIt would also improve your grip on this language.";
	cout<<"\n\t    It has a user friendly interface, and trust "
	    <<"you would really "
	    <<"\n\tlike this Game. It\'d be cool to call it- "
	    <<"\"ENGLISH-ANTAKSHRI\"";

	cout<<"\n\n\t";
	cprintf("HOW TO PLAY");
	cout<<"\n\t1) Enter Names of the players and no. of words to be "
	    <<"entered."
	    <<"\n\t2) Now, one player would enter the first word."
	    <<"\n\t3) Then other\'d enter new word starting from last "
	    <<"word\'s last letter."
	    <<"\n\t4) In this way the loop would continue until players "
	    <<"would not enter \n\t"
	    <<"   complete no. of words or anyone would not loose the game"
	    <<"\n\t5) Every player would get 3 chances to correct his/her "
	    <<"entry.";
	cout<<"\n\n\t     So, what are you waiting for! "
	    <<"Come-on get your friend \n\tnow and let\'s play it!!";
	cprintf("\n____________________\n");

	cout<<"\n\t";
     textcolor(14);
	cprintf("*");
	cout<<" Enter any key to go back to Main Menu or "
	    <<"\'0\' to get exit.\n";
	cout<<"\t  Enter Your choice: ";
	cin>>choice;

	    Main.Choice(choice);
}
		      /* ABOUT THE DEVELOPER */

void credit()
{
clrscr();
     char choice;
     textcolor(5);
	cout<<"\n\n\t  This game is independently developed by ";
	cprintf("\"Ravi Prakash\"");
	cout<<".\n\n\t";

	cprintf("*");
	cout<<" Enter any key to go back to Main Menu or "
	    <<"\'0\' to get exit.";
	cout<<"\n\t  Enter Your choice: ";
	cin>>choice;

	    Main.Choice(choice);
}
		      /* TO DISPLAY RECENT 5 WINNERS' NAME */

void winner()
{
clrscr();
     char choice;
     textcolor(6);
	cout<<"\n\t";
	cprintf("WINNERS");
	cprintf("\n\b\b\b\b\b\b\b\b\b____________");
	cout<<"\n\n\t";
		char ch,winners[25];
		fstream win_data;
		win_data.open("winner.txt",ios::in);
		if(!win_data)
		{  win_data.close();
		   cout<<"File does not exist!!";
		   textcolor(14);
			cout<<"\n\n ";
			cprintf("*");
			cout<<" Enter any key to go back to Main Menu or "
			    <<"\'0\' to get exit.";
			cout<<"\n   Enter Your choice: ";
			cin>>choice;
		     if(choice!='0')
			{
			  clrscr();
			  Main.Menu();
			}
		     else
			{
			  clrscr();
			  cout<<"\n\tThanks for giving a look.";
			  delay(2000);
			  exit(0);
			}
		}
		else
		{
			while(!win_data.eof())
			{
				win_data.getline(winners,25);
				win_data.get(ch);
				cout<<"\n\t\t"<<winners;
			}
		}
		win_data.close();



     cout<<"\n\n\t";
     textcolor(14);
	cprintf("*");
	cout<<" Enter any key to go back to Main Menu or "
	    <<"\'0\' to get exit.";
	cout<<"\n\t Enter Your choice: ";
	cin>>choice;

	    Main.Choice(choice);
}
			   /* TO SUMMERISE THE GAME'S RESULT */

void summery(int j, int copy)
{
clrscr();
     cout<<"\n\n\t";
     textcolor(18);
	cprintf("Words entered respectivally:-");
	cout<<"\n\n";
		for(int i=0;i<j;i++)
		{
		   if(i%2==0)
		   {
		      cout<<"\tBy "<<p1<<": ";
		      puts(word[i]);
		   }
		   else
		   {
		      cout<<"\tBy "<<p2<<": ";
		      puts(word[i]);
		      cout<<"\n";
		   }
		}
	cout<<"\n\t";
     textcolor(15);
	cprintf("Result:-\n");
     textcolor(9+BLINK);
		if(i==copy)
		{
		   cprintf("Match Draw!!");
		   goto Place;
		}
		else
		cout<<"\n\t\t";
		cprintf("Winner is: ");
		{
		   if(i%2==0)
		      cprintf(p2);
		   else
		      cprintf(p1);
		}

     Place:

	cout<<"\n\n\t";
	cprintf("*");
	cout<<" Enter any key to go back to Main Menu or "
	    <<"\'0\' to get exit.\n";
	char choice;
	cout<<"\t  Enter Your choice: ";
	cin>>choice;

	    Main.Choice(choice);

}

		   /*TO UPDATE WINNER"S FILE*/

void win_update(char Winner[25])
{
	char ch,winners[25];
	int counter=1;
	fstream New("winner.txt",ios::noreplace);
	  if(New)
	   {
	     New<<Winner<<"\n";
	     New.close();
	   }
	  else
	   {
	     fstream backup("backup.txt",ios::out);
	     backup<<Winner<<"\n\t";
	     fstream old("winner.txt",ios::in);
	     while(!old.eof())
	     {
		old.get(winners,25);
		old.get(ch);
			{   counter++;
			    backup<<winners<<"\n";
			}
		if(counter==5)
		break;
	     }
	   old.close();
	   backup.close();
		remove("winner.txt");
		rename("backup.txt","winner.txt");

	   }
}
				/* THE END */
