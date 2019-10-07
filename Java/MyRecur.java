import java.util.Scanner;

public class MyRecur{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter an Integer: ");
        int a = scan.nextInt();

        System.out.println("Sum is: "+sum(a));
    }
    static int sum(int n){
        if(n == 1)
            return 1;
        else
            return(n + sum(n-1));
    }
}