package first_try;
/**
 * Author: Michael Arthur Mills 
 * Class: CS 5005 
 * Date: July 1 2023
 */


public class Sentence {
    private Node head;

    public Sentence(Node node) {
        this.head = new EmptyNode();
    }

    public void addWord(String word) {
        Node newNode = new WordNode(word);
        head = head.merge(newNode);
    }

    public void addPunctuation(char punctuation) {
        Node newNode = new PunctuationNode(punctuation);
        head = head.merge(newNode);
    }

    public int getNumberOfWords() {
        int count = 0;
        Node current = head;
        while (!(current instanceof EmptyNode)) {
            if (current instanceof WordNode) {
                count++;
            }
        }
        return count;
    }

    public String longestWord() {
        String longest = "";
        Node current = head;
        while (!(current instanceof EmptyNode)) {
            if (current instanceof WordNode) {
                String word = ((WordNode) current).getWord();
                if (word.length() > longest.length()) {
                    longest = word;
                }
            }
        }
        return longest;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node current = head;
        while (!(current instanceof EmptyNode)) {
            sb.append(current.getStringRepresentation());
            if (!(current instanceof EmptyNode)) {
                sb.append(" ");
            }
        }
        String sentenceString = sb.toString();
        if (!sentenceString.isEmpty() && !isPunctuation(sentenceString.charAt(sentenceString.length() - 1))) {
            sb.append(".");
        }
        return sb.toString();
    }

    public Sentence clone() {
        Sentence clonedSentence = new Sentence(head);
        Node current = head;
        while (!(current instanceof EmptyNode)) {
            clonedSentence.addWord(current.getStringRepresentation());
        }
        return clonedSentence;
    }

    public Sentence merge(Sentence other) {
        Sentence mergedSentence = new Sentence(head);
        Node current = head;
        while (!(current instanceof EmptyNode)) {
            mergedSentence.addWord(current.getStringRepresentation());
        }
        current = other.head;
        while (!(current instanceof EmptyNode)) {
            mergedSentence.addWord(current.getStringRepresentation());
        }
        return mergedSentence;
    }

    private boolean isPunctuation(char c) {
        return c == '.' || c == ',' || c == '!' || c == '?' || c == ';' || c == ':';
    }
}
