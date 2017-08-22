package volcano.sample.tuning.sample2;

/***
 * for system those can only run serials
 * @author ehuakch
 *
 */
public class Tuning {
    
    TuningFactor x;
    SampleTuningSystem sys;
    StepCloseTuningAlgorithm alg;

    public TuningFactor run() {

        TuningSample y = null;
        while (true) {
            int delta = 0;
            sys.start(x);
            y = sys.get();

            try {
                delta = alg.ask(x, y);
            } catch (StepCloseTuningAlgorithm.MeetConditionEx e) {
                System.out.println("Tuning result:  " + x);
                break;
            }
            x.adjust( delta);
        }
        return x;
    }

    public SampleTuningSystem getSys() {
        return sys;
    }

    public void setSys(SampleTuningSystem sys) {
        this.sys = sys;
    }

    public StepCloseTuningAlgorithm getAlg() {
        return alg;
    }

    public void setAlg(StepCloseTuningAlgorithm alg) {
        this.alg = alg;
    }

}
