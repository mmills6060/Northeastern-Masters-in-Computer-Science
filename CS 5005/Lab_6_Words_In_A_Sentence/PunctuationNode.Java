public class PunctuationNode implements Node {
    private String punctuation;

    public PunctuationNode(String punctuation) {
        this.punctuation = punctuation;
    }

    public String getValue() {
        return punctuation;
    }
}
