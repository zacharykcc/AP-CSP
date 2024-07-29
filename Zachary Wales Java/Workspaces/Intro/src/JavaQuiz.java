
// Didn't have
import java.util.Scanner;


public class JavaQuiz {

	public static void main(String[] args) {
		Scanner grabber = new Scanner(System.in);
		System.out.print("What is the desired max value? ");
		int maxVal = grabber.nextInt();
		int counter = 0;
		int numNums = (maxVal/2);
		
		while(counter != numNums) {
			counter++;
			System.out.print((counter*2)+ " ");
		}
		grabber.close();
	}

}
