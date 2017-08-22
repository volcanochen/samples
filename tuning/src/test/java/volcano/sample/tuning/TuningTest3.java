package volcano.sample.tuning;

import java.util.ArrayList;

import org.junit.Test;

import volcano.sample.tuning.sample3.SampleTuningSystem;
import volcano.sample.tuning.sample3.Tuning;
import volcano.sample.tuning.sample3.TuningAlgorithm;
import volcano.sample.tuning.sample3.TuningAlgorithm.IStopCondition;

public class TuningTest3 {

    @Test
    public void testbasic() {
        // y = - (x - 3)^2 + 30, find max Y

        Tuning tuning = new Tuning();

        TuningAlgorithm alg1 = new TuningAlgorithm();
        IStopCondition howToStop = new IStopCondition() {
            ArrayList<Double> result = new ArrayList<>();

            public boolean isStop() {
                if (result.size() > 10) {
                    return true;
                }
                return false;
            }

            @Override
            public void input(Double x, Double y) {
                result.add(y);

            }
        };
        alg1.setStop(howToStop);

        tuning.setAlg(alg1);

        SampleTuningSystem sys = new SampleTuningSystem();

        tuning.setSys(sys);
        Double x = tuning.run();

    }

}
