import java.util.Scanner;public class Main {
        public static void main(String[] args) {
        Scanner inputScanner = new Scanner(System.in);
String Name;
long Age;
final var MinimumAge =  15;
System.out.print("Enter your name: "); Name = inputScanner.nextLine();
System.out.print("Enter your age: "); Age = inputScanner.nextLong();
if (Age >= MinimumAge);
{
System.out.println("Welcome, " + "" + Name);
ELSE;
System.out.println("Sorry, the minimum age is " + "" + MinimumAge);
}
inputScanner.close();
}
}