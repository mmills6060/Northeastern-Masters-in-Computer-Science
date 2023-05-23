import java.text.DecimalFormat;

public class Employee {
    private static int employeeCount = 0;
    private int id;
    private String name;
    private double payRate;
    private double hoursWorked;

     /**
     * Creates an object with the name of employee with name and pay rate
     * Sets the hours worked to zero and sets the Employee ID based on
     * how many employee objects have been created.
     *
     * @param name    the name of the employee
     * @param payRate the pay rate of the employee
     */

    public Employee(String name, double payRate) {
        this.name = name;
        this.payRate = payRate;
        this.hoursWorked = 0;
        this.id = ++employeeCount;
    }

   /**
     * Adds the specified number of hours to the total hours worked by the employee.
     *
     * @param hours the number of hours to add
     */

    public void addHoursWorked(double hours) {
        if (hours < 0) {
            throw new IllegalArgumentException("Hours worked cannot be negative.");
        }
        if (hours > 60) {
            throw new IllegalArgumentException("Hours worked cannot exceed 60.");
        }
        this.hoursWorked += hours;
    }
    /**
     * Resets the number of hours worked by the employee to zero.
     */
    public void resetHoursWorked() {
        this.hoursWorked = 0;
    }
    /**
     * Determines the total pay for the week and returns a PayCheck object
     * calculated with the employee's name, ID, rate, hours worked, and total pay.
     * Resets the hours worked for the employee to zero.
     *
     * @return a PayCheck object
     */
    public PayCheck getWeeklyCheck() {
        PayCheck paycheck = new PayCheck(this);
        return paycheck;
        
    }
    /**
     * Returns a string representation of the employee in the format:
     * "Employee Name: {name}, Employee ID: {id}"
     *
     * @return a string representation of the employee
     */
    public String toString() {
        return "Employee Name: " + name + ", Employee ID: " + id;
    }
    /**
     * Returns the name of the employee.
     *
     * @return the name of the employee
     */
    public String getName() {
        return name;
    }
    /**
     * Returns the pay rate of the employee.
     *
     * @return the pay rate of the employee
     */
    public double getPayRate() {
        return payRate;
    }
    /**
     * Returns the number of hours worked by the employee.
     *
     * @return the number of hours worked by the employee
     */
    public double getHoursWorked() {
        return hoursWorked;
    }
    /**
     * Returns the ID of the employee.
     *
     * @return the ID of the employee
     */
    public int getID() {
        return id;
    }
}
