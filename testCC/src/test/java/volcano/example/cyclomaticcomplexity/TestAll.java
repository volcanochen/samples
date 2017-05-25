package volcano.example.cyclomaticcomplexity;

import org.junit.Test;

public class TestAll {

    @Test
    public void testC1function1Challege() {

        
        All.C1.function1Challege(0);
        All.C1.function1Challege(1);
        All.C1.function1Challege(11);
    }
    @Test
    public void testC1function1() {

        
        All.C1.function1(1,1);  //2 branches covered
        All.C1.function1(1,0);  //3rd branch covered
        All.C1.function1(0, -100); // 4st covered   (0, -100) (0, 100) the same
    }
}
