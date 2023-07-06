package essay_code2.Constructor;

public class Main {
    
    public static void main(String[] args) {
        // Create a new TennisPlayer object with name "Roger Federer" and age 39
        TennisPlayer player = new TennisPlayer("Roger Federer", 39);
        
        // Print the name and age of the TennisPlayer object
        System.out.println("Name: " + TennisPlayer.getName());
        System.out.println("Age: " + player.getAge());
    }
}
