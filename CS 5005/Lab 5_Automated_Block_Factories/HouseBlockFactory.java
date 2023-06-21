public class HouseBlockFactory implements Factory {
    private int stoneBlockAccumulator;
    private int woodBlockAccumulator;

    @Override
    public void takeResource(Object resource) {
        try {
            if (resource instanceof Block) {
                Block block = (Block) resource;
                ResourceType type = block.getType();

                switch (type) {
                    case STONE:
                        stoneBlockAccumulator++;
                        break;
                    case WOOD:
                        woodBlockAccumulator++;
                        break;
                }
            } else {
                // Handle the case where the resource is not a Block (if needed)
                System.out.println("Invalid resource type: " + resource.getClass().getName());
            }
        } catch (IllegalArgumentException e) {
            System.out.println("Invalid resource: " + resource);
            e.printStackTrace(); // Print the stack trace for debugging purposes
        }
    }

    @Override
    public Block produce() {
        if (stoneBlockAccumulator >= Const.STONE_WEIGHT && woodBlockAccumulator >= Const.WOOD_WEIGHT) {
            stoneBlockAccumulator -= Const.STONE_WEIGHT;
            woodBlockAccumulator -= Const.WOOD_WEIGHT;
            return new HouseBlock(null, null);
        } else {
            return new NullBlock(); // Return a special NullBlock indicating that a block couldn't be produced
        }
    }

    @Override
    public void displayInventory() {
        System.out.println("Stone block accumulator: " + stoneBlockAccumulator);
        System.out.println("Wood block accumulator: " + woodBlockAccumulator);
    }
}
