import java.util.Random;
import java.lang.Math;

/*
creates a stone block factory class

*/
public class StoneBlockFactory implements Factory<Block>, Factory {
    private int stoneCount;

    public StoneBlockFactory() {
        stoneCount = 0;
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

        if (resource.getType() != ResourceType.STONE) {
            throw new InvalidResourceException("Invalid resource type. Only stone resources are accepted.");
        }

        stoneCount++;
    }

    @Override
    public Block produce() {
        if (stoneCount > 0) {
            stoneCount--;
            return new Block(ResourceType.STONE);
        }

        return null;
    }
}





