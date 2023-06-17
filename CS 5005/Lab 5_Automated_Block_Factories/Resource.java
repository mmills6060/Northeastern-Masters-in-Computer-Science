import java.util.Random;
import java.lang.Math;

/*
creates a class resource

this class will be like a raw material. I can have 
any amount including partial amounts. Thus, this will
need to be a double. We'll use weight to record
this amount, but we'll ignore what unit that weight is in.
You will need a constructor for this Resource that takes a
weight and a type.

a resource has a weight and a resource type of stone
or wood. I need to make sure the weight and type can't 
be changed by other objects, but can be retrieved if 
needed.

I am also going to need a method to add to an amount of 
an existing resource of the same type. That just means I 
increase th weight of that resource. I also want to be able
to subtract from a resource by reducing the weight.
*/

public class Resource {
    public double weight;
    public ResourceType type;

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

    public void addWeight(double amount) {
        if (amount >= 0) {
            double updatedWeight = weight + amount;
            // Do any additional checks or operations here
            weight = updatedWeight; // Assign the new value back to the field
        }
    }
    
    public void subtractWeight(double amount) {
        if (amount >= 0) {
            double updatedWeight = weight - amount;
            // Do any additional checks or operations here
            weight = updatedWeight; // Assign the new value back to the field
        }
    }
}

