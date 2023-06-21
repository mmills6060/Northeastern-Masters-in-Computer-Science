public class Resource {
    private double weight;
    private ResourceType type;

    public Resource(double weight, ResourceType type) {
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
