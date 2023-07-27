package second_try;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class test {

    private Sentence sentence;

    @Before
    public void setUp() {
        sentence = new Sentence();
    }

    @Test
    public void testAddWord() {
        SentenceAddWord.addWord(sentence, "Tennis");
        SentenceAddWord.addWord(sentence, "is");
        SentenceAddWord.addWord(sentence, "a");
        SentenceAddWord.addWord(sentence, "sport");

        assertEquals("Tennis is a sport", SentenceToString.toString(sentence));
    }

    @Test
    public void testAddPunctuation() {
        SentenceAddPunctuation.addPunctuation(sentence, ".");
        SentenceAddPunctuation.addPunctuation(sentence, "!");
        SentenceAddPunctuation.addPunctuation(sentence, "?");

        assertEquals(".!?", SentenceToString.toString(sentence));
    }

    @Test
    public void testToString() {
        SentenceAddWord.addWord(sentence, "Testing");
        SentenceAddWord.addWord(sentence, "that");
        SentenceAddWord.addWord(sentence, "string");
        SentenceAddWord.addWord(sentence, "works");
        SentenceAddPunctuation.addPunctuation(sentence, ".");

        assertEquals("Testing that string works.", SentenceToString.toString(sentence));
    }

    @Test
    public void testGetNumberOfWords() {
        SentenceAddWord.addWord(sentence, "testing");
        SentenceAddWord.addWord(sentence, "that");
        SentenceAddWord.addWord(sentence, "numberofwords");
        SentenceAddWord.addWord(sentence, "works");
        SentenceAddPunctuation.addPunctuation(sentence, ".");

        assertEquals(4, SentenceGetNumberOfWords.getNumberOfWords(sentence));
    }

    @Test
    public void testLongestWord() {
        SentenceAddWord.addWord(sentence, "testing");
        SentenceAddWord.addWord(sentence, "that");
        SentenceAddWord.addWord(sentence, "longestword");
        SentenceAddWord.addWord(sentence, "works");
        SentenceAddPunctuation.addPunctuation(sentence, ".");

        assertEquals("longestword", SentenceLongestWord.longestWord(sentence));
    }

    @Test
    public void testClone() {
        SentenceAddWord.addWord(sentence, "testing");
        SentenceAddWord.addWord(sentence, "that");
        SentenceAddWord.addWord(sentence, "clone");
        SentenceAddWord.addWord(sentence, "works");
        SentenceAddPunctuation.addPunctuation(sentence, ".");

        Sentence clonedSentence = SentenceClone.clone(sentence);
        assertEquals(SentenceToString.toString(sentence), SentenceToString.toString(clonedSentence));
    }

    @Test
    public void testMerge() {
        SentenceAddWord.addWord(sentence, "Testing");
        SentenceAddWord.addWord(sentence, "that");
        SentenceAddWord.addWord(sentence, "merge");
        SentenceAddWord.addWord(sentence, "works");

        Sentence otherSentence = new Sentence();
        SentenceAddWord.addWord(otherSentence, "Another");
        SentenceAddWord.addWord(otherSentence, "sentence");

        Sentence mergedSentence = SentenceMerge.merge(sentence, otherSentence);
        assertEquals("Testing that merge works Another sentence", SentenceToString.toString(mergedSentence));
    }
}
