import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class PointLineTester {
	Point p1;
	Point p2;
	Point p3;
	Point p4;
	Point p5;
	Line l1;
	Line l2;
	Line l3;
	
	@Before
	public void setUp()	{
		p1 = new Point();		// Origin Point
		p2 = new Point(1,2);	// Quadrant A Point
		p3 = new Point(-1,2); 	// Quadrant B Point
		p4 = new Point (-1,-2);	// Quadrant C Point
		p5 = new Point (1,-2);	// Quadrant D Point
		l1 = new Line();
		l2 = new Line(p1,p2);
		l3 = new Line(4,5,6,7);
	}

	@Test
	public void lineSlopeTest() {
		assertEquals(2.0,l2.lineSlope(),0.01);
		assertEquals(0.0,l1.lineSlope(),0.01);
		assertEquals(1.0,l3.lineSlope(),0.01);
	}

	@Test
	public void getQuadTest() {
		assertEquals("There is no line.",l1.getQuad());
		assertEquals("Quadrant A",l2.getQuad());
		assertEquals("Quadrant A",l3.getQuad());
	}

	@Test
	public void noArgsPointConstructorTest() {
		assertEquals(0,p1.getX() + p1.getY());
	}
	
	@Test
	public void twoArgsPointConstructorTest() {
		assertEquals(1,p2.getX());
		assertEquals(2,p2.getY());
	}
	
	@Test
	public void setterTestX() {
		p1.setX(42);
		assertEquals(42,p1.getX());
	}
	
	@Test
	public void setterTestY() {
		p1.setY(42);
		assertEquals(42,p1.getY());
	}
	
	@Test
	public void limitTestGTX() {
		p1.setX(999);
		assertEquals(99,p1.getX());
	}
	
	@Test
	public void limitTestLTX() {
		p1.setX(-999);
		assertEquals(-99,p1.getX());
	}
	
	@Test
	public void limitTestGTY() {
		p1.setY(999);
		assertEquals(99,p1.getY());
	}
	
	@Test
	public void limitTestLTY() {
		p1.setY(-999);
		assertEquals(-99,p1.getY());
	}
	
	@Test
	public void originTest()
	{
		assertEquals("Origin",p1.getQuadrant());
	}
	
	@Test
	public void quadrantATest()
	{
		assertEquals("Quadrant A",p2.getQuadrant());
	}
	
	@Test
	public void quadrantBTest()
	{
		assertEquals("Quadrant B",p3.getQuadrant());
	}
	
	@Test
	public void quadrantCTest()
	{
		assertEquals("Quadrant C",p4.getQuadrant());
	}
	
	@Test
	public void quadrantDTest()
	{
		assertEquals("Quadrant D",p5.getQuadrant());
	}
	
	@Test
	public void noArgsConstructorLine()	{
		assertEquals(0,
				l1.getP1().getX() +
				l1.getP1().getY() +
				l1.getP2().getX() +
				l1.getP2().getY());
	}

	@Test
	public void pointArgsConstructorLine() {
		assertEquals(0,l2.getP1().getX());
		assertEquals(0,l2.getP1().getY());
		assertEquals(1,l2.getP2().getX());
		assertEquals(2,l2.getP2().getY());
	}

	@Test
	public void intArgsConstructorLine() {
		assertEquals(4,l3.getP1().getX());
		assertEquals(5,l3.getP1().getY());
		assertEquals(6,l3.getP2().getX());
		assertEquals(7,l3.getP2().getY());
	}

	@Test
	public void getLengthTest() {
		assertEquals(0.0,l1.getLength(),0.1);
		assertEquals(2.2, l2.getLength(), 0.1);
		assertEquals(2.8, l3.getLength(), 0.1);
	}
}
