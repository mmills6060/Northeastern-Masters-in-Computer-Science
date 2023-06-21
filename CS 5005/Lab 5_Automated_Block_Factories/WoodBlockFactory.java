public class WoodBlockFactory implements Factory {
    private double binWeight;

    public void takeResource(Object resource) {
        if (resource instanceof Resource) {
            Resource woodResource = (Resource) resource;
            if (woodResource.getType() == ResourceType.WOOD) {
                binWeight += woodResource.getWeight();
            } else {
                throw new IllegalArgumentException("Invalid resource type. Expected wood.");
            }
        } else {
            throw new IllegalArgumentException("Invalid resource object. Expected Resource.");
        }
    }

    public Block produce() {
        if (binWeight >= Const.WOOD_BLOCK_WEIGHT) {
            binWeight -= Const.WOOD_BLOCK_WEIGHT;
            return new WoodBlock(binWeight, null);
        } else {
            return null;
        }
    }

    public void displayInventory() {
        System.out.println(binWeight);
    }
}
