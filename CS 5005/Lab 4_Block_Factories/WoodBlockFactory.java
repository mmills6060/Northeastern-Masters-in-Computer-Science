import java.util.Random;
import java.lang.Math;

/*
creates a class woodblockfactory


*/
public class WoodBlockFactory implements Factory {
    private ResourceBin resourceBin;

    public WoodBlockFactory() {
        this.resourceBin = new ResourceBin();
    }

    @Override
    public void takeResource(Resource resource) {
        resourceBin.addResource(resource.getWeight());
    }

    public Block produce() {
        try {
            return resourceBin.produceBlock();
        } catch (InsufficientWeightException e) {
            System.out.println(e.getMessage());
            return null;
        }
    }

    @Override
    public void displayInventory() {
    }
}




