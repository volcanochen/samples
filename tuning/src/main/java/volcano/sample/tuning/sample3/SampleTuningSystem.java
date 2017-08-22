package volcano.sample.tuning.sample3;

import java.util.concurrent.Callable;

public class SampleTuningSystem {
    Double x;
    Double y;

    class SystemA implements Callable<Double> {
        Double x;

        SystemA(Double x) {
            this.x = x;
        }

        @Override
        public Double call() throws Exception {
            Thread.sleep(1000);
            return Double.valueOf(-(x - 3) * (x - 3) + 40.0);
        }

    };

    void start(Double x) {
        Callable<Double> s = new SampleTuningSystem.SystemA(x);
        try {
            y = s.call();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    Double get() {
        return y;
    }

}