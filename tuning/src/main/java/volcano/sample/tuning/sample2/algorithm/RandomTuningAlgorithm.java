package volcano.sample.tuning.sample2.algorithm;

import volcano.sample.tuning.sample2.framework.ITuningAlgorithm;
import volcano.sample.tuning.sample2.framework.ITuningFactor;
import volcano.sample.tuning.sample2.framework.ITuningSample;
import volcano.sample.tuning.sample2.framework.TuningAdjustMethod;
import volcano.sample.tuning.sample2.framework.TuningAdjustMethod.OPCODE;
import volcano.sample.tuning.sample2.framework.TuningAdjustMethod.OPVALUE;

public class RandomTuningAlgorithm extends ITuningAlgorithm {

    //Map<ITuningFactor, ITuningSample> alltries = new HashMap<>();
    private int count = 0;
    private int size = 20;

    private ITuningFactor bestFactor = null;
    private ITuningSample bestSample = null;
    TuningAdjustMethod rand = new TuningAdjustMethod(OPCODE.ADJUST, OPVALUE.STEP_RANDON);
    
    @Override
    public TuningAdjustMethod process(ITuningFactor x, ITuningSample y) {
        count ++;
        if (this.getBestFactor() == null) {
            this.keepBest(x,y);
        } else {
            if (y.isBetter(bestSample)) {
                System.out.println("       *****       the best is " + x.print());
                this.keepBest(x,y);
            }
        }
        return rand;
    }

    @Override
    public boolean isStop() {
        if (count >= size) {
            return true;
        }
        return false;
    }


    public void keepBest(ITuningFactor x,ITuningSample y) {

        bestFactor = x.copy();
        this.bestSample = y.copy();
    }


    @Override
    public String getOutput() {

        return this.getBestFactor().print() + " -> " + this.getBestSample().print();
    }

    public ITuningFactor getBestFactor() {
        return bestFactor;
    }

    public ITuningSample getBestSample() {
        return bestSample;
    }

    public void setBestSample(ITuningSample bestSample) {
        this.bestSample = bestSample;
    }

    @Override
    public ITuningFactor getBest() {
        return this.getBestFactor();
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

}
