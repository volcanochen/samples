package volcano.sample.tuning.sample2;

import volcano.sample.tuning.sample2.TuningAlgorithm.MeetConditionEx;

public abstract class TuningAlgorithm {

    public interface IStopCondition {

        void input(TuningFactor x, TuningSample y);

        boolean isStop();

    }

    IStopCondition stop;

    class MeetConditionEx extends Exception {

    }

    public  TuningAdjustMethod ask(TuningFactor x, TuningSample y) throws MeetConditionEx{
        stop.input(x,y);
        if (stop.isStop()){
            System.out.println("TuningAlgorithm stop condition met ");
            throw new MeetConditionEx();
        }
        return process(x,y);
    };

    private abstract int process(TuningFactor x, TuningSample y);

    public IStopCondition getStop() {
        return stop;
    }

    public void setStop(IStopCondition stop) {
        this.stop = stop;
    }
}
