package volcano.sample.tuning.sample2.onevariable;

import volcano.sample.tuning.sample2.framework.ITuningSample;

public class TuningSample implements ITuningSample {
    double sample;

    public TuningSample(double y){
        sample = y;
    }
    
    public double getSample() {
        return sample;
    }

    public void setSample(double sample) {
        this.sample = sample;
    }

    @Override
    public boolean isBetter(ITuningSample y) {
        TuningSample t = (TuningSample)y;
        if (this.getSample() >= t.getSample()){
            return true;
        }
        return false;
    }

    @Override
    public String print() {
        return String.format("%.2f", this.sample);
    }

    @Override
    public ITuningSample copy() {
        return new TuningSample(this.getSample());
    }


    
}
