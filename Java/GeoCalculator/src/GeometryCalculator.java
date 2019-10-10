import java.util.Scanner;

public class GeometryCalculator {

	public static void main(String[] args) {
		int choice;
		float s;//side
		float ba;//base
		float l;//length
		float b;//breadth
		float h;//height
		float a;//area
		float r;//radius
		Scanner sc = new Scanner(System.in);
		System.out.println("1 --> Circle\n2 --> Rectangle\n3 --> Triangle\n4 --> Square\n");
		System.out.println("Enter a number:");
		choice = sc.nextInt();
		switch (choice) {
		case 1:
			System.out.println("Enter the radius:");
			r = sc.nextFloat();
			a = (float) (3.142 * r * r);
			System.out.println("Area of a circle =" + a);
			break;
		case 2:
			System.out.println("Enter the breadth and length:");
			b = sc.nextFloat();
			l = sc.nextFloat();
			a = (float) (b * l);
			System.out.println("Area of a Reactangle =" + a);
			break;
		case 3:
			System.out.println("Enter the base and height:");
			ba = sc.nextFloat();
			h = sc.nextFloat();
			a = (float) (0.5 * ba * h);
			System.out.println("Area of a Triangle =" + a);
			break;
		case 4:
			System.out.println("Enter the side:");
			s = sc.nextFloat();
			a = (float) (s * s);
			System.out.println("Area of a Square=" + a);
			break;
		default:
			System.out.println("Error ");
			break;
		}
	}
}
