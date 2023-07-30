import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        // Create instances of UserModel, UserController, and UserView
        Model userModel = new Model();
        Controller userController = new Controller(userModel);
        View userView = new View();

        // Add some sample users and their uploaded files (for demonstration purposes)
        userController.handleNewUser("Rafael Nadal", "user1@example.com");
        userController.handleNewUser("Andre Agassi", "user2@example.com");
        userController.handleNewUser("Roger Federer", "user3@example.com");

        userController.handleFileUpload("Rafael Nadal", "file1.txt");
        userController.handleFileUpload("Rafael Nadal", "file2.jpg");
        userController.handleFileUpload("Andre Agassi", "file3.docx");
        userController.handleFileUpload("Andre Agassi", "file4.pdf");
        userController.handleFileUpload("Roger Federer", "file5.mp4");

        // Print the list of all added users
        List<String> addedUsers = userController.getAddedUsers();
        System.out.println("List of Added Users:");
        for (String username : addedUsers) {
            System.out.println("- " + username);
        }
        // Print the total number of users
        int totalUsers = userController.getTotalUsers();
        System.out.println("Total Number of Users: " + totalUsers);
       }
       }

