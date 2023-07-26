package first_try;
/**
 * Author: Michael Arthur Mills 
 * Class: CS 5005 
 * Date: July 1 2023
 */


public interface Node {
    String getStringRepresentation();
    Node cloneNode();
    Node merge(Node other);
    Object getValue();
}