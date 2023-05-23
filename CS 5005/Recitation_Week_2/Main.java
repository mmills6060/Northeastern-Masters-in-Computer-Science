public class Main {
    public static void main(String[] args) {
        // Create an employee object
        Employee employee = new Employee("Andre Agassi", 20.0);

        // Add hours worked
        employee.addHoursWorked(40);

        // Get the weekly paycheck
        PayCheck paycheck = employee.getWeeklyCheck();

        // Print employee information
        System.out.println(employee);

        // Print total pay from the paycheck
        System.out.println("Total Pay: " + paycheck.getTotalPay());
    }
}
