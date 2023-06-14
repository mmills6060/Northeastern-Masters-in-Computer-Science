import java.text.DecimalFormat;

public class PayCheck {
    private static DecimalFormat decimalFormat = new DecimalFormat("$0.00");
    private String employeeName;
    private int employeeId;
    private double rate;
    private double hoursWorked;
    private double totalPay;

    public PayCheck(String employeeName, int employeeId, double rate, double hoursWorked) {
        this.employeeName = employeeName;
        this.employeeId = employeeId;
        this.rate = rate;
        this.hoursWorked = hoursWorked;
        this.totalPay = rate * hoursWorked;
    }

    public PayCheck(Employee employee) {
        this(employee.getName(), employee.getID(), employee.getPayRate(), employee.getHoursWorked());
        if (employee == null) {
            throw new IllegalArgumentException("Employee cannot be null.");
        }
        
    }

    public double getTotalPay() {
        return totalPay;
    }

    public String toString() {
        return String.format("%.1f", totalPay);
    }
}