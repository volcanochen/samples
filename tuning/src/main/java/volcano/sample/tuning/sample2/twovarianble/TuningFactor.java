package volcano.sample.tuning.sample2.twovarianble;

import java.util.Random;

import volcano.sample.tuning.sample2.framework.ITuningFactor;
import volcano.sample.tuning.sample2.framework.TuningAdjustMethod;

public class TuningFactor implements ITuningFactor {
    
    double interval = 0.1;
    Double[] factor = {0.0,0.0};
    double  x;
    double y;
    private Double  min = -10.0;
    private Double max = 30.0;
    
    public TuningFactor(Double[] factor){
        this.factor = factor;
    }
    public Double[] getFactor() {
        return factor;
    }

    public void setFactor(Double[] factor) {
        this.factor = factor;
    }
    @Override
    public void adjust(TuningAdjustMethod.OPVALUE delta) {

        switch (delta){
        case STEP_RANDON:
            this.factor[0] = (new Random()).nextDouble() * (max - min) + min;
            this.factor[1] = (new Random()).nextDouble() * (max - min) + min;
            break;
        case MAX:
            this.factor[0] = max;
            this.factor[1] = max;
            break;
        case MIN:
            this.factor[0] = min;
            this.factor[1] = min;
            break;
        default:
            break;
        
        }

    }
    @Override
    public String print() {
        return String.format("(%.2f,%.2f)", this.factor[0],this.factor[1]);
    }
    @Override
    public ITuningFactor copy() {
        return new TuningFactor(this.factor.clone());
    }

}
