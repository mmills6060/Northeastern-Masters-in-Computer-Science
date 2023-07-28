// Main.java (Driver File)
public class Main {
    public static void main(String[] args) {
        Model model = new Model();
        View view = new View();
        Controller controller = new Controller(model, view);

        // Example usage
        double lat1 = 43.8523;
        double lon1 = 69.6281;
        double lat2 = 43.5637;
        double lon2 = 70.2000;

        controller.calculateDistance(lat1, lon1, lat2, lon2);

        double distance = 56; // miles
        double speed = 60; // mph
        controller.calculateTime(distance, speed);

        double fuelEfficiency = 30; // miles per gallon
        double currentSpeed = 50; // mph
        double remainingFuel = 10; // gallons
        controller.calculateTimeToRefuel(fuelEfficiency, currentSpeed, remainingFuel);

        double currentSpeed2 = 40; // mph
        double distanceToStop = 50; // feet
        double decelerationRate = 10; // ft/s^2
        controller.calculateStoppingTime(currentSpeed2, distanceToStop, decelerationRate);
    }
}
