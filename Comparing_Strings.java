import java.util.Scanner;


public class ComparadorDeStrings {
	
	
	public void reverseString() {
		this.reverseString();
	}
	
	public static void main(String[] args) {
		
		
		System.out.println("Imprima duas palavras separadas por espaço: \n");
		
		Scanner input = new Scanner(System.in);
		String first = input.nextLine();		
		String second = input.nextLine();
		
		StringBuffer fr = new StringBuffer(first);
		StringBuffer se = new StringBuffer(second);
		
		fr.reverse();
		se.reverse();
		
		String new1 = fr.toString();
		String new2 = se.toString();
		
		input.close();

		System.out.println("Comparando " + first + " e " + second + " : " + (first.equals(new2)));
		System.out.println();
		
		
	}
}	
