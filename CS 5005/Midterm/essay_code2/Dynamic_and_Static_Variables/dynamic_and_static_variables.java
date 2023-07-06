package essay_code2.Dynamic_and_Static_Variables;
public class dynamic_and_static_variables {
    //declare a private static variable of type int
    private static int courtCount = 0;
    //declare a private variable of type String
    private String courtName;
    
    //define a constructor that takes in a String argument called courtName
    public dynamic_and_static_variables(String courtName) {
        //set the value of the private variable courtName to the value of the argument courtName
        this.courtName = courtName;
        //increment the value of the private static variable courtCount
        courtCount++;
    }
    
    //define a method called displayCourtInfo
    public void displayCourtInfo() {
        //print out the value of the private variable courtName
        System.out.println("Court Name: " + courtName);
        //print out the value of the private static variable courtCount
        System.out.println("Number of Courts: " + courtCount);
    }
}