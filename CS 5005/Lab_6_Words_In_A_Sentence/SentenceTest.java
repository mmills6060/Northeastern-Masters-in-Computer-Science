import org.junit.jupiter.api.Test;

public class SentenceTest {
    
// Test 1 for EmptyNode.java
    @Test
    public void testEmptyNode() {
        Node emptyNode = new EmptyNode();
        org.junit.jupiter.api.Assertions.assertEquals("", emptyNode.getValue());
    }


// Test 2 for EmptyNode.java
    @Test
    public void testEmptyNode2() {
        Node emptyNode = new EmptyNode();
        org.junit.jupiter.api.Assertions.assertEquals(0, emptyNode.count());
    }
// Test 1 for Node.java
    @Test
    public void testNode() {
        Node node = new Node("Hello");
        org.junit.jupiter.api.Assertions.assertEquals("Hello", node.getValue());
    }
// Test 2 for Node.java
    @Test
    public void testNode2() {
        Node node = new Node("Hello");
        org.junit.jupiter.api.Assertions.assertEquals(1, node.count());
    }
// Test 1 fro PunctuationNode.java
    @Test
    public void testPunctuationNode() {
        Node punctuationNode = new PunctuationNode("!");
        org.junit.jupiter.api.Assertions.assertEquals("!", punctuationNode.getValue());
    }
// Test 2 for PunctuationNode.java
    @Test
    public void testPunctuationNode2() {
        Node punctuationNode = new PunctuationNode("!");
        org.junit.jupiter.api.Assertions.assertEquals(1, punctuationNode.count());
    }
// Test 1 for Sentence.java
    @Test
    public void testSentence() {
        Node node = new Node("Hello");
        Sentence sentence = new Sentence(node);
        org.junit.jupiter.api.Assertions.assertEquals("Hello", sentence.toString());
    }
// Test 2 for Sentence.java
    @Test
    public void testSentence2() {
        Node node = new Node("Hello");
        Sentence sentence = new Sentence(node);
        org.junit.jupiter.api.Assertions.assertEquals(1, sentence.getNumberOfWords());
    }
// Test 1 for WordNode.java
    @Test
    public void testWordNode() {
        Node wordNode = new WordNode("Hello");
        org.junit.jupiter.api.Assertions.assertEquals("Hello", wordNode.getValue());
    }
// Test 2 for WordNode.java
    @Test
    public void testWordNode2() {
        Node wordNode = new WordNode("Hello");
        org.junit.jupiter.api.Assertions.assertEquals(1, wordNode.count());
    }

}