package essay_code2.Composition;


public class TennisRacket {
    //create a String variable named brand
    //this variable will be used to store the brand of the racket
    private String brand;
    
    //create a constructor that takes a String parameter
    //this constructor will be used to create a new TennisRacket object
    public TennisRacket(String brand) {
        //store the value of the parameter in the brand variable
        this.brand = brand;
    }
    
    //create a method named swing
    //this method will be used to swing the racket
    public void swing() {
        //print a message to the screen
        System.out.println("Swinging the " + brand + " racket.");
    }
}