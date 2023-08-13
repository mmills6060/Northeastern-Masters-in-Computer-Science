public class Main {
    public static void main(String[] args) {
        TennisMatchModel model = new TennisMatchModel();
        TennisMatchView view = new TennisMatchView();
        TennisMatchController controller = new TennisMatchController(model, view);
        controller.run();
    }
}
