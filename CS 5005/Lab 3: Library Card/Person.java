/**
 *  Name: Michael Mills
 * Course: CS 5005
 * Assignment: Recitation Week 3 - Person-3.java
 * Didnt have enough time to implement code. 
 * This class represents a person
 * The person has a first name, last name and year of birth
 */
public class Person {
    private String firstName;
    private String lastName;
    private int yearOfBirth;

    /**
     * Constructs a Person object and initializes it
     * to the given first name, last name and year of birth
     * @param firstName the first name of this person
     * @param lastName the last name of this person
     * @param yearOfBirth the year of birth of this person
     */

    public Person(String firstName, String lastName, int yearOfBirth) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.yearOfBirth = yearOfBirth;
    }

    /**
     * Get the first name of this person
     * @return the first name of this person
     */
    public String getFirstName() {
        
        return this.firstName;
    }

    /**
     * Return the last name of this person
     * @return the last name of this person
     */

    public String getLastName() {
        return this.lastName;
    }

    /**
     * Return the year of birth of this person
     * @return the year of birth of this person
     */
    public int getYearOfBirth() {
        return this.yearOfBirth;
    }

    /**
     Returns a string representation of this person with first
     and last name
     @return a formatted string
     */

    public String toString() {
        return "" + firstName  + " " + lastName;
    }

    /**
     * check if this person is the same
     * as the person in the argument.
     * two persons are the same iff they
     * have the same first and last names
     * and the same years of birth
     * @param other the other person to be compared to
     * @return true if this person is the same as other, false otherwise
     */
    public boolean same(Person other) {
        return  this.firstName.equals(other.firstName)
                && this.lastName.equals(other.lastName)
                && this.yearOfBirth == other.yearOfBirth;
    }
    
}
