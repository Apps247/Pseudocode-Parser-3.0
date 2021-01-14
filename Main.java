import java.util.Scanner;public class Main {
        public static void main(String[] args) {
        Scanner inputScanner = new Scanner(System.in);
char Direction;
System.out.print("Enter the direction Symbol: "); Direction = inputScanner.next().charAt(0);
switch (Direction) {
case 'N'  : System.out.println("North");break;
case 'S'  : System.out.println("South");break;
case 'E'  : System.out.println("East");break;
case 'W'  : System.out.println("West");break;
}
inputScanner.close();
}
}