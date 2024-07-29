// Zachary Wales
/*
An application class MaxMin4 that reads the input of five integers and
determines and prints the largest, the smallest and the mean of the group. Use
only the programming techniques that have been discussed in the class so far.
*/
// Due 5/18/23 BOP
import java.util.Scanner;
public class MaxMin4 {
	public static void main(String[] args) {
		Scanner input1 = new Scanner(System.in);
		
		
		// Inputs all 5 integers
		 System.out.print("Please enter in first number: ");
		 int integer1 = input1.nextInt();
		 System.out.print("Please enter in second number: ");
		 int integer2 = input1.nextInt();
		 System.out.print("Please enter in third number: ");
		 int integer3 = input1.nextInt();
		 System.out.print("Please enter in fourth number: ");
		 int integer4 = input1.nextInt();
		 System.out.print("Please enter in fifth number: ");
		 int integer5 = input1.nextInt();
		
		// Max and Min variables
		int max;
		int min;

		// Finds the max of the 5 integers, and sets it to max
		if (integer1 > integer2) {
			max = integer1;
		} else {
			max = integer2;
		}
		if (integer3 > max) {
			max = integer3;
		}
		if (integer4 > max) {
			max = integer4;
		}
		if (integer5 > max) {
			max = integer5;
		}

		// Finds the min of the 5 integers, and sets it to min
		if (integer1 < integer2) {
			min = integer1;
		} else {
			min = integer2;
		}
		if (integer3 < min) {
			min = integer3;
		}
		if (integer4 < min) {
			min = integer4;
		}
		if (integer5 < min) {
			min = integer5;
		}

		// Prints the max and min
		System.out.println("The largest number is: " + max);
		System.out.println("The smallest number is: " + min);

			// Makes a double of the integers
			double double1 = integer1;
			double double2 = integer2;
			double double3 = integer3;
			double double4 = integer4;
			double double5 = integer5;
			
			
			double mean = ((double1+double2+double3+double4+double5)/5);
			System.out.print("The mean of the 5 numbers is: "+mean);
			
			
		input1.close();
				}
			}

