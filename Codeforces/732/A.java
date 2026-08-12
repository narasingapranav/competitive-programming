import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int k = sc.nextInt();
        int r = sc.nextInt();

        for (int n = 1; n <= 10; n++) {
            int total = n * k;

            if (total % 10 == 0 || total % 10 == r) {
                System.out.println(n);
                break;
            }
        }
    }
}