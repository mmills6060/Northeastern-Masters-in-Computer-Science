public class filter {
    public static void main(String[] args) {
        List<Integer> availableCourts = new ArrayList<>();
        availableCourts.add(7);
        availableCourts.add(2);
        availableCourts.add(10);
        availableCourts.add(1);
        availableCourts.add(5);
        availableCourts.add(9);
        availableCourts.add(8);
        availableCourts.add(4);
        availableCourts.add(6);
        availableCourts.add(3);

        // Sort the list in descending order
        Collections.sort(availableCourts, Collections.reverseOrder());

        // Display only the first five courts
        List<Integer> firstFiveCourts = availableCourts.subList(0, Math.min(5, availableCourts.size()));

        System.out.println("First five available courts (sorted): " + firstFiveCourts);
    }
}

