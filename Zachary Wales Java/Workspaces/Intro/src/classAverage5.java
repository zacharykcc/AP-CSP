/*
Zachary Wales, Period 1

An application that takes in 10 grades for a quiz and tells the mean
  
Due 5/22/2023
*/

import java.util.Scanner;

public class classAverage5 {
	public static void main(String[] args) {
		// Creates input1 scanner for input
		Scanner input1 = new Scanner(System.in);

		int grade = 0;
		int sum = 0;
		int counter = 0;
		
		// And = &&, Or = ||
		
		
		// Creates a while loop for all of the grades
		while(counter<10) {
			// Sequences the counter
			counter++;
			// Prints the grade request
			System.out.print("Grade "+counter+": ");
			// Gets input
			grade = input1.nextInt();
			// Sanitizes the input
			while(grade > 100 || grade < 0) {
				System.out.print("That grade is unacceptable. Please enter a grade 0-100 : ");
				grade = input1.nextInt();
			}
			// Adds the grades to sum
			sum += grade;
		}
		// Tells the mean of the 10 numbers
		System.out.print("The mean of the 10 numbers is: "+(sum/10.0));
		
		// Closes the input
		input1.close();
	}
}
