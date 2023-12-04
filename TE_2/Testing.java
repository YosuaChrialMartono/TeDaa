package TE_2;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class Testing {
    public static void main(String[] args) {
        String smallDatasetPath = "TE_2/dataset/small_dataset.txt";
        String mediumDatasetPath = "TE_2/dataset/medium_dataset.txt";
        String largeDatasetPath = "TE_2/dataset/large_dataset.txt";

        // Specify the output file
        String outputFileName = "test_results.txt";

        // Clear existing content in the output file
        clearFile(outputFileName);

        List<Integer> smallDataset = readNumbersFromFile(smallDatasetPath);
        List<Integer> mediumDataset = readNumbersFromFile(mediumDatasetPath);
        List<Integer> largeDataset = readNumbersFromFile(largeDatasetPath);

        // Test each dataset and method separately and record results
        writeTestResults(outputFileName, "Small", smallDataset);
        writeTestResults(outputFileName, "Medium", mediumDataset);
        writeTestResults(outputFileName, "Large", largeDataset);
    }

    private static void writeTestResults(String fileName, String datasetName, List<Integer> dataset) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName, true))) {
            writer.write("Results for " + datasetName + " dataset:");
            writer.newLine();

            // Test Memory for Dynamic Programming Method
            writer.write("Test Memory for Dynamic Programming Method:");
            writer.newLine();
            testMemory(writer, datasetName, dataset, true);

            // Test Memory for Branch and Bound Method
            writer.write("Test Memory for Branch and Bound Method:");
            writer.newLine();
            testMemory(writer, datasetName, dataset, false);

            // Test Runtime for Dynamic Programming Method
            writer.write("Test Runtime for Dynamic Programming Method:");
            writer.newLine();
            testRuntime(writer, datasetName, dataset, true);

            // Test Runtime for Branch and Bound Method
            writer.write("Test Runtime for Branch and Bound Method:");
            writer.newLine();
            testRuntime(writer, datasetName, dataset, false);

            writer.newLine(); // Add an empty line for separation between datasets
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void testRuntime(BufferedWriter writer, String datasetName, List<Integer> dataset, boolean useDynamicProgramming) {
        int[] datasetArray = dataset.stream().mapToInt(Integer::intValue).toArray();
        boolean[] testAssignment = new boolean[datasetArray.length];
        int totalValue = Arrays.stream(datasetArray).sum();
        int unassignedValue = totalValue;

        try {
            long startTime, endTime, elapsedTime;
            boolean[] bestAssignment;

            if (useDynamicProgramming) {
                startTime = System.nanoTime();
                DPPartition.findPartition(datasetArray, datasetArray.length);
                endTime = System.nanoTime();
                elapsedTime = endTime - startTime;
                bestAssignment = new boolean[datasetArray.length]; // No meaningful assignment for Dynamic Programming
            } else {
                startTime = System.nanoTime();
                bestAssignment = BBPartition.PartitionValuesFromIndex(datasetArray, 0, totalValue, unassignedValue, testAssignment, 0);
                endTime = System.nanoTime();
                elapsedTime = endTime - startTime;
            }

            writer.write("Best Assignment for " + datasetName + " dataset using " +
                    (useDynamicProgramming ? "Dynamic Programming" : "Branch and Bound") + " Method: " +
                    Arrays.toString(bestAssignment));
            writer.newLine();
            writer.write("Elapsed time for " + datasetName + " dataset using " +
                    (useDynamicProgramming ? "Dynamic Programming" : "Branch and Bound") +
                    " Method: " + elapsedTime + " nanoseconds");
            writer.newLine();
            writer.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void testMemory(BufferedWriter writer, String datasetName, List<Integer> dataset, boolean useDynamicProgramming) {
        int[] datasetArray = dataset.stream().mapToInt(Integer::intValue).toArray();
        boolean[] testAssignment = new boolean[datasetArray.length];
        int totalValue = Arrays.stream(datasetArray).sum();
        int unassignedValue = totalValue;

        try {
            long earlyMemory, lateMemory, memoryUsed;

            // Memory testing for Dynamic Programming Method
            if (useDynamicProgramming) {
                earlyMemory = getUsedMemory();
                DPPartition.findPartition(datasetArray, datasetArray.length);
                lateMemory = getUsedMemory();
                memoryUsed = lateMemory - earlyMemory;
            } else {
                // Memory testing for Branch and Bound Method
                earlyMemory = getUsedMemory();
                BBPartition.PartitionValuesFromIndex(datasetArray, 0, totalValue, unassignedValue, testAssignment, 0);
                lateMemory = getUsedMemory();
                memoryUsed = lateMemory - earlyMemory;
            }

            // Write the result
            writer.write("Memory used for " + datasetName + " dataset using " +
                    (useDynamicProgramming ? "Dynamic Programming" : "Branch and Bound") + " Method: " +
                    memoryUsed + " bytes");
            writer.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static long getUsedMemory() {
        Runtime runtime = Runtime.getRuntime();
        return runtime.totalMemory() - runtime.freeMemory();
    }

    private static List<Integer> readNumbersFromFile(String filePath) {
        List<Integer> numbers = new java.util.ArrayList<>();

        try (java.io.BufferedReader reader = new java.io.BufferedReader(new java.io.FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                int number = Integer.parseInt(line.trim());
                numbers.add(number);
            }
        } catch (java.io.IOException | NumberFormatException e) {
            e.printStackTrace();
        }

        return numbers;
    }

    private static void clearFile(String fileName) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName, false))) {
            // Writing an empty string to clear the file
            writer.write("");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
