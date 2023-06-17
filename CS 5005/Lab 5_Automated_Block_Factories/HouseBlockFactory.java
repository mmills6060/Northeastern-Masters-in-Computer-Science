public class HouseBlockFactory implements Factory {
    private static final int STONE_BLOCKS_REQUIRED = 5;
    private static final int WOOD_BLOCKS_REQUIRED = 10;
    
    private int stoneBlockAccumulator;
    private int woodBlockAccumulator;
    
    public class HouseFactory() {
        stoneBlockAccumulator = 0;
        woodBlockAccumulator = 0;
    }
    
    public void takeResource(Object obj) throws InvalidBlockException {
        if (!(obj instanceof Block)) {
            throw new InvalidBlockException("Invalid object. Only blocks can be accepted.");
        }
        
        Block block = (Block) obj;
        
        switch (block.getType()) {
            case STONE:
                stoneBlockAccumulator++;
                break;
            case WOOD:
                woodBlockAccumulator++;
                break;
            default:
                throw new InvalidBlockException("Invalid block type. Only stone and wood blocks are accepted.");
        }
    }
}
