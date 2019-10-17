import java.util.*;
class factorial{
	static int factorial(int n){
		if(n==1)
			return 1;
		else
			return (n*factorial(n-1));
		
	}
	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		int n;
		n=s.nextInt();
		int result=factorial(n);
		System.out.println("Factorial of "+n+" is "+result);

	}
}
