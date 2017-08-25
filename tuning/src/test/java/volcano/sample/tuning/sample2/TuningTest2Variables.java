package volcano.sample.tuning.sample2;

import org.junit.Test;

import volcano.sample.tuning.sample2.algorithm.RandomTuningAlgorithm;
import volcano.sample.tuning.sample2.framework.Tuning;
import volcano.sample.tuning.sample2.twovarianble.SampleTuningSystem2Variables;
import volcano.sample.tuning.sample2.twovarianble.TuningFactor;


public class TuningTest2Variables {

    @Test
    public void testTwoVariable() {

        Tuning tuning = new Tuning(new TuningFactor(new Double[]{0.0,0.0}));

        RandomTuningAlgorithm alg1 = new RandomTuningAlgorithm();
        SampleTuningSystem2Variables sys = new SampleTuningSystem2Variables();
        alg1.setSize(1000);
        tuning.setAlg(alg1);
        tuning.setSys(sys);
        Double[] factor = ((TuningFactor)tuning.run()).getFactor();
        
        
    }

}
