package volcano.sample;

import volcano.sample.annotaionprocessor.PrintMe;

@PrintMe
public class MyClass {
    @PrintMe
    String field;
    
    @PrintMe
    public void test(){
        System.out.println("@@@@@@@@@@@@@@@@");
        
        
        //this local variant cannot be catched!!!
       @PrintMe
       String st = "testString";
        
    }
    
}
