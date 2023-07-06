package essay_code2.Constructor;

// Create a class TennisPlayer
public class TennisPlayer {
    // Create a private static String variable called "name"
    private static String name;
    // Create a private int variable called "age"
    private int age;
    // Create a constructor that takes a String and an int as parameters
    public TennisPlayer(String string, int i) {
        // Set the static variable "name" to the String parameter
        TennisPlayer.name = string;
        // Set the int variable "age" to the int parameter
        this.age = i;}
    // Create a public static method called getName that returns a String
    public static String getName() {
        // Return the static variable "name"
        return name;
    }
    // Create a public method called getAge that returns an int
    public int getAge() {
        // Return the int variable "age"
        return age;
    }
}