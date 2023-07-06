package essay_code2.Interface;

class AmateurPlayer implements TennisPlayer {
    private String name;

    public AmateurPlayer(String name) {
        this.name = name;
    }

    @Override
    public void playTennis() {
        System.out.println(name + " is playing tennis as an amateur player.");
    }
}