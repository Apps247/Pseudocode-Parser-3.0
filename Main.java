import java.util.Scanner;public class Main {
        public static void main(String[] args) {
        Scanner inputScanner = new Scanner(System.in);
String Name;
final var AdminName =  "Apps";
System.out.print("Enter your name: "); Name = inputScanner.nextLine();
System.out.println(Utility.stringCompare(Name, AdminName));
inputScanner.close();
}
}