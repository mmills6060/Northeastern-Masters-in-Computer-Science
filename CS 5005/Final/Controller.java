import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Controller {
    private Model userModel;
    private View userView;
    private List<String> addedUsers;

    public Controller(Model userModel) {
        this.userModel = userModel;
        this.userView = new View(); // For simplicity, we'll create a new View instance here
        this.addedUsers = new ArrayList<>();  // We can also use an array or any other
    }

    public void handleNewUser(String username, String email) {
        // Add a new user using the UserModel
        userModel.addUser(username, email);
        addedUsers.add(username); // keep track of the added user
        // Display a message to the user using the view
        userView.displayMessage("New user '" + username + "' added successfully!");
    }

    public void handleFileUpload(String username, String filename) {
        // Add the uploaded file to the user's file list using the UserModel
        userModel.addUploadedFile(username, filename);

        // Display a message to the user using the view
        userView.displayMessage("File '" + filename + "' uploaded successfully for user '" + username + "'.");
    }
    public List<String> getAddedUsers() {
        // Get a list of all the added users
        return addedUsers;
    }
    public int getTotalUsers() {
        // count the number of items in the array list addedusers
        return addedUsers.size();

    }
}
