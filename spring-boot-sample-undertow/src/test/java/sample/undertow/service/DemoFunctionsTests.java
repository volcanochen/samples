
package sample.undertow.service;

import org.junit.Assert;
import org.junit.Test;
//import org.junit.runner.RunWith;
import org.mockito.Mockito;



import static org.assertj.core.api.Assertions.assertThat;

//@RunWith(SpringRunner.class)
//@SpringBootTest
public class DemoFunctionsTests {

    @Test
    public void testSubFunc1() throws Exception {

        String word = "mocked Return";
        DemoFunctions demo = Mockito.mock(DemoFunctions.class);
        Mockito.when(demo.subFunc1()).thenReturn(word);
        Assert.assertEquals(demo.subFunc1(), word);

        // Assert.assertTrue(a.subFunc1().equals("Hello"));
    }

    @Test
    public void testSubFunc12() throws Exception {

        String word = "mocked Return1";
        DemoFunctions demo = Mockito.spy(DemoFunctions.class);
        Mockito.doReturn(word).when(demo).subFunc1();
        Assert.assertEquals(demo.subFunc12(), word + demo.subFunc2());

    }



}