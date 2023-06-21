/*
Defines a resource and assigns its weight and type. 
*/
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
