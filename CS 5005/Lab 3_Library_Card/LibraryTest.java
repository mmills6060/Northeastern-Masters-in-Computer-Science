/**
 *  Name: Michael Mills
 * Course: CS 5005
 * Assignment: Recitation Week 3 - Person-3.java
 * Didnt have enough time to implement code. 
 * This class represents a person
 * The person has a first name, last name and year of birth
 */
import java.time.LocalDate;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;


public class LibraryTest{
    /**
     * 
     */
    public void testAll(){
        testToString();
        testPerson();
        testFirstName();
        testLastName();
        testYearOfBirth();
        testToString();
        testSamePerson();
        testGetCardNumber();                
        testTotalFees();
        testborrowBook();
        testreturnBook();
        testmakePayment();
        testgetDueDate();
        testbook();
        testgetTitle();
        testgetAuthor();
        testgetISBN();
        testisAvailable();
        testisAvailable();
        testtoString(); 
        testgetIssueDate();
        testgetDueDate();
        testGetLateFees();
    }
    @Test
   // Test Person
    public void testPerson() {
        Person person = new Person("Michael", "Mills", 1997);
        Assertions.assertEquals("Michael", person.getFirstName());
        Assertions.assertEquals("Mills", person.getLastName());
        Assertions.assertEquals(1997, person.getYearOfBirth());
        System.out.println("Person test Passed");
    }    
    // Test getFirstName
    public void testFirstName() {
        Person person = new Person("Michael", "Mills", 1997);
        Assertions.assertEquals("Michael", person.getFirstName());
        System.out.println("FirstName test Passed");
    }
    // Test getLastName
    public void testLastName() {
        Person person = new Person("Michael", "Mills", 1997);
        Assertions.assertEquals("Mills", person.getLastName());
        System.out.println("LastName test Passed");
    }
    // Test getYearOfBirth
    public void testYearOfBirth() {
        Person person = new Person("Michael", "Mills", 1997);
        Assertions.assertEquals(1997, person.getYearOfBirth());
        System.out.println("YearOfBirth test Passed");
    }
    // Test toString
    public void testToString() {
        Person person = new Person("Michael", "Mills", 1997);
        Assertions.assertEquals("Michael Mills", person.toString());
        System.out.println("ToString test Passed");}
    // Test samePerson
    public void testSamePerson() {
        Person person1 = new Person("Michael", "Mills", 1997);
        Person person2 = new Person("Michael", "Mills", 1997);
        Assertions.assertTrue(person1.same(person2));
        System.out.println("SamePerson test Passed");
    }
    // Test LibraryCard
    // Test getCardNumber
    public void testGetCardNumber() {
        LibraryCard card = new LibraryCard(0, 0.0);
        Assertions.assertEquals(0, card.getCardNumber());
        System.out.println("GetCardNumber test Passed");
    }
    // Test getTotalFees
    public void testTotalFees() {
        LibraryCard card = new LibraryCard(0, 0.0);
        Assertions.assertEquals(0, card.getTotalFees());
        System.out.println("TotalFee test Passed");
    }
    // Test borrowBook
    public void testborrowBook() {
        LibraryCard card = new LibraryCard(0, 0.0);
        Assertions.assertEquals(0, card.getTotalFees());
        System.out.println("borrowBook test Passed");
    }
    // Test returnBook
    public void testreturnBook() {
        LibraryCard card = new LibraryCard(0, 0.0);
        Assertions.assertEquals(0, card.getTotalFees());
        System.out.println("TreturnBook test Passed");
    }
    // Test makePayment
    public void testmakePayment() {
        LibraryCard card = new LibraryCard(0, 0.0);
        Assertions.assertEquals(0, card.getTotalFees());
        System.out.println("makePayment test Passed");
    }
    // Test Book
    public void testbook() {
        Book book = new Book("The Great Gatsby", "F. Scott Fitzgerald", 0);
        Assertions.assertEquals("The Great Gatsby", book.getTitle());
        Assertions.assertEquals("F. Scott Fitzgerald", book.getAuthor());
        Assertions.assertEquals(0, book.getISBN());
        Assertions.assertTrue(book.isAvailable());
        System.out.println("Book test Passed");
    }
    // Test getTitle
    public void testgetTitle() {
        Book book = new Book("The Great Gatsby", "F. Scott Fitzgerald", 0);
        Assertions.assertEquals("The Great Gatsby", book.getTitle());
        System.out.println("GetTitle test Passed");
    }
    // Test getAuthor
    public void testgetAuthor() {
        Book book = new Book("The Great Gatsby", "F. Scott Fitzgerald", 0);
        Assertions.assertEquals("F. Scott Fitzgerald", book.getAuthor());
        System.out.println("GetAuthor test Passed");
    }
    // Test getISBN
    public void testgetISBN() {
        Book book = new Book("The Great Gatsby", "F. Scott Fitzgerald", 0);
        Assertions.assertEquals(0, book.getISBN());
        System.out.println("GetISBN test Passed");
    }
    // Test isAvailable
    public void testisAvailable() {
        Book book = new Book("The Great Gatsby", "F. Scott Fitzgerald", 0);
        Assertions.assertTrue(book.isAvailable());
        System.out.println("IsAvailable test Passed");
    }
    // Test setAvailable
    public void testsetAvailable() {
        Book book = new Book("The Great Gatsby", "F. Scott Fitzgerald", 0);
        Assertions.assertTrue(book.isAvailable());
        System.out.println("SetAvailable test Passed");
    }
    // Test toString
    public void testtoString() {
        Book book = new Book("The Great Gatsby", "F. Scott Fitzgerald", 0);
        Assertions.assertEquals("Title: The Great Gatsby\nAuthor: F. Scott Fitzgerald\nISBN: ", book.toString());
        System.out.println("ToString test Passed");
    }
    // Test BorrowedBook
    // Test getIssueDate
    public void testgetIssueDate() {
        LocalDate expectedIssueDate = LocalDate.now();
        BorrowedBook book = new BorrowedBook(null, null, 0);
        LocalDate actualIssueDate = book.getIssueDate();
        Assertions.assertEquals(expectedIssueDate, actualIssueDate);
        System.out.println("getIssueDate test Passed");
    } 
    // Test getDueDate
    public void testgetDueDate() {
        LocalDate issueDate = LocalDate.now();
        LocalDate expectedDueDate = issueDate.plusDays(14);
        BorrowedBook book = new BorrowedBook(issueDate, null, 0);
        LocalDate actualDueDate = book.getDueDate();
        Assertions.assertEquals(expectedDueDate, actualDueDate);    
        System.out.println("getDueDate test Passed");
    }
    // Test getLateFees
    public void testGetLateFees() {
        LocalDate issueDate = LocalDate.now();
        LocalDate dueDate = issueDate.minusDays(7);
        int expectedLateFees = 14;
        BorrowedBook book = new BorrowedBook(issueDate, dueDate, 0);
        int actualLateFees = book.getLateFees();
        Assertions.assertEquals(expectedLateFees, actualLateFees);
        System.out.println("getLateFees test Passed");}
}
