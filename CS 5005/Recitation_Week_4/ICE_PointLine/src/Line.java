public class Line {
    private Point p1;
    private Point p2;

    public Line() {
        p1 = new Point(0, 0);
        p2 = new Point(0, 0);
    }

    public Line(Point p1, Point p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public Line(int x1, int y1, int x2, int y2) {
        p1 = new Point(x1, y1);
        p2 = new Point(x2, y2);
    }

    public void printLine() {
        System.out.println("Line: " + p1.toString() + " to " + p2.toString());
    }

    public double getLength() {
        int deltaX = p2.getX() - p1.getX();
        int deltaY = p2.getY() - p1.getY();
        return Math.sqrt(deltaX * deltaX + deltaY * deltaY);
    }

    public double lineSlope() {
        int deltaY = p2.getY() - p1.getY();
        int deltaX = p2.getX() - p1.getX();
        return (double) deltaY / deltaX;
    }
}
