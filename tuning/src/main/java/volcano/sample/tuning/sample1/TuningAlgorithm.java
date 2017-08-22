package volcano.sample.tuning.sample1;

public class TuningAlgorithm {

    public interface IStopCondition{

        void input(int x, int y);

        boolean isStop();
        
    }
    IStopCondition stop;
    class MeetConditionEx extends Exception{
        
    }
    public int ask(int x, int y) throws MeetConditionEx {
        
        stop.input(x,y);
        if (stop.isStop()){
            System.out.println("TuningAlgorithm stop condition met ");
            throw new MeetConditionEx();
        }
        return process(x,y);
    }
    
    private int process(int x, int y) {
        System.out.println("TuningAlgorithm processing " + x + " " + y);

        return 0;
    }

    public IStopCondition getStop() {
        return stop;
    }

    public void setStop(IStopCondition stop) {
        this.stop = stop;
    }

}
