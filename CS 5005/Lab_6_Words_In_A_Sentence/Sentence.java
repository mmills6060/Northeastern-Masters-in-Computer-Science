public class Sentence {
    private Node head;

    public Sentence() {
        this.head = new EmptyNode();
    }

    public void addWord(String word) {
        Node newNode = new WordNode(word);

        if (head instanceof EmptyNode) {
            head = newNode;
        } else {
            Node current = head;
            while (!(current instanceof EmptyNode)) {
                current = current.getNext();
            }
            current.setNext(newNode);
        }
    }

    public void addPunctuation(String punctuation) {
        Node newNode = new PunctuationNode(punctuation);

        if (head instanceof EmptyNode) {
            head = newNode;
        } else {
            Node current = head;
            while (!(current instanceof EmptyNode)) {
                current = current.getNext();
            }
            current.setNext(newNode);
        }
    }

    public int getNumberOfWords() {
        int count = 0;
        Node current = head;
        while (!(current instanceof EmptyNode)) {
            if (current instanceof WordNode) {
                count++;
            }
            current = current.getNext();
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
            current = current.getNext();
        }
        return longest;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node current = head;
        while (!(current instanceof EmptyNode)) {
            if (current instanceof WordNode) {
                sb.append(current.getStringValue()).append(" ");
            } else if (current instanceof PunctuationNode) {
                sb.append(current.getStringValue());
            }
            current = current.getNext();
        }

        if (sb.length() > 0) {
            sb.deleteCharAt(sb.length() - 1);
            if (current instanceof PunctuationNode) {
                sb.append(current.getStringValue());
            } else {
                sb.append(".");
            }
        }

        return sb.toString();
    }

    public Sentence clone() {
        Sentence clone = new Sentence();
        Node current = head;
        while (!(current instanceof EmptyNode)) {
            if (current instanceof WordNode) {
                clone.addWord(((WordNode) current).getWord());
            } else if (current instanceof PunctuationNode) {
                clone.addPunctuation(((PunctuationNode) current).getPunctuation());
            }
            current = current.getNext();
        }
        return clone;
    }

    public Sentence merge(Sentence other) {
        Sentence merged = new Sentence();
        Node current = head;
        while (!(current instanceof EmptyNode)) {
            if (current instanceof WordNode) {
                merged.addWord(((WordNode) current).getWord());
            } else if (current instanceof PunctuationNode) {
                merged.addPunctuation(((PunctuationNode) current).getPunctuation());
            }
            current = current.getNext();
        }

        current = other.head;
        while (!(current instanceof EmptyNode)) {
            if (current instanceof WordNode) {
                merged.addWord(((WordNode) current).getWord());
            } else if (current instanceof PunctuationNode) {
                merged.addPunctuation(((PunctuationNode) current).getPunctuation());
            }
            current = current.getNext();
        }

        return merged;
    }
}