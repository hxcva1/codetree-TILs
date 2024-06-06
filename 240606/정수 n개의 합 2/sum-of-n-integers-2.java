import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        int ans = -100000000;
        Scanner sc = new Scanner(System.in);
        int n, k;
        n = sc.nextInt();
        k = sc.nextInt();
        int[] arr = new int[n];
        int[] prepix = new int[n];
        int num;
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        prepix[0] = arr[0];
        for(int i = 1; i < n; i++){
            prepix[i] = prepix[i-1] + arr[i];
        }
        for(int i = k-1; i < n; i++){

            if (i == k-1){
                ans = Math.max(ans, prepix[i]);
                continue;
            }
            ans = Math.max(ans, prepix[i] - prepix[i-k]);
        }
        System.out.println(ans);

    }
}