public class Point {
    private int x;
    private int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public void printPoint() {
        System.out.println("(" + x + ", " + y + ")");
    }

    public String getQuadrant() {
        if (x == 0 && y == 0) {
            return "Origin";
        } else if (x > 0 && y > 0) {
            return "Quadrant A";
        } else if (x < 0 && y > 0) {
            return "Quadrant B";
        } else if (x < 0 && y < 0) {
            return "Quadrant C";
        } else if (x > 0 && y < 0) {
            return "Quadrant D";
        } else {
            return "Boundary";
        }
    }
}
