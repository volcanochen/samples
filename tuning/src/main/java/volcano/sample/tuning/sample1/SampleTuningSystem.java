package volcano.sample.tuning.sample1;

import java.util.concurrent.Callable;

public class SampleTuningSystem  {
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
    
    void start(int x){
        Callable<Integer> s = new SystemA(x);
        try {
            y =  s.call();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    int get(){
        return y;
    }
    
    
    

}