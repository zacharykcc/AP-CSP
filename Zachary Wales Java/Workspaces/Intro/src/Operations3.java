// Zachary Wales
// Period 1
/* An application will calculate the sum, difference, product, quotient, and modulus
of the two numbers and will display them and a greeting to the user to the
screen on separate lines.
*/

//Imports Scanner
import java.util.Scanner;


public class Operations3 {
	public static void main(String[] args) {
		//Starts scanner 
		Scanner input1 = new Scanner(System.in);
		 
		//Asks what is the users name and gets the input
		System.out.print("What is your name? ");
		 String name = input1.nextLine();
		 
		 // Prints the user's name
		 System.out.println("Hello "+name);
		 
		 
		 //Asks and inputs integer 1
		 System.out.print("Please enter in first number: ");
		 int integer1 = input1.nextInt();
		 
		//Asks and inputs integer 1
		 System.out.print("Please enter in second number: ");
		 int integer2 = input1.nextInt();
		 
		 
		 
		 //Maths
		 	//Addition
		 		System.out.println(integer1+" + "+integer2+" = "+(integer1+integer2));
		 	//Subtraction
		 		System.out.println(integer1+" - "+integer2+" = "+(integer1-integer2));
		 	//Multiplication
		 		System.out.println(integer1+" * "+integer2+" = "+(integer1*integer2));
		 	// Division
		 		System.out.println(integer1+" ÷ "+integer2+" = "+(integer1/integer2));
		 	//Modulus
		 		System.out.println(integer1+" mod "+integer2+" = "+(integer1%integer2));
		 
		 		
		 		//Closes the input1 scanner
		 input1.close();
		
		
		
	}
}
