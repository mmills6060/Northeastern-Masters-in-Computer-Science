import java.util.Collections;
import java.util.List;
import java.util.Map;

public class Model {
    private Map<String, User> usersData;

    // Constructor and methods to interact with the usersData HashMap
    // ...

    public void addUser(String username, String email) {
        // Add a new user to the usersData HashMap
    }

    public void addUploadedFile(String username, String filename) {
        // Add the uploaded file to the user's file list
    }

    public List<String> getUploadedFiles(String username) {
        // Get a list of files uploaded by a user
        return Collections.emptyList(); // Replace with actual implementation
    }

    // Other methods to fetch and manipulate user data
    // ...
}
