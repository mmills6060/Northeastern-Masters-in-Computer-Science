package essay_code2.Dynamic_and_Static_Variables;

public class Main {
    
    
    public static void main(String[] args) {
        //Create a new TennisCourt object called court1
        TennisCourt court1 = new TennisCourt("Centre Court");
        //Display information about the TennisCourt object called court1
        court1.displayCourtInfo();
        
        //Create a new TennisCourt object called court2
        TennisCourt court2 = new TennisCourt("Court 1");
        //Display information about the TennisCourt object called court2
        court2.displayCourtInfo();
        
        //Create a new TennisCourt object called court3
        TennisCourt court3 = new TennisCourt("Court 2");
        //Display information about the TennisCourt object called court3
        court3.displayCourtInfo();
    }
}