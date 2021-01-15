import java.util.Scanner;public class Main {
        public static void main(String[] args) {
        Scanner inputScanner = new Scanner(System.in);
String Username;
String Password;
final var Correct_Username =  "Apps247";
final var Correct_Password =  "yoyothrower247";
System.out.print("Welcome. Please enter your username:\n"); Username = inputScanner.nextLine();
if (Utility.stringCompare(Correct_Username, Username))
{
System.out.print("Password:\n"); Password = inputScanner.nextLine();
while (! Utility.stringCompare(Password, Correct_Password)) {
System.out.print("Password:\n"); Password = inputScanner.nextLine();
}
} else {
System.out.println("Sorry, your username was not recognized");
}
inputScanner.close();
}
}