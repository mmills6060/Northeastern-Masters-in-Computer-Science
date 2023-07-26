package second_try;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class test {

    @Test
    public void testClone() {
        List<String> original = new ArrayList<>();
        original.add("This");
        original.add("is");
        original.add("a");
        original.add("sentence");
        original.add(".");

        List<String> duplicate = Clone.clone(original);

        assertEquals(original, duplicate);
    }

    @Test
    public void testGetNumberOfWords() {
        getNumberOfWords.ListNode sentence = new getNumberOfWords.ListNode("This");
        sentence.next = new getNumberOfWords.ListNode("is");
        sentence.next.next = new getNumberOfWords.ListNode("a");
        sentence.next.next.next = new getNumberOfWords.ListNode("sentence");
        sentence.next.next.next.next = new getNumberOfWords.ListNode(".");

        int numWords = getNumberOfWords.getNumberOfWordsInSentence(sentence);

        assertEquals(5, numWords);
    }

    @Test
    public void testMerge() {
        merge.ListNode sentence1 = new merge.ListNode("Andre");
        sentence1.next = new merge.ListNode("Agassi");
        sentence1.next.next = new merge.ListNode("is");
        sentence1.next.next.next = new merge.ListNode("good");
        sentence1.next.next.next.next = new merge.ListNode("at");
        sentence1.next.next.next.next.next = new merge.ListNode("tennis");

        merge.ListNode sentence2 = new merge.ListNode("Andy");
        sentence2.next = new merge.ListNode("Murray");
        sentence2.next.next = new merge.ListNode("is");
        sentence2.next.next.next = new merge.ListNode("also");
        sentence2.next.next.next.next = new merge.ListNode("good");
        sentence2.next.next.next.next.next = new merge.ListNode("at");
        sentence2.next.next.next.next.next.next = new merge.ListNode("tennis");

        merge.ListNode mergedNode = merge.mergeSentences(sentence1, sentence2);

        // Create a list from the merged nodes to compare with the expected list
        List<String> mergedList = new ArrayList<>();
        while (mergedNode != null) {
            mergedList.add(mergedNode.data);
            mergedNode = mergedNode.next;
        }

        List<String> expectedMergedList = Arrays.asList("Andre", "Agassi", "is", "good", "at", "tennis", "Andy", "Murray", "is", "also", "good", "at", "tennis");
        assertEquals(expectedMergedList, mergedList);
    }

    @Test
    public void testLongestWord() {
        longestWord.ListNode sentence3 = new longestWord.ListNode("Roger");
        sentence3.next = new longestWord.ListNode("Federer");
        sentence3.next.next = new longestWord.ListNode("is");
        sentence3.next.next.next = new longestWord.ListNode("a");
        sentence3.next.next.next.next = new longestWord.ListNode("good");
        sentence3.next.next.next.next.next = new longestWord.ListNode("tennis");
        sentence3.next.next.next.next.next.next = new longestWord.ListNode("player");
        sentence3.next.next.next.next.next.next.next = new longestWord.ListNode("!");

        String longestWordInSentence = longestWord.findLongestWord(sentence3);

        assertEquals("Federer", longestWordInSentence);
    }

    @Test
    public void testToString() {
        toString.ListNode sentence4 = new toString.ListNode("Rafa");
        sentence4.next = new toString.ListNode("Nadal");
        sentence4.next.next = new toString.ListNode("can");
        sentence4.next.next.next = new toString.ListNode("talk");
        sentence4.next.next.next.next = new toString.ListNode("as");
        sentence4.next.next.next.next.next = new toString.ListNode("a");
        sentence4.next.next.next.next.next.next = new toString.ListNode("string");
        sentence4.next.next.next.next.next.next.next = new toString.ListNode("!");

        String sentenceAsString = toString.sentenceToString(sentence4);

        assertEquals(" Rafa Nadal can talk as a string!", sentenceAsString);
    }
}
