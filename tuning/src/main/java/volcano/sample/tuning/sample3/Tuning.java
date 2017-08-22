package volcano.sample.tuning.sample3;


public class Tuning {
    
    double x;
    SampleTuningSystem sys;
    TuningAlgorithm alg;

    public Double run() {

        double y = 0;
        while (true) {
            Double delta = 0.0;
            sys.start(x);
            y = sys.get();

            try {
                delta = alg.ask(x, y);
            } catch (TuningAlgorithm.MeetConditionEx e) {
                System.out.println("Tuning result:  " + x);
                break;
            }
            x += delta;
        }
        return x;
    }

    public SampleTuningSystem getSys() {
        return sys;
    }

    public void setSys(SampleTuningSystem sys) {
        this.sys = sys;
    }

    public TuningAlgorithm getAlg() {
        return alg;
    }

    public void setAlg(TuningAlgorithm alg) {
        this.alg = alg;
    }

}
