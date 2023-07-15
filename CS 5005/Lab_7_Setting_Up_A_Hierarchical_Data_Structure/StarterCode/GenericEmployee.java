import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

/**
 * This class represents the data and operations of any employee. It defines
 * all the operations that either ought to be common to all implementations,
 * or have a reasonable default to be overridden by them.
 *
 * Note that you will need to ADD THE addEmployee METHOD that is being used
 * in the OrganizationDriver file. This might be a good place to create it.
 */

public abstract class GenericEmployee implements Employee {
  protected String name;
  protected double pay;
  protected Gender gender;


  public GenericEmployee(String name,double pay, Gender gender) {
    this.name = name;
    this.pay = pay;
    this.gender = gender;
  }


  @Override
  public String getName() {
    return this.name;
  }

  @Override
  public Gender getGender() {
    return this.gender;
  }

  @Override
  public double getAnnualPay() {
    return this.pay;
  }


  /**
   * By default, there is no end date for an employee. Only contract
   * employees have an actual end date.
   * @return
   */
  @Override
  public String getEmploymentEndDate() {
    return "XXXXXXXX";
  }

  @Override
  public int count(Predicate<Employee> condition) {
    if (condition.test(this)) {
      return 1;
    }
    return 0;
  }

  @Override
  public List<Employee> toList() {
    List<Employee> result = new ArrayList<Employee>();
    result.add(this);
    return result;
  }
  
  @Override
  public List<Employee> toList(Predicate<Employee> predicate) {
    List<Employee> result = new ArrayList<Employee>();
	
	if(predicate.test(this))result.add(this);
	
    return result;
  }
  
  public String toString()
  {
	  return "Name : " + name + ", Gender : " + gender + ", Pay : " + pay; 
  }
  
}