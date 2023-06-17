import java.util.Random;
import java.lang.Math;

/*
creates a class woodblockfactory


*/
public class WoodBlockFactory implements Factory<Block>, Factory {
    private int woodCount;

    public WoodBlockFactory() {
        woodCount = 0;
    }

    @Override
    public void takeResource(Object obj) throws InvalidResourceException {
        if (obj == null) {
            throw new InvalidResourceException("Invalid resource. Null object cannot be accepted.");
        }

        if (!(obj instanceof Resource)) {
            throw new InvalidResourceException("Invalid resource. Only Resource objects can be accepted.");
        }

        Resource resource = (Resource) obj;

        if (resource.getType() != ResourceType.WOOD) {
            throw new InvalidResourceException("Invalid resource type. Only wood resources are accepted.");
        }

        woodCount++;
    }

    @Override
    public Block produce() {
        if (woodCount > 0) {
            woodCount--;
            return new Block(ResourceType.WOOD);
        }

        return null;
    }
}





