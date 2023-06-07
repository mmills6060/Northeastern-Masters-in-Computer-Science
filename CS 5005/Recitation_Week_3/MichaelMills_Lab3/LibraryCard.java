import java.util.ArrayList;
import java.util.List;

/**
 * Represents a library card that a person can hold and use.
 * Each library card has a card number and keeps track of associated fees.
 */
public class LibraryCard {
    private int cardNumber;
    private double fees; 
    private static int numCards = 0;

    /**
     * Constructs a LibraryCard object and initializes it
     * with the given card number and fees.
     *
     * @param cardNumber the card number of this library card
     * @param fees the fees associated with this library card
     */
    public LibraryCard(int cardNumber, double fees) {
        this.cardNumber = cardNumber;
        this.fees = fees;
    }

    /**
     * Returns the card number associated with this library card.
     * Each time this method is called, it generates and returns a new card number.
     *
     * @return the card number of this library card
     */
    public int getCardNumber(){
        cardNumber = numCards++;
        return this.cardNumber;
    }
    
    /**
     * Returns the total fees associated with this library card.
     *
     * @return the total fees of this library card
     */
    public double getTotalFees(){
        fees = 0.00;
        return this.fees;
    }
    private List<Book> borrowedBooks = new ArrayList<>(); 

    /**
     * Borrows the given book by updating its availability status
     * and putting it into one of three available borrowed book spots.
     * If the book is available, it sets the availability to false,
     * adds it to the borrowed books list, and returns 0.
     * If the book is already borrowed, it returns 1.
     * If all three spots are occupied, it returns 2.
     *
     * @param book the book to be borrowed
     * @return 0 if the book is successfully borrowed,
     *         1 if the book is already borrowed,
     *         2 if all three spots are occupied.
     */
    public int borrowBook(Book book) {
        if (book.isAvailable()) {
            if (borrowedBooks.size() < 3) {
                book.setAvailable(false);
                borrowedBooks.add(book);
                return 0;
            } else {
                return 2; // All spots are occupied
            }
        } else {
            return 1; // Book is already borrowed
        }
    }

    /**
     * Returns the given book by updating its availability status.
     * If the book is already available, it returns 1 indicating an error.
     * Otherwise, it sets the availability to true and returns 0.
     *
     * @param book the book to be returned
     * @return 0 if the book is successfully returned, 1 if the book is already available
     */
    public int returnBook(Book book){
        if(book.isAvailable()){
            return 1;
        }
        else{
            book.setAvailable(true);
            return 0;
        }
    }

    /**
     * Makes a payment towards the fees associated with this library card.
     * If the given amount is positive, it subtracts the amount from the fees and returns 0.
     * Otherwise, it returns 1 indicating an error.
     *
     * @param amount the payment amount
     * @return 0 if the payment is successful, 1 if the amount is non-positive
     */
    public int makePayment(double amount){
        if(amount > 0){
            this.fees -= amount;
            return 0;
        }
        else{
            return 1;
        }
    }
}
