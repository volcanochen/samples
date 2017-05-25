package mockitosample;

import java.util.List;

import org.junit.Test;
import org.mockito.ArgumentCaptor;

import static org.junit.Assert.*;
import static org.mockito.Mockito.*;

public class TestTest {
    
    
    @Test  
    public void argumentCaptoraOnceTest() {  
        List mock = mock(List.class);  
        mock.add("John");  
        
        ArgumentCaptor argument = ArgumentCaptor.forClass(String.class);  

        verify(mock).add(argument.capture());  
        assertEquals("John", argument.getValue());  

    }  
    
    @Test  
    public void argumentCaptoraArrayTest() {  
     
        // #2
        List mock2 = mock(List.class);  
        mock2.add("Brian");  
        mock2.add("Jim");  
        
        ArgumentCaptor argument2 = ArgumentCaptor.forClass(String.class);  
          
        verify(mock2, times(2)).add(argument2.capture());  
      
        assertEquals("Jim", argument2.getValue());  
        assertArrayEquals(new Object[]{"Brian","Jim"},argument2.getAllValues().toArray());  
    }  
    
    
    
}
