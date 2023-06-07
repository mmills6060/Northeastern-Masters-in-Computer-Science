/**
 * CS 5004 Summer 2023
 * ICE Points and Lines
 * May 31, 2023
 * Completed driver test file with manual test cases.
 */

public class Driver {
    public static void main(String[] args) {
        // Create new point objects for testing
        Point p1 = new Point(0,0);
        Point p2 = new Point(1, 2);
        Point p3 = new Point(-1, 2);
        Point p4 = new Point(-1, -2);
        Point p5 = new Point(1, -2);
        Point p6 = new Point(-1,-1);
        Point p7 = new Point(-3, 2);

        // Create new line objects for testing
        Line l1 = new Line(1,3,-2,-4);
        Line l2 = new Line(p1, p2);
        Line l3 = new Line();
        Line l4 = new Line(p6,p7);

        // Testing line objects to make sure print method works as expected.
        l1.printLine();
        l2.printLine();
        l3.printLine();

        //Testing point objects to make sure print method works as expected.
        p1.printPoint();
        p2.printPoint();
        p3.printPoint();

        // Manual test cases run to test getQuadrant
        System.out.println(p1.getQuadrant());
        if (p1.getQuadrant() == "Origin") {
            System.out.println("Origin Test Passed.\n");
        }
        else System.out.println("Origin test failed.\n");

        System.out.println(p2.getQuadrant());
        if (p2.getQuadrant() == "Quadrant A") {
            System.out.println("Quadrant A test passed\n");
        }
        else System.out.println("Quadrant A test failed.\n");

        System.out.println(p3.getQuadrant());
        if (p3.getQuadrant() == "Quadrant B") {
            System.out.println("Quadrant B test passed\n");
        }
        else System.out.println("Quadrant B test failed.\n");

        System.out.println(p4.getQuadrant());
        if (p4.getQuadrant() == "Quadrant C") {
            System.out.println("Quadrant C test passed\n");
        }
        else System.out.println("Quadrant C test failed.\n");

        System.out.println(p5.getQuadrant());
        if (p5.getQuadrant() == "Quadrant D") {
            System.out.println("Quadrant D test passed\n");
        }
        else System.out.println("Quadrant D test failed.\n");
    }
}
