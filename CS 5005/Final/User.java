import java.util.ArrayList;
import java.util.List;

public class User {
    private String username;
    private String email;
    private List<String> uploadedFiles;

    public User(String username, String email) {
        this.username = username;
        this.email = email;
        this.uploadedFiles = new ArrayList<>();
    }

    public String getUsername() {
        return username;
    }

    public String getEmail() {
        return email;
    }

    public List<String> getUploadedFiles() {
        return uploadedFiles;
    }

    public void addUploadedFile(String filename) {
        uploadedFiles.add(filename);
    }
}


