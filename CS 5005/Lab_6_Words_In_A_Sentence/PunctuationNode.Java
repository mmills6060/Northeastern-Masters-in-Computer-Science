public class PunctuationNode implements Node {
    private String punctuation;

    public PunctuationNode(String punctuation) {
        this.punctuation = punctuation;
    }

    public String getPunctuation() {
        return punctuation;
    }

    @Override
    public String getStringValue() {
        return punctuation;
    }
}