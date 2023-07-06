    
public class TennisRacket {
    private String brand;
    
    public TennisRacket(String brand) {
        this.brand = brand;
    }
    
    public void swing() {
        System.out.println("Swinging the " + brand + " racket.");
    }
}
