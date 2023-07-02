import static org.junit.Assert.assertNotSame;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;


public class SentenceTest {

    @Test
    public void testGetStringRepresentation() {
        Node emptyNode = new EmptyNode();
        assertEquals(null, emptyNode.getStringRepresentation());
    }
    @Test
    public void testPunctuationNode() 
    {
        Node punctuationNode = new PunctuationNode('!');
        org.junit.jupiter.api.Assertions.assertEquals("!", punctuationNode.getStringRepresentation());
    }

   @Test
    public void testAddWord() {
        Sentence sentence = new Sentence(new EmptyNode());
        sentence.addWord("Hello");
        sentence.addWord("world");
        assertEquals(2, sentence.getNumberOfWords());
    }

    @Test
    public void testAddPunctuation() {
        Sentence sentence = new Sentence(new EmptyNode());
        sentence.addPunctuation('!');
        sentence.addWord("Hello");
        assertEquals("Hello!", sentence.toString());
    }

    @Test
    public void testGetNumberOfWords() {
        Sentence sentence = new Sentence(new EmptyNode());
        sentence.addWord("This");
        sentence.addWord("is");
        sentence.addWord("a");
        sentence.addWord("sentence");
        assertEquals(4, sentence.getNumberOfWords());
    }

    @Test
    public void testLongestWord() {
        Sentence sentence = new Sentence(new EmptyNode());
        sentence.addWord("Hello");
        sentence.addWord("world");
        sentence.addWord("beautiful");
        assertEquals("beautiful", sentence.longestWord());
    }

    @Test
    public void testToString() {
        Sentence sentence = new Sentence(new EmptyNode());
        sentence.addWord("Hello");
        sentence.addWord("world");
        sentence.addPunctuation('!');
        assertEquals("Hello world!", sentence.toString());
    }

    @Test
    public void testClone() {
        Sentence sentence = new Sentence(new EmptyNode());
        sentence.addWord("Hello");
        sentence.addWord("world");

        Sentence clonedSentence = sentence.clone();
        assertEquals(sentence.toString(), clonedSentence.toString());
        assertNotSame(sentence, clonedSentence);
    }

    @Test
    public void testMerge() {
        Sentence sentence1 = new Sentence(new EmptyNode());
        sentence1.addWord("Hello");

        Sentence sentence2 = new Sentence(new EmptyNode());
        sentence2.addWord("world");

        Sentence mergedSentence = sentence1.merge(sentence2);
        assertEquals("Hello world", mergedSentence.toString());
    }
    @Test
    public void testWordNode() {
        Node wordNode = new WordNode("Hello");
        org.junit.jupiter.api.Assertions.assertEquals("Hello", wordNode.getValue());
    }
    @Test
    public void testGetWord() {
        Node wordNode = new WordNode("Hello");
        assertEquals("Hello", ((WordNode) wordNode).getWord());
    }

    @Test
    public void testGetStringRepresentationword() {
        Node wordNode = new WordNode("Hello");
        assertEquals("Hello", wordNode.getStringRepresentation());
    }

    @Test
    public void testCloneNode() {
        Node wordNode = new WordNode("Hello");
        Node clonedNode = wordNode.cloneNode();
        assertEquals("Hello", clonedNode.getValue());
        assertNotSame(wordNode, clonedNode);
    }

    @Test
    public void testwordMerge() {
        Node wordNode = new WordNode("Hello");
        Node otherNode = new PunctuationNode('!');
        Node mergedNode = wordNode.merge(otherNode);
        assertEquals('!', mergedNode.getValue());
        assertNotSame(wordNode, mergedNode);
    }
}