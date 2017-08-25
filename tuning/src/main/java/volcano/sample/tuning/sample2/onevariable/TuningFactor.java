package volcano.sample.tuning.sample2.onevariable;

import java.util.Random;

import volcano.sample.tuning.sample2.framework.ITuningFactor;
import volcano.sample.tuning.sample2.framework.TuningAdjustMethod;

public class TuningFactor implements ITuningFactor {
    
    double interval = 0.1;
    double  factor;
    private int  min = -10;
    private int max = 30;
    
    public TuningFactor(double factor){
        this.factor = factor;
    }
    public double getFactor() {
        return factor;
    }

    public void setFactor(double factor) {
        this.factor = factor;
    }
    @Override
    public void adjust(TuningAdjustMethod.OPVALUE delta) {
        switch (delta){
        case STEP_BACK:
            this.factor -= interval ;
            break;
        case STEP_FORWARD:
            this.factor += interval ;
            break;
        case STEP_RANDON:
            this.factor = (new Random()).nextDouble() * (max - min) + min;
            break;
        case MAX:
            this.factor = max;
            break;
        case MIN:
            this.factor = min;
            break;
        default:
            break;
        
        }

    }
    @Override
    public String print() {
        return String.format("%.2f", this.factor);
    }
    @Override
    public ITuningFactor copy() {
        return new TuningFactor(this.factor);
    }

}
