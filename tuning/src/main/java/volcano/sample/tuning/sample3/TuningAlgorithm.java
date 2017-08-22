package volcano.sample.tuning.sample3;


public class TuningAlgorithm {

    public interface IStopCondition{

        void input(Double x, Double y);

        boolean isStop();
        
    }
    IStopCondition stop;
    class MeetConditionEx extends Exception{
        
    }
    public Double ask(Double x, Double y) throws MeetConditionEx {
        
        stop.input(x,y);
        if (stop.isStop()){
            System.out.println("TuningAlgorithm stop condition met ");
            throw new MeetConditionEx();
        }
        return process(x,y);
    }
    
    private Double process(Double x, Double y) {
        System.out.println("TuningAlgorithm processing " + x + " " + y);

        return 0.0;
    }

    public IStopCondition getStop() {
        return stop;
    }

    public void setStop(IStopCondition stop) {
        this.stop = stop;
    }

}
