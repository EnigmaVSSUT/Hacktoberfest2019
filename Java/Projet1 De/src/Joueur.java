
public class Joueur {
 private String Pseudo;
private static   int score  ;
public Joueur(String Nom) {
	this.Nom=Nom;
	this.score=score;
}

public String getNom ()
{
	return Nom;
}
public void setNom(String Nom)
{
	this.Nom = Nom;
}
public int getScore ()
{
	return score;
}
public void setscore (int score)
{
	this.score = score;
}
public static int score (int point) {
	return score+=point;
}
}
