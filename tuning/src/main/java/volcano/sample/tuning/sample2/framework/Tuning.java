package volcano.sample.tuning.sample2.framework;

import volcano.sample.tuning.sample2.algorithm.RandomTuningAlgorithm;
import volcano.sample.tuning.sample2.framework.TuningAdjustMethod.OPCODE;
import volcano.sample.tuning.sample2.framework.TuningAdjustMethod.OPVALUE;
import volcano.sample.tuning.sample2.onevariable.TuningFactor;

/***
 * for system those can only run serials
 * 
 * @author ehuakch
 *
 */
public class Tuning {

    ITuningFactor x;
    ITuningSystem sys;
    RandomTuningAlgorithm alg;

    public Tuning(ITuningFactor x) {
        this.x = x;
    }

    public ITuningFactor run() {

        ITuningSample y = null;
        TuningAdjustMethod algMethod = new TuningAdjustMethod(OPCODE.ADJUST, OPVALUE.MIN);
        while (!algMethod.isEnd()) {
            x.adjust(algMethod.getOperationValue());
            sys.start(x);
            y = sys.get();
            algMethod = alg.ask(x, y);
        }
        System.out.println("result:  " + alg.getOutput());
        return x;
    }

    public ITuningSystem getSys() {
        return sys;
    }

    public void setSys(ITuningSystem sys) {
        this.sys = sys;
    }

    public RandomTuningAlgorithm getAlg() {
        return alg;
    }

    public void setAlg(RandomTuningAlgorithm alg) {
        this.alg = alg;
    }

}
