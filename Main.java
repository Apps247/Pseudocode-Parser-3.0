import java.util.Scanner;public class Main {
        public static void main(String[] args) {
        Scanner inputScanner = new Scanner(System.in);
String Name;
int Age;
final var MinimumAge =  15;
System.out.print("Enter your name: "); Name = inputScanner.nextLine();
System.out.print("Enter your age: "); Age = inputScanner.nextInt();
System.out.println("Hi " + "" + Age);
System.out.println(Age + Age);
System.out.println(Age + "" + Age);
System.out.println(Age - MinimumAge);
inputScanner.close();
}
}