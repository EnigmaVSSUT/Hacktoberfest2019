import java.util.*;
public class fibonacci
{
	static int n1=0,n2=1,n3;
	static void FiboByRecursion(int n)
	{
	  if(n>0)
	  {
		n3=n1+n2;
		n1=n2;
		n2=n3;
		System.out.print(", "+ n3);
		FiboByRecursion(n-1);
	  }
    }

public static void main(String[] args) 
	{
		Scanner s=new Scanner(System.in);
		System.out.println("Enter a number: ");
		int n=s.nextInt();

		System.out.print( "fibonacci series is: " +n1 + ", " + n2);

		FiboByRecursion(n-2);
	}
}
