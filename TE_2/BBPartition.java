package TE_2;

import java.util.Arrays;

public class BBPartition {
    public static void main(String[] args) {
        // Example usage
        int[] values = {1, 2, 3, 4};
        boolean[] testAssignment = new boolean[values.length];
        boolean[] bestAssignment = new boolean[values.length];
        int totalValue = Arrays.stream(values).sum();
        int unassignedValue = totalValue;
        int testValue = 0;

        // Find the best assignment
        bestAssignment = PartitionValuesFromIndex(values, 0, totalValue, unassignedValue, testAssignment, testValue);
        
        // Print the best assignment
        if (bestAssignment == null) {
            System.out.println("No valid assignment found.");
        } else {
            System.out.println("Best Assignment: " + Arrays.toString(bestAssignment));
        }
    }

    public static boolean[] PartitionValuesFromIndex(int[] values,
                                                      int startIndex, int totalValue, int unassignedValue,
                                                      boolean[] testAssignment, int testValue) {
        boolean[] bestAssignment = new boolean[values.length];
        int[] bestError = {Integer.MAX_VALUE};

        // Call the recursive helper function
        PartitionValuesFromIndexHelper(values, startIndex, totalValue, unassignedValue, testAssignment, testValue, bestAssignment, bestError);

        return bestAssignment;
    }

    private static void PartitionValuesFromIndexHelper(int[] values,
                                                       int startIndex, int totalValue, int unassignedValue,
                                                       boolean[] testAssignment, int testValue,
                                                       boolean[] bestAssignment, int[] bestError) {
        // If startIndex is beyond the end of the array,
        // then all entries have been assigned.
        if (startIndex >= values.length) {
            // We're done. See if this assignment is better than
            // what we have so far.
            int testError = Math.abs(2 * testValue - totalValue);
            if (testError < bestError[0]) {
                // This is an improvement. Save it.
                bestError[0] = testError;
                System.arraycopy(testAssignment, 0, bestAssignment, 0, testAssignment.length);
            }
        } else {
            // See if there's any way we can assign
            // the remaining items to improve the solution.
            int testError = Math.abs(2 * testValue - totalValue);
            if (testError - unassignedValue < bestError[0]) {
                // There's a chance we can make an improvement.
                // We will now assign the next item.
                unassignedValue -= values[startIndex];

                // Try adding values[startIndex] to set 1.
                testAssignment[startIndex] = true;
                PartitionValuesFromIndexHelper(values, startIndex + 1,
                        totalValue, unassignedValue,
                        testAssignment, testValue + values[startIndex],
                        bestAssignment, bestError);

                // Try adding values[startIndex] to set 2.
                testAssignment[startIndex] = false;
                PartitionValuesFromIndexHelper(values, startIndex + 1,
                        totalValue, unassignedValue,
                        testAssignment, testValue,
                        bestAssignment, bestError);
            }
        }
    }
}
