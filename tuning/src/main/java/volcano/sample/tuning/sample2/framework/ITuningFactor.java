package volcano.sample.tuning.sample2.framework;

import volcano.sample.tuning.sample2.framework.TuningAdjustMethod.OPVALUE;

public interface ITuningFactor {

    public String print();
    public ITuningFactor copy();
    public void adjust(OPVALUE operationValue);
    
}
