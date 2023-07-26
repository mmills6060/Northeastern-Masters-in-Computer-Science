package StarterCode;
/*
This is your starting point and your testing file. 
Except for task 3 the code should work without modifications once you have everything else implemented.
*/

class OrganizationDriver
{
	public static void main(String [] args)
	{
		/** The following are the employees you'll need to add to the organization.
		 * Decide who should be a non-manager employee, who should be a supervisor,
		 * and who should be a supervisee for this hierarchy to work. Review the module
		 * and talk with your classmates if you get stuck.
		 *
		 * Remember to add any missing parameters based on the type of employee you make them.
		 * Include at least one contract employee and at least two supervisors. You can generate
		 * more employees and change around this structure if you wish.
		 *
		[employee type] m1 = new [employee type]("Hank Hill", 300.00, Gender.Male);
		 [employee type] m2 = new [employee type]("Ron Swanson", 350.00, Gender.Female);
		[employee type] m3 = new [employee type]("Norman Norton", 50.00, Gender.Male);
		[employee type] m4 = new [employee type]("Fred Kostos", 550.00, Gender.Male);
		[employee type] m5 = new [employee type]("Sarah Hemsworth", 1000.00, Gender.Female);
		[employee type] m6 = new [employee type]("Howard Scott", 300.00, Gender.Male);
		[employee type] m7 = new [employee type]("George Gant", 300.00, Gender.Male);
		[employee type] m8 = new [employee type]("Lin Dorset", 300.00, Gender.Female);
		[employee type] m9 = new [employee type]("Betty Ross", 300.00, Gender.Female);
		*/

		/**
		 * this will generate the organization, but double check:
		 * Do we need to make this person, Boss Boss, an employee as well?
		 */
		OrganizationImpl TestCorp = new OrganizationImpl("Boss Boss", 300000.00,Gender.UnDisclosed);

		/**
		 * The employees have been generated.
		 * Check to see if the hierarchy works!
		 */


		//This was part of the sample code provided by the module
		System.out.println(TestCorp.getSize());

		//Task 1: 
		//Build an implementation that does this: Print all the employees along with all their information
		//TestCorp.printEmployees();
		
		//Task 2:
		//Design a code segment to return a single int value: the number of employees who make 300.00 annually
		//System.out.println(TestCorp.getSize(m->m.getAnnualPay()==300.00));
		//Examine existing code to help with this task. getSizeByGender is a good example of this.
		//There was also an example implementation similar in the module.
		
		//Task 3: 
		//Print out a list of just employee names using allEmployees()
		//This function should return a string of all employee names that you can then print as output
	}
	
}