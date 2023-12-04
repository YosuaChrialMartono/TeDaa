package TE_2;

import java.util.Arrays;

public class DPPartition {

    static boolean findPartition(int arr[], int n) {
        int sum = Arrays.stream(arr).sum();

        if (sum % 2 != 0) {
            System.out.println("Cannot be divided into two subsets of equal sum");
            return false;
        }

        int partitionSum = sum / 2;
        boolean part[][] = new boolean[partitionSum + 1][n + 1];

        // Initialization
        for (int i = 0; i <= n; i++) {
            part[0][i] = true;
        }

        for (int i = 1; i <= partitionSum; i++) {
            part[i][0] = false;
        }

        // Fill the part array
        for (int i = 1; i <= partitionSum; i++) {
            for (int j = 1; j <= n; j++) {
                part[i][j] = part[i][j - 1];
                if (i >= arr[j - 1]) {
                    part[i][j] = part[i][j] || part[i - arr[j - 1]][j - 1];
                }
            }
        }

        // Print the partitioned sets
        printPartitionSets(arr, part, n);

        return part[partitionSum][n];
    }

    static void printPartitionSets(int arr[], boolean part[][], int n) {
        int partitionSum = part.length - 1;
        int i = partitionSum;
        int j = n;

        if (!part[partitionSum][n]) {
            System.out.println("No valid partition found.");
            return;
        }

        System.out.print("Partition Set 1: [");
        boolean isFirstElementPrinted = false;  // Added flag
        boolean[] isInSet1 = new boolean[n + 1];  // Track elements in Set 1

        while (i > 0 && j > 0) {
            while (j > 0 && !part[i][j]) {
                j--;  // Skip elements that are not part of the partition
            }

            if (j <= 0) {
                break;  // Break if we reached the end of the array
            }

            if (isFirstElementPrinted) {
                System.out.print(", ");
            }
            System.out.print(arr[j - 1]);
            isInSet1[j] = true;  // Mark the element as in Set 1
            isFirstElementPrinted = true;
            i -= arr[j - 1];
            j--;
        }
        System.out.println("]");

        System.out.print("Partition Set 2: [");
        for (int k = 0; k < n; k++) {
            if (!isInSet1[k + 1]) {
                System.out.print(arr[k]);
                if (k < n - 1) {
                    System.out.print(", ");
                }
            }
        }
        System.out.println("]");
    }

    public static void main(String[] args) {
        int arr[] = {1, 2, 3, 4, 5, 6, 7,8, 9,10, 11, 12};
        int n = arr.length;

        if (findPartition(arr, n)) {
            System.out.println("Can be divided into two subsets of equal sum");
        } else {
            System.out.println("Cannot be divided into two subsets of equal sum");
        }
    }
}
