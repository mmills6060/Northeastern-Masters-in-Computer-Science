package StarterCode;
import java.util.ArrayList;
import java.util.List;
/**
 * This class  represents an employee that does not have any managerial
 * responsibilities.
 */

public class NonManagerEmployee extends GenericEmployee{
  public NonManagerEmployee(String name, double pay, Gender gender) {
    super(name, pay, gender);
  }

  @Override
  public Employee addSupervisee(String supervisorName,Employee supervisee) {
    if (this.name.equals(supervisorName)) {
      //must first "promote" this employee
      Supervisor newSelf = new Supervisor(this.name,this.pay,this
              .gender);
      newSelf.addSupervisee(supervisorName,supervisee);
      return newSelf;
    }
    return this;
  }
  
  
  /*
	A non manager shouldn't have supervisees, but we need a place holder
  */
  @Override
  public Employee removeSupervisee(String supervisorName,Employee supervisee) {
    return this;
  }
  
  public void printEmployees()
  {
	  System.out.println(this);
  }
}