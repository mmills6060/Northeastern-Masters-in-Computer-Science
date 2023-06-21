public abstract class Block {
    private double weight;
    private ResourceType type;

    public Block(double weight, ResourceType type) {
        this.weight = weight;
        this.type = type;
    }

    public double getWeight() {
        return weight;
    }

    public ResourceType getType() {
        return type;
    }
}