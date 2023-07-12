public class Controller {
    /**
     * First, we need to declare our objects
     * as class attributes.
     */
    private Model model;
    private View view;
    /**
     * You should then construct the controller,
     * passing your objects through and binding them.
     */
    public Controller(Model model, View view) {
        this.model = model;
        this.view = view;
    }
    /**
     * Next, determine setters and getters needed for the
     * Model
     */
    public void setModelAttribute(String attribute) {
        model.setAttribute(attribute);
    }
    /**
     * Finally, you will need a method to refresh
     * or update the view.
     */
    public void updateView() {
        view.render(model); // Pass the model to the view for rendering/updating
    }
}
