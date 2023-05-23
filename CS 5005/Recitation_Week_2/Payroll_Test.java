
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class Payroll_Test {
    /**
     * 
     */
    @Test
    public void testGetWeeklyCheck() {
        Employee employee = new Employee("Roger Federer", 20.0);
        employee.addHoursWorked(40);

        PayCheck paycheck = employee.getWeeklyCheck();
    /**
     * 
     * testing to make sure that the name, id, pay rate and hours worked are correct
     */
        Assertions.assertEquals("Roger Federer", employee.getName());
        Assertions.assertEquals(1, employee.getID());
        Assertions.assertEquals(20.0, employee.getPayRate());
        Assertions.assertEquals(40.0, employee.getHoursWorked());
 
    }
    @Test
    public void testToString() {
        Employee employee = new Employee("Tiger Woods", 25.0);
        String expected = "Employee Name: Tiger Woods, Employee ID: 1";
        Assertions.assertEquals(expected, employee.toString());
    }
}
