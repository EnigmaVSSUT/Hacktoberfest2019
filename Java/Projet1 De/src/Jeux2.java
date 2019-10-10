import java.util.Scanner;
import java.util.ArrayList;

public class Jeux2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Joueur> ja = new ArrayList<Joueur>();
		System.out.println("Donner le nombre des joueurs:");
		int j = sc.nextInt();
		System.out.println("Donner le nombre des tours:");
		int t = sc.nextInt();
		for (int i = 0; i < j; i++) {
			System.out.println("le Pseudo de joueur" + (i + 1) + ":");
			String Nom = sc.next();
			ja.add(new Joueur(Nom));

		}
		for (int i = 0; i < t; i++) {
			System.out.println("*Tour" + (i + 1) + ":");
			for (int k = 0; k < j; k++) {
				int d = De.Lancerde();
				ja.get(k).score(d);
				System.out.println(" Pseudo:" + ja.get(k).getPseudo() + "\n Score :" + ja.get(k).getScore()); // we can
																												// add
																												// point
			}
		}
		int s = ja.get(0).getScore();
		for (int i = 0; i < j; i++) {
			if (ja.get(i).getScore() > s)
				s = ja.get(i).getScore();

		}
		String w = null;
		for (int i = 0; i < j; i++) {
			if (ja.get(i).getScore() == s)
				w = ja.get(i).getPseudo();

		}
		System.out.println(w + " a gangé");
	}

}
