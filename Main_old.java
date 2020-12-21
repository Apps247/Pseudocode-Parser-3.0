import java.util.Scanner;public class Main_old {
public static void main(String[] args) {
 Scanner inputScanner = new Scanner(System.in);
String Name;
int Age;
int MinimumAge;
MinimumAge = 10;
System.out.println("Hi");
System.out.print("Enter your Name: ");Name = inputScanner.nextLine();
System.out.print("Enter your Age: ");Age = inputScanner.nextInt();
if (Age >= MinimumAge)
{
System.out.println("Welcome, " + "" + Name);
} else {
System.out.println("Sorry, the minimum age is");
System.out.println(MinimumAge);
}
inputScanner.close();
}
}