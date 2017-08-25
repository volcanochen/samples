package volcano.sample.tuning.sample1;

import java.util.ArrayList;

import org.junit.Test;

import volcano.sample.tuning.sample1.SampleTuningSystem;
import volcano.sample.tuning.sample1.Tuning;
import volcano.sample.tuning.sample1.TuningAlgorithm;
import volcano.sample.tuning.sample1.TuningAlgorithm.IStopCondition;

public class TuningTest {

    @Test
    public void testbasic() {
        // y = - (x - 3)^2 + 30, find max Y

        Tuning tuning = new Tuning();

        TuningAlgorithm alg1 = new TuningAlgorithm();
        IStopCondition howToStop = new IStopCondition() {
            ArrayList<Integer> result = new ArrayList<>();

            public void input(int x, int y) {
                result.add(y);
            }

            public boolean isStop() {
                if (result.size() > 10) {
                    return true;
                }
                return false;
            }
        };
        alg1.setStop(howToStop);

        tuning.setAlg(alg1);

        SampleTuningSystem sys = new SampleTuningSystem();

        tuning.setSys(sys);
        int x = tuning.run();

    }

}
