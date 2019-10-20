import java.util.*;
class reverse_num{
	public static void main(String[] args) {
		int rem=0,rev=0;
		System.out.print("Enter number: ");
		Scanner s=new Scanner(System.in);
		int n=s.nextInt();
		while(n!=0){
			rem=n%10;
			rev = (rev*10)+(rem);
			n=n/10;
		}
		System.out.println("Reverse number is: "+rev);
	}
}
