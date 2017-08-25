package volcano.sample.tuning.sample2.framework;

public abstract class ITuningAlgorithm {

    public  TuningAdjustMethod ask(final ITuningFactor x, final ITuningSample y) {
        
        if (isStop()){
            System.out.println("TuningAlgorithm stop condition met ");
            return new TuningAdjustMethod(TuningAdjustMethod.OPCODE.DONE, null);
        }
        return process(x,y);
    }
   
    public abstract ITuningFactor getBest();

    public abstract TuningAdjustMethod process(final ITuningFactor x, final ITuningSample y);
    
    public abstract boolean  isStop();

    public abstract String getOutput();

}
