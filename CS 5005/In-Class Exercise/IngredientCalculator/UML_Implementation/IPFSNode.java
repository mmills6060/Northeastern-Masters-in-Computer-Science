class IPFSNode {
    private String nodeID;
    private String nodeAddress;
    private boolean isConnected;

    public IPFSNode(String nodeID, String nodeAddress) {
        this.nodeID = nodeID;
        this.nodeAddress = nodeAddress;
        this.isConnected = false;
    }

    public void connect() {
        // Code to connect to the IPFS network
        isConnected = true;
        System.out.println("Connected to IPFS node: " + nodeID);
    }

    public void disconnect() {
        // Code to disconnect from the IPFS network
        isConnected = false;
        System.out.println("Disconnected from IPFS node: " + nodeID);
    }

    // Getters and setters

    public String getNodeID() {
        return nodeID;
    }

    public void setNodeID(String nodeID) {
        this.nodeID = nodeID;
    }

    public String getNodeAddress() {
        return nodeAddress;
    }

    public void setNodeAddress(String nodeAddress) {
        this.nodeAddress = nodeAddress;
    }

    public boolean isConnected() {
        return isConnected;
    }
}