package volcano.sample.tuning.sample2.onevariable;

import java.util.concurrent.Callable;

import volcano.sample.tuning.sample2.framework.ITuningFactor;
import volcano.sample.tuning.sample2.framework.ITuningSystem;

public class SampleTuningSystem implements ITuningSystem {
    Double x;
    Double y;

    class SystemA implements Callable<Double> {
        Double x;

        SystemA(Double x) {
            this.x = x;
        }

        @Override
        public Double call() throws Exception {
            
            //Thread.sleep(50);
            Double te = Double.valueOf(-(x - 3) * (x - 3) + 40.0);
            System.out.println(" ------  run f("+x +") = "+ te);
            return te;
        }

    };

    @Override
    public void start(final ITuningFactor x) {
        TuningFactor t = (TuningFactor)x;
        Callable<Double> s = new SampleTuningSystem.SystemA(t.getFactor());
        try {
            y = s.call();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    @Override
    public TuningSample get() {
        return new TuningSample(y);
    }

}