/*
handles the null block exception error.
*/
public class NullResourceException extends RuntimeException {
    public NullResourceException(String message) {
        super(message);
    }
}