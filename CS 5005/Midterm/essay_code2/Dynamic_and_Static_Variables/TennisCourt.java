package essay_code2.Dynamic_and_Static_Variables;

public class TennisCourt {

    public TennisCourt(String string) {
    }

   
    //define a method called displayCourtInfo
    public void displayCourtInfo() {
        //print out the value of the private variable courtName
        System.out.println("Court Name: " + courtName);
        String courtCount;
        //print out the value of the private static variable courtCount
        System.out.println("Number of Courts: " + courtCount);
    }
}
