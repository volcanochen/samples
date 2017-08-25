package volcano.sample.tuning.sample2.twovarianble;

import java.util.concurrent.Callable;

import volcano.sample.tuning.sample2.framework.ITuningFactor;
import volcano.sample.tuning.sample2.framework.ITuningSystem;

public class SampleTuningSystem2Variables implements ITuningSystem {
    Double x;
    Double y;
    Double z;

   class SystemA implements Callable<Double> {
        Double x;
        Double y;

        SystemA(Double x, Double y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public Double call() throws Exception {
            //Thread.sleep(50);
            Double te = Double.valueOf((x - 10) * (x - 10) + 0.7*(y-8)*(y-8) );
            System.out.println(" ------  run f("+x +","+ y  +") = "+ te);
            return te;
        }

    };

    @Override
    public void start(final ITuningFactor x) {
        volcano.sample.tuning.sample2.twovarianble.TuningFactor t = (volcano.sample.tuning.sample2.twovarianble.TuningFactor)x;
        Callable<Double> s = new SystemA(t.getFactor()[0],t.getFactor()[1]);
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