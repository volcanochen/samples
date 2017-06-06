package sample.undertow.loader;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class DemoFunctions {

    class CSample{

        public String implID() {
            // TODO Auto-generated method stub
            return "CSample";
        }
        
    }
    class CSample2{

        public String implID() {
            // TODO Auto-generated method stub
            return "CSample2";
        }
        
    }
    
	public static void getBeanFromContxtByName() {
	    List<CSample> testListImpls;
		String[] as = SpringContextUtil.getBeanNamesForType(CSample.class);
		testListImpls = new ArrayList<CSample>();
		Arrays.asList(as).forEach((i) -> {
			testListImpls.add((CSample) SpringContextUtil.getBean(i));

		});
		testListImpls.forEach(i -> {
			System.out.println(">>>>>>> implement id: " + i.implID());
		});
	}

	public static void getBeanFromContxtUnderName() {

		System.out.println(">>>>  get from annotation injected bean from interface implementation  >>>");
		System.out.println(">>>>  CSample >>");
		String beanInterfaceClasspath = "sample.undertow.loader.DemoFunctions$CSample";
		List<Object> ll;
		try {
			ll = CustomerLoader.getBeans(beanInterfaceClasspath);
			ll.forEach(i -> {
				System.out.println(">>>>>>> implement id: " + ((CSample) i).implID());
			});
		} catch (ClassNotFoundException e1) {
			// TODO Auto-generated catch block
			System.out.println(">>>>>>> ClassNotFoundException  >>>> " + beanInterfaceClasspath);
			//e1.printStackTrace();
		}
		
		System.out.println(">>>>  Appif >>");
		beanInterfaceClasspath = "com.ericsson.automotive.application.discovery.api.appif.Appif";

        try {
            ll = CustomerLoader.getBeans(beanInterfaceClasspath);
            ll.forEach(i -> {
                
                
                System.out.println(">>>>>>> implement id: " + ((CSample2) i).implID());
                
//                if (((Appif) i).implID() == 8009){
//                    ((Appif) i).setConfig(null);
//                }
                
                
            });
        } catch (ClassNotFoundException e1) {
            // TODO Auto-generated catch block
            System.out.println(">>>>>>> ClassNotFoundException  >>>> " + beanInterfaceClasspath);
            //e1.printStackTrace();
        }
		

	}

}
