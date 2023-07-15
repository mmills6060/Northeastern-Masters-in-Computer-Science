import java.util.List;
import java.util.function.Predicate;

/**
 * This interface represents a single employee in the organization. Every
 * employee is guaranteed to have a name, gender and pay on record
 */

public interface Employee {
  /**
   * Get the name of this employee
   * @return the name of this employee as a string
   */
  String getName();

  /**
   * Get the gender of this employee as per the organization records
   * @return the gender of this employee as an enum {@link organization.Gender}
   */
  Gender getGender();

  /**
   * Get the annual pay of this employee as per the organization records
   * @return the annual pay of this employee
   */
  double getAnnualPay();

  /**
   * Add the given employee as the supervisee of the employee with the given
   * name. This method has no effect on the hierarchy if the supervisor
   * cannot be found.
   * @param supervisorName the name of the supervisor
   * @param supervisee the employee that will be supervised by this employee
   * @return the resulting hierarchy of this employee
   */
   Employee addSupervisee(String supervisorName,Employee supervisee);

	 /**
   * Remove the given employee as the supervisee of the employee with the given
   * name. This method has no effect on the hierarchy if the supervisor
   * cannot be found.
   * @param supervisorName the name of the supervisor
   * @param supervisee the name of the employee that will be supervised by this employee
   * @return the resulting hierarchy of this employee
   */
   Employee removeSupervisee(String supervisorName, Employee supervisee);

  /**
   * Count the number of employees in this hierarchy
   * who fulfill the given predicate
   * @return the number of employees in this hierarchy that fulfill the
   * given predicate
   */
  int count(Predicate<Employee> condition);

  /**
   * Convert the employee hierarchy into a list.
   * @return the resulting list
   */
  List<Employee> toList();
  
  List<Employee> toList(Predicate<Employee> predicate);

  /**
   * Returns the date of the end of employment of this employee
   * @return the date in MMDDYYYY format
   */
  String getEmploymentEndDate();
  
  void printEmployees();


}