// Project created by Michael Arthur Mills

// Main.java (Driver File)

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Create instances of Model, View, and Controller
        Model model = new Model();
        View view = new View();
        Controller controller = new Controller(model, view);

            // I am pretty sure you will need to run the file using terminal in order to be able to input an option. Otherwise it will just print as output. 
               // Create a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);
        // ask user what they would like to do today, wehther it is calculate distance between two points, calculate time to travel, calculate time remaining until refueling, or calculate time needed tobring a car to a complete stop
                System.out.println("What would you like to do today?");
                System.out.println("1. Calculate distance between two points");
                System.out.println("2. Calculate time to travel a distance");
                System.out.println("3. Calculate time remaining until refueling");
                System.out.println("4. Calculate time needed to bring a car to a complete stop");
                System.out.println("5. Do all of these things, with predefined values");
         // Read the user's choice
         int choice = scanner.nextInt();

        // Ensure the input is within the desired range (1 to 5)
        while (choice < 1 || choice > 5) {
            System.out.println("Invalid choice. Please enter a number between 1 and 5:");
            choice = scanner.nextInt();
        }
         // Perform the selected action based on the user's choice
         switch (choice) {
            case 1:
                System.out.println("Enter latitude and longitude of the first point:");
                double lat1 = scanner.nextDouble();
                double lon1 = scanner.nextDouble();
 
                System.out.println("Enter latitude and longitude of the second point:");
                double lat2 = scanner.nextDouble();
                double lon2 = scanner.nextDouble();
 
                controller.calculateDistance(lat1, lon1, lat2, lon2);
                break;
 
            case 2:
                 System.out.println("Enter the distance (in miles):");
                 double distance = scanner.nextDouble();
 
                 System.out.println("Enter the speed (in mph):");
                 double speed = scanner.nextDouble();
 
                 controller.calculateTime(distance, speed);
                 break;
 
            case 3:
                 System.out.println("Enter fuel efficiency (in miles per gallon):");
                 double fuelEfficiency = scanner.nextDouble();
 
                 System.out.println("Enter current speed (in mph):");
                 double currentSpeed = scanner.nextDouble();
 
                 System.out.println("Enter remaining fuel (in gallons):");
                 double remainingFuel = scanner.nextDouble();
 
                 controller.calculateTimeToRefuel(fuelEfficiency, currentSpeed, remainingFuel);
                 break;
 
            case 4:
                 System.out.println("Enter current speed (in mph):");
                 double currentSpeed2 = scanner.nextDouble();
 
                 System.out.println("Enter distance to stop (in feet):");
                 double distanceToStop = scanner.nextDouble();
 
                 System.out.println("Enter deceleration rate (in ft/s^2):");
                 double decelerationRate = scanner.nextDouble();
 
                 controller.calculateStoppingTime(currentSpeed2, distanceToStop, decelerationRate);
                 break;
            case 5:
                // Calculate distance between two points using latitude and longitude
                double lat1_fixed = 43.8523;
                double lon1_fixed = 69.6281;
                double lat2_fixed = 43.5637;
                double lon2_fixed = 70.2000;
                controller.calculateDistance(lat1_fixed, lon1_fixed, lat2_fixed, lon2_fixed);

                // Calculate time to travel a distance at a specific speed
                double distance_fixed = 56; // miles
                double speed_fixed = 60; // mph
                controller.calculateTime(distance_fixed, speed_fixed);

                // Calculate time remaining until refueling
                double fuelEfficiency_fixed = 30; // miles per gallon
                double currentSpeed_fixed = 50; // mph
                double remainingFuel_fixed = 11; // gallons
                controller.calculateTimeToRefuel(fuelEfficiency_fixed, currentSpeed_fixed, remainingFuel_fixed);

                // Calculate time needed to bring a car to a complete stop
                double currentSpeed2_fixed = 40; // mph
                double distanceToStop_fixed = 50; // feet
                double decelerationRate_fixed = 10; // ft/s^2
                controller.calculateStoppingTime(currentSpeed2_fixed, distanceToStop_fixed, decelerationRate_fixed);

                break;
 
             default:
                 System.out.println("Invalid choice. Please try again.");
         }
 
         // Close the scanner
         scanner.close();
     }
    }
