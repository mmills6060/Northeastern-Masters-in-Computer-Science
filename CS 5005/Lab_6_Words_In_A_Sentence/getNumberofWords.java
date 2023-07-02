import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Author: Michael Arthur Mills 
 * Class: CS 5005 
 * Date: July 1 2023
 */


public class getNumberofWords {
    public static int getNumberOfWords(String sentence) {
        // Removing leading and trailing whitespace
        sentence = sentence.trim();
        
        // Removing punctuation marks from the sentence
        sentence = sentence.replaceAll("[^a-zA-Z ]", "");
        
        // Splitting the sentence into words and counting the number of words
        String[] words = sentence.split("\\s+");
        return words.length;
    }
    
    public static void main(String[] args) {
        String sentence = "Hello, how are you doing today?";
        int numWords = getNumberOfWords(sentence);
        System.out.println("Number of words: " + numWords);
    }
}
