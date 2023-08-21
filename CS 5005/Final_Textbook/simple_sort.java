public class PlayerRankingSorting {
    public static void main(String[] args) {
        int[] rankings = {5, 2, 9, 1, 7, 3, 8, 4, 6}; 

        bubbleSort(rankings);

        System.out.println("Sorted Rankings: " + Arrays.toString(rankings));
    }

    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean swapped;

        for (int i = 0; i < n - 1; i++) {
            swapped = false;

            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            // If no two elements were swapped in the inner loop, the array is already sorted
            if (!swapped) {
                break;
            }
        }
    }
}