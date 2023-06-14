/**
 *  Name: Michael Mills
 * Course: CS 5005
 * Assignment: Recitation Week 3 - Person-3.java
 * Didnt have enough time to implement code. 
 * This class represents a person
 * The person has a first name, last name and year of birth
 */
//import java.time.localDate;

import java.time.LocalDate;


/**
 * Represents a borrowed book with associated dates and late fees.
 * The book has an issue date, due date, and late fees.
 */
public class BorrowedBook {
    private LocalDate issueDate;
    private LocalDate dueDate;
    private int lateFees;
    private LocalDate currentDate;

    /**
     * Constructs a BorrowedBook object with the given issue date, due date, and late fees.
     *
     * @param issueDate the issue date of the borrowed book
     * @param dueDate the due date of the borrowed book
     * @param lateFees the late fees associated with the borrowed book
     */
    public BorrowedBook(LocalDate issueDate, LocalDate dueDate, int lateFees){
        this.issueDate = issueDate;
        this.dueDate = dueDate;
        this.lateFees = lateFees;
    }

    /**
     * Returns the issue date of the borrowed book.
     * The issue date is set to the current date when this method is called.
     *
     * @return the issue date of the borrowed book
     */
    public LocalDate getIssueDate(){
        this.issueDate = LocalDate.now();
        return issueDate;
    }

    /**
     * Returns the due date of the borrowed book.
     * The due date is calculated by adding 14 days to the issue date.
     *
     * @return the due date of the borrowed book
     */
    public LocalDate getDueDate(){
        return issueDate.plusDays(14);
    }

    /**
     * Returns the late fees associated with the borrowed book.
     * If the current date is greater than or equal to the due date,
     * the late fees are calculated based on the number of days late,
     * where each day late incurs a fee of twice the number of days late.
     *
     * @return the late fees associated with the borrowed book
     */
    public int getLateFees(){
        this.currentDate = LocalDate.now();
        if (this.currentDate.compareTo(this.dueDate) >= 0){
            int daysLate = this.currentDate.compareTo(this.dueDate);
            this.lateFees = daysLate * 2;
        }
        return this.lateFees;
    }
}
