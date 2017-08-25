package volcano.sample.tuning.sample2;

import org.junit.Test;

import volcano.sample.tuning.sample2.algorithm.RandomTuningAlgorithm;
import volcano.sample.tuning.sample2.framework.Tuning;
import volcano.sample.tuning.sample2.onevariable.SampleTuningSystem;
import volcano.sample.tuning.sample2.onevariable.TuningFactor;


public class TuningTest2 {

    @Test
    public void testOneVariable() {
        // y = - (x - 3)^2 + 30, find max Y

        Tuning tuning = new Tuning(new TuningFactor(0.0));

        RandomTuningAlgorithm alg1 = new RandomTuningAlgorithm();
        SampleTuningSystem sys = new SampleTuningSystem();
        alg1.setSize(100);
        tuning.setAlg(alg1);
        tuning.setSys(sys);
        double x = ((TuningFactor)tuning.run()).getFactor();
        
    }

}
