public class list {
    public static void main(String[] args) {
        List<Integer> availableCourts = new ArrayList<>();
        availableCourts.add(1);
        availableCourts.add(2);
        availableCourts.add(3);
        availableCourts.add(4);
        availableCourts.add(5);

        int bookedCourt = 3;
        if (availableCourts.contains(bookedCourt)) {
            availableCourts.remove(Integer.valueOf(bookedCourt));
            System.out.println("Court " + bookedCourt + " has been booked.");
        } else {
            System.out.println("Court " + bookedCourt + " is not available.");
        }

        int freedCourt = 2;
        if (!availableCourts.contains(freedCourt)) {
            availableCourts.add(freedCourt);
            System.out.println("Court " + freedCourt + " is now available.");
        } else {
            System.out.println("Court " + freedCourt + " is already available.");
        }

        System.out.println("Currently available courts: " + availableCourts);
    }
 
}
