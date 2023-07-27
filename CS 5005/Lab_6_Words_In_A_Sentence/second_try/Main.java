package second_try;

import org.junit.runner.JUnitCore;
import org.junit.runner.Result;

// this is the main driver. there are random tests, but it also calls the test file which contains junit.


public class Main {

    public static void main(String[] args) {
        runTests();

        // Test the Sentence class
        Sentence sentence = new Sentence();
        SentenceAddWord.addWord(sentence, "Rafa");
        SentenceAddWord.addWord(sentence, "is");
        SentenceAddWord.addWord(sentence, "a");
        SentenceAddWord.addWord(sentence, "good");
        SentenceAddWord.addWord(sentence, "tennis");
        SentenceAddWord.addWord(sentence, "player");
        SentenceAddPunctuation.addPunctuation(sentence, ".");
        System.out.println("Original Sentence: " + SentenceToString.toString(sentence));

        // Test getNumberOfWords method
        int numWords = SentenceGetNumberOfWords.getNumberOfWords(sentence);
        System.out.println("Number of words: " + numWords);

        // Test longestWord method
        String longestWord = SentenceLongestWord.longestWord(sentence);
        System.out.println("Longest word: " + longestWord);

        // Test clone method
        Sentence clonedSentence = SentenceClone.clone(sentence);
        System.out.println("Cloned Sentence: " + SentenceToString.toString(clonedSentence));

        // Test merge method
        Sentence otherSentence = new Sentence();
        SentenceAddWord.addWord(otherSentence, "more");
        SentenceAddWord.addWord(otherSentence, "words");
        SentenceAddPunctuation.addPunctuation(otherSentence, "!");
        System.out.println("Other Sentence: " + SentenceToString.toString(otherSentence));

        Sentence mergedSentence = SentenceMerge.merge(sentence, otherSentence);
        System.out.println("Merged Sentence: " + SentenceToString.toString(mergedSentence));
    }

    private static void runTests() {
        Result result = JUnitCore.runClasses(test.class);

        if (result.wasSuccessful()) {
            System.out.println("All tests passed :)");
        } else {
            System.out.println("Test failures:");
            for (org.junit.runner.notification.Failure failure : result.getFailures()) {
                System.out.println(failure.toString());
            }
        }
    }
}
