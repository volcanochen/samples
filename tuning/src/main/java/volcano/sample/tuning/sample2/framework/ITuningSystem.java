package volcano.sample.tuning.sample2.framework;

public interface ITuningSystem {
    
    void start(final ITuningFactor x);
    ITuningSample get();
}
