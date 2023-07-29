// Controller.java
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Controller {
    private Model model;
    private View view;

    public Controller(Model model) {
        this.model = model;
        this.view = view;
    }

    public void calculateDistance(double lat1, double lon1, double lat2, double lon2) {
        double distance = model.calculateDistance(lat1, lon1, lat2, lon2);
        view.displayDistance(distance);
    }

    public void calculateTime(double distance, double speed) {
        double time = model.calculateTime(distance, speed);
        view.displayTime(time);
    }

    public void calculateTimeToRefuel(double fuelEfficiency, double currentSpeed, double remainingFuel) {
        double timeToRefuel = model.calculateTimeToRefuel(fuelEfficiency, currentSpeed, remainingFuel);
        view.displayTimeToRefuel(timeToRefuel);
    }

    public void calculateStoppingTime(double currentSpeed, double distanceToStop, double decelerationRate) {
        double stoppingTime = model.calculateStoppingTime(currentSpeed, distanceToStop, decelerationRate);
        view.displayStoppingTime(stoppingTime);
    }

    public void handleNewUser(String string, String string2) {
    }

    public void handleFileUpload(String string, String string2) {
    }

    public int getTotalUsers() {
        return 0;
    }

    public List<String> getMostActiveUsers() {
        return null;
    }

    public Map<String, Integer> getFileTypeDistribution() {
        return null;
    }

    public List<String> getAddedUsers() {
        return null;
    }
}
