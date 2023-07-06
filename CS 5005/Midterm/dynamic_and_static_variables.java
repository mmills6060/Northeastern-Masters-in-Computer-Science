public class dynamic_and_static_variables {
    private static int courtCount = 0;
    private String courtName;
    
    public void TennisCourt(String courtName) {
        this.courtName = courtName;
        courtCount++;
    }
    
    public void displayCourtInfo() {
        System.out.println("Court Name: " + courtName);
        System.out.println("Number of Courts: " + courtCount);
    }
    
    public static void main(String[] args) {
        TennisCourt court1 = new TennisCourt();
        court1.displayCourtInfo();
        
        TennisCourt court2 = new TennisCourt();
        court2.displayCourtInfo();
        
        TennisCourt court3 = new TennisCourt();
        court3.displayCourtInfo();
    }
}
