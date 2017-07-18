package sample.thread.multithread;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.FutureTask;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import sample.thread.multithread.CommonResourceContainer;
import sample.thread.multithread.basicmodel.Client;
import sample.thread.multithread.basicmodel.Data;



/**
 * Unit test for simple App.
 */
public class AppTestFuture extends TestCase {
    /***
     * basic future data model
     * 
     * 
     */
    public void testBasicFuture() {
        Client client = new Client();
        //这里会立即返回，因为获取的是FutureData，而非RealData
        Data data = client.request("name");
        //这里可以用一个sleep代替对其他业务逻辑的处理
        //在处理这些业务逻辑过程中，RealData也正在创建，从而充分了利用等待时间
        try {
            Thread.sleep(2000);
            //使用真实数据
            System.out.println("data="+data.getResult());
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        
    }
    /***
     * JDK future sample, key: FutureTask, Callable 
     */
    public void testJDKFuture(){
        FutureTask<String> futureTask = 
                new FutureTask<String>(new RealData("name"));
        ExecutorService executor = 
                Executors.newFixedThreadPool(1); //使用线程池
        //执行FutureTask，相当于上例中的client.request("name")发送请求
        executor.submit(futureTask);
        //这里可以用一个sleep代替对其他业务逻辑的处理
        //在处理这些业务逻辑过程中，RealData也正在创建，从而充分了利用等待时间
        try {
            Thread.sleep(2000);
            //使用真实数据
            //如果call()没有执行完成依然会等待
            System.out.println("data=" + futureTask.get());
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ExecutionException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        


    }
}
