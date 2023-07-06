package essay_code2.Interface;
// interface declares a method signature, playTennis().
// class that implement this interface must provide implementations for these methods
interface Interface {
    void playTennis();
}

class ProfessionalPlayer implements TennisPlayer {
    private String name;

    public ProfessionalPlayer(String name) {
        this.name = name;
    }

    @Override
    public void playTennis() {
        System.out.println(name + " is playing tennis as a professional player.");
    }
}
