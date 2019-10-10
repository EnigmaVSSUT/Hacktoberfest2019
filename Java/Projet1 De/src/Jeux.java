/*import java.util.Scanner;

public class Jeux {
    public static void main (String [] args){
   Scanner sc = new Scanner(System.in);
   int j,t,i,k,d,s;
   String Pseudo;
   System.out.println("Donner le nombre des joueurs:");
   j=sc.nextInt();
   System.out.println("Donner le nombre des tours:");
    t=sc.nextInt(); 
    Joueur T1[] = new Joueur[j];
    for(i=0;i<j;i++) {
    	  System.out.println("le Pseudo de joueur" +(i+1) +":");
    	 Pseudo=sc.next(); 
    	 T1[i]= new Joueur(Pseudo);
    }
    for(i=0;i<t;i++) {
  	  System.out.println("*Tour" +(i+1) +":");
  	 for(k=0;k<j;k++) {
  		d = De.Lancerde();
  		T1[k].score(d);
  	  	System.out.println(" Pseudo:" +T1[k].getPseudo() +  "\n Score :" +T1[k].getScore()); // we can add point 

  	 }
  }
   s=T1[0].getScore();
   for(i=0;i<j;i++) {
 	 if(T1[i].getScore()>s)
 		 s=T1[i].getScore();
 }
    
   for(i=0;i<j;i++) {
	 	 if(T1[i].getScore()==s)
	 	System.out.println(T1[i].getPseudo() + " a gangé ");
	 }   
        }
}
      
      
*/