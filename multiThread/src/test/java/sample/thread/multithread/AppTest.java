package sample.thread.multithread;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;


import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import sample.thread.multithread.CommonResourceContainer;

/**
 * Unit test for simple App.
 */
public class AppTest extends TestCase {
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTest(String testName) {
        super(testName);
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite() {
        return new TestSuite(AppTest.class);
    }

    /**
     * Rigourous Test :-)
     */
    public void testApp() {
        assertTrue(true);
    }

    final class MyThread extends Thread {

        private String user;

        public MyThread(String s) {
            System.out.println("i am thread " + s);
            this.user = s;

        }

        public void run() {
            for (int i = 0; i < 10; i++) {
                Random r = new Random();
                int n = r.nextInt(2);   // <<== decide lock on object,
                if (n == 1) {
                    globalController.action(user, i);
                } else {
                    globalController2.action(user, i);
                }

            }

            System.out.println(user + " end");
        }

    }

    CommonResourceContainer globalController = new CommonResourceContainer(1);
    CommonResourceContainer globalController2 = new CommonResourceContainer(2);

    public void testThreadSafety() {

        List<MyThread> list = new ArrayList<MyThread>();
        MyThread m1 = new MyThread("Leo");
        MyThread m2 = new MyThread("CR7");
        m1.start();
        m2.start();

        list .add(m1);
        list .add(m2);
        
        try  
        {  
            for (MyThread my : list)  
            {  
                my.join();  
            }  
        }  
        catch (InterruptedException e)  
        {  
            e.printStackTrace();  
        }  

        System.out.println("MAIN " + " end");
    }
}
