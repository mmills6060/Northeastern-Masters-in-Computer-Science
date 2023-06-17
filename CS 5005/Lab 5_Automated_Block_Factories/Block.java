import java.util.Random;
import java.lang.Math;

/*
creates a class block

a class that should never be instantiated

it contains a weight and a resource type of stone or wood

the constructor for a block only accepts a resource type 
and weight

I need to make sure other class objects can get th type
and weight of a block, but not set them. I need to create an
appropriate toString override as well. 
*/

public class Block {
    private final ResourceType type;
    private final double weight;


    public Block(ResourceType type, double weight) {
        this.type = type;
        this.weight = weight;
    }

    public ResourceType getType() {
        return type;
    }

    public double getWeight() {
        return weight;
    }

    @Override
    public String toString() {
        return "Block [type=" + type + ", weight=" + weight + "]";
    }
}

