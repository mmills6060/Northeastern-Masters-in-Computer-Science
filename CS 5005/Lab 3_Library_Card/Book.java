/**
 * This class represents a book. A book has a title, an author,
 * an ISBN, and a status (available or checked out).
 */
public class Book {
    private String title;
    private String author;
    private int ISBN;
    private boolean isAvailable;

    /**
     * Construct a Book object that has the
     * provided title, author and ISBN.
     *
     * @param title the title to be given to this book
     * @param string the author to be given to this book
     * @param ISBN the International Standard Book Number of this book
     */

    public Book(String title, String string, int ISBN) {
        this.title = title;
        this.author = string;
        this.ISBN = ISBN;
        this.isAvailable = true;
    }

    /**
     * Return the title of this book
     * @return the title of this book
     */

    public String getTitle() {
        
        return this.title;
    }

    /**
     * Return the author of this object
     * @return the author of this object as a @link{Person}
     */
    public String getAuthor() {
        return this.author;
    }

    /**
     * Return the ISBN of this book
     * @return the ISBN of this book
     */
    public int getISBN() {
        this.ISBN = 0;
        return this.ISBN;
    }

    /**
     * Return the availability status of the book.
     * @return the availability of the book: true if available,
     *         false otherwise.
     */
    public boolean isAvailable() {
        return isAvailable;
    }

    /**
     *
     * @param available
     */
    public void setAvailable(boolean available) {
        isAvailable = available;
    }

    /**
     * Return a formatted string that contains the information
     * of this object. The string should be in the following format:
     *
     * Title: [title of the book]
     * Author: [first-name last-name]
     * ISBN: [ISBN as a 13-digit integer with digits separated appropriately
     *        by dashes i.e. 978-3-16-148410-0].
     *
     * @return the formatted string as above
     */
    public String toString() {
        String str;

        str = "Title: "+ this.title + "\n" +
                "Author: "+this.author + "\n";
        str = str + String.format("ISBN: ", ISBN);

        return str;
    }
}
