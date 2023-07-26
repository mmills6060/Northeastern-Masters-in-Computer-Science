import java.time.DateTimeException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

/**
 * This class represents an organization with employees.
 */

public class OrganizationImpl implements Organization {
    private Employee root;
    private List<Employee> employees;

    public OrganizationImpl(String nameCEO, double pay, Gender gender) {
        root = new InternalEmployee(nameCEO, pay, gender);
        employees = new ArrayList<>();
        employees.add(root);
    }

    /**
     * The implementation below does not work. Why is that? Inspect the errors and change it around until it does.
     * @param name name of employee to be added
     * @param pay the annual pay of this employee
     * @param gender the gender of this employee
     * @param supervisorName the name of the supervisor. The supervisor should
     *                       be an existing employee
     */
    @Override
    public void addEmployee(String name, double pay, Gender gender, String supervisorName) {
        Employee newEmployee = new NonManagerEmployee(name,pay,gender);
        root = root.addSupervisee(supervisorName,newEmployee);
        employees.add(newEmployee);
    }

    @Override
    public void addContractEmployee(String name, double pay, Gender gender, int
            endDate, int endMonth, int endYear, String supervisorName) {
        Employee newEmployee = new ContractEmployee(name,pay,gender,endDate,endMonth,
                endYear);
        root = root.addSupervisee(supervisorName,newEmployee);
        employees.add(newEmployee);
    }

//    @Override
    public int getSize() {
        return root.count(b -> true);
    }
   public int getSizeByPay(Predicate<Employee> condition) {
    return root.count(condition);
}

   @Override
    public int getSizeByGender(Gender gender) {
        return root.count(b -> b.getGender() == gender);
    }
    @Override
    public List<String> allEmployees() {
        return root.toList().stream().map(e->e.getName()).collect(Collectors
                .toList());
    }
    public List<Employee> allWorkers() {
        return root.toList();
    }
    public List<Employee> getEmployees() {
        return employees;
    }
    //@Override
    public int countPayAbove(double amount) {
        return root.count(b -> b.getAnnualPay() > amount);
    }

    //@Override
    public int terminatedBefore(int date,int month,int year) {
        LocalDate threshold;

        try {
            threshold = LocalDate.of(year,month,date);
        }
        catch (DateTimeException e) {
            return 0;
        }
        return root.count(b->{
            if (b.getEmploymentEndDate().equals("XXXXXXXX"))
                return false;
            else {
                LocalDate d = LocalDate.parse(b.getEmploymentEndDate(),
                        DateTimeFormatter.ofPattern("MMddyyyy"));
                return d.compareTo(threshold)<0;
            }
        });
    }

    public void printEmployees() {
        for (Employee employee : employees) {
            System.out.println("Name: " + employee.getName());
            System.out.println("Gender: " + employee.getGender());
            System.out.println("Annual Pay: " + employee.getAnnualPay());
            System.out.println("-------------------------");
        }
    }



}