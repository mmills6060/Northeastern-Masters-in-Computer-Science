/**
 * Represents the main class for running the library tests.
 * This class executes the tests defined in the LibraryTest class.
 * It serves as the entry point for the program.
 */
public class Main {

    /**
     * The main method that runs the library tests.
     * It creates an instance of LibraryTest and calls the testAll method to execute all tests.
     *
     * @param args the command line arguments (unused)
     */
    public static void main(String[] args) {
        LibraryTest test = new LibraryTest();
        test.testAll();
    }
}
