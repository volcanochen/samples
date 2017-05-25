package volcano.example.cyclomaticcomplexity;

import java.util.List;

public class SampleToSimplify {

    static public void complexFunc(int a, List<Integer> li, int b, int c, int d, int e, int f){
        if (a > 0 && b > 0) {
            // cmpx 3
        }
        if (a>0 && b>0 && c>0 && d >0 && e >0 && f > 0){

        }else{
            return;
        }
    }
    static public void complexFunc2(int a, List<Integer> li, int b, int c, int d, int e, int f){
        
        if (a>0 && b>0 && c>0 || d >0 && e >0 && f > 0){

        }else{
            return;
        }
    }
}
