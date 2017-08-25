package volcano.sample.tuning.sample2.framework;

public interface ITuningSample {

    public boolean isBetter(ITuningSample last_y);
    public String print();
    public ITuningSample copy();

}
