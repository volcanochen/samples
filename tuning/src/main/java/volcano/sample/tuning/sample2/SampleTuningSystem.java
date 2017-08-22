package volcano.sample.tuning.sample2;

import java.util.concurrent.Callable;

public class SampleTuningSystem implements  TuningSystem {
    int x;
    int y;
    
    class SystemA implements Callable<Integer> {
        Integer x;

        SystemA(Integer x) {
            this.x = x;
        }

        public Integer call() throws Exception {
            Thread.sleep(1000);

            return -(x - 3) ^ 2 + 40;
        }

    };
    @Override
    public void start(TuningFactor x){
        Callable<Integer> s = new SystemA(x.getFactor());
        try {
            y =  s.call();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    @Override
    public TuningSample get(){
        return new TuningSample(y);
    }
    
    
    

}