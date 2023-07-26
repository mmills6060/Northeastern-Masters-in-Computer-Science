class FileStorageSystem {
    private ArrayList<IPFSNode> storageNodes;

    public FileStorageSystem() {
        storageNodes = new ArrayList<>();
    }

    public void addNode(IPFSNode node) {
        storageNodes.add(node);
    }

    public void uploadFile(FileUpload file) {
        // Code to upload the file to the decentralized storage system
        for (IPFSNode node : storageNodes) {
            if (node.isConnected()) {
                // Upload the file to the connected node
                System.out.println("File uploaded to IPFS node: " + node.getNodeID());
                return;
            }
        }
        System.out.println("No connected nodes available to upload the file.");
    }

    // Other methods for file retrieval, etc.

    public void retrieveFile(String fileName) {
        // Code to retrieve the file from the decentralized storage system
        // ...
    }
}