
public class Conditional {

	public static void main(String[] args) {
		int dadAge = 46,momAge = 42;
		if(dadAge > momAge) {
			System.out.println("My dad is older than my mom!");
		}
		if(momAge > dadAge) {
			System.out.println("My dad is older than my mom!");
		}
		if(dadAge == momAge) {
			System.out.println("My dad and my mom are the same age");
		}
		// Elif does not exist
		
		// Else and an if does exist
		else {
			if(dadAge == momAge) {
				System.out.print("a");
			}
		}
	}

}
