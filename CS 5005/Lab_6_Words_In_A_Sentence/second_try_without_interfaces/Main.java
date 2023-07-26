package second_try;

import org.junit.runner.JUnitCore;
import org.junit.runner.Result;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        runTests();

        // Clone
        List<String> original = new ArrayList<>();
        original.add("This");
        original.add("is");
        original.add("a");
        original.add("sentence");
        original.add(".");

        List<String> duplicate = Clone.clone(original);

        System.out.println("Original: " + original);
        System.out.println("Duplicate: " + duplicate);

        // Get number of words
        // Create a linked list of words
        getNumberOfWords.ListNode sentence = new getNumberOfWords.ListNode("This");
        sentence.next = new getNumberOfWords.ListNode("is");
        sentence.next.next = new getNumberOfWords.ListNode("a");
        sentence.next.next.next = new getNumberOfWords.ListNode("sentence");
        sentence.next.next.next.next = new getNumberOfWords.ListNode(".");

        // Call the getNumberOfWordsInSentence method to get the number of words in the sentence
        int numWords = getNumberOfWords.getNumberOfWordsInSentence(sentence);

        // Print the result
        System.out.println("Number of words in the sentence: " + numWords);

        // Merge
        // Create the first sentence linked list
        merge.ListNode sentence1 = new merge.ListNode("Andre");
        sentence1.next = new merge.ListNode("Agassi");
        sentence1.next.next = new merge.ListNode("is");
        sentence1.next.next.next = new merge.ListNode("good");
        sentence1.next.next.next.next = new merge.ListNode("at");
        sentence1.next.next.next.next.next = new merge.ListNode("tennis");

        // Create the second sentence linked list
        merge.ListNode sentence2 = new merge.ListNode("Andy");
        sentence2.next = new merge.ListNode("Murray");
        sentence2.next.next = new merge.ListNode("is");
        sentence2.next.next.next = new merge.ListNode("also");
        sentence2.next.next.next.next = new merge.ListNode("good");
        sentence2.next.next.next.next.next = new merge.ListNode("at");
        sentence2.next.next.next.next.next.next = new merge.ListNode("tennis");

        // Merge the two sentences
        merge.ListNode mergednode = merge.mergeSentences(sentence1, sentence2);

        // Print the merged sentence
        System.out.println("Merged Sentence:");
        printSentence(mergednode);

        // Longest word
        // Create the linked list for the sentence
        longestWord.ListNode sentence3 = new longestWord.ListNode("Roger");
        sentence3.next = new longestWord.ListNode("Federer");
        sentence3.next.next = new longestWord.ListNode("is");
        sentence3.next.next.next = new longestWord.ListNode("a");
        sentence3.next.next.next.next = new longestWord.ListNode("good");
        sentence3.next.next.next.next.next = new longestWord.ListNode("tennis");
        sentence3.next.next.next.next.next.next = new longestWord.ListNode("player");
        sentence3.next.next.next.next.next.next.next = new longestWord.ListNode("!");

        // Find the longest word in the sentence
        String longestWordInSentence = longestWord.findLongestWord(sentence3);

        // Print the result
        System.out.println("Longest word: " + longestWordInSentence);

        // toString
        // Create the linked list for the sentence
        toString.ListNode sentence4 = new toString.ListNode("Rafa");
        sentence4.next = new toString.ListNode("Nadal");
        sentence4.next.next = new toString.ListNode("can");
        sentence4.next.next.next = new toString.ListNode("talk");
        sentence4.next.next.next.next = new toString.ListNode("as");
        sentence4.next.next.next.next.next = new toString.ListNode("a");
        sentence4.next.next.next.next.next.next = new toString.ListNode("string");
        sentence4.next.next.next.next.next.next.next = new toString.ListNode("!");

        // Convert the sentence to a string
        String sentenceAsString = toString.sentenceToString(sentence4);

        // Print the result
        System.out.println("Sentence as a string: " + sentenceAsString);
    }

    // Helper method to print the merged sentence
    private static void printSentence(merge.ListNode node) {
        while (node != null) {
            System.out.print(node.data + " ");
            node = node.next;
        }
        System.out.println();
    }

    private static void runTests() {
        Result result = JUnitCore.runClasses(test.class);

        if (result.wasSuccessful()) {
            System.out.println("All tests passed!");
        } else {
            System.out.println("Test failures:");
            for (org.junit.runner.notification.Failure failure : result.getFailures()) {
                System.out.println(failure.toString());
            }
        }
    }
}
