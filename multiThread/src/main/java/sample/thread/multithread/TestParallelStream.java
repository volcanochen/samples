package sample.thread.multithread;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.concurrent.CopyOnWriteArraySet;
import java.util.concurrent.CountDownLatch;

/**
 * @description 这是一个用来让你更加熟悉parallelStream的原理的实力
 * @date 2016年10月11日18:26:55
 * @version v1.0
 * @author wangguangdong 
 */
public class TestParallelStream {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello World!");
        // 构造一个10000个元素的集合
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < 10000; i++) {
            list.add(i);
        }
        // 统计并行执行list的线程
        Set<Thread> threadSet = new CopyOnWriteArraySet<>();
        // 并行执行
        list.parallelStream().forEach(integer -> {
            Thread thread = Thread.currentThread();
            // System.out.println(thread);
            // 统计并行执行list的线程
            threadSet.add(thread);
        });
        System.out.println("threadSet :" + threadSet.size() + " threads");
        System.out.println("total cpu processor:"+Runtime.getRuntime().availableProcessors()+" cpus");
        System.out.println("---------------------------");
        System.out.println(threadSet);
        System.out.println("---------------------------");
        
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        for (int i = 0; i < 100000; i++) {
            list1.add(i);
            list2.add(i);
        }
        Set<Thread> threadSetTwo = new CopyOnWriteArraySet<>();
        CountDownLatch countDownLatch = new CountDownLatch(2);
        Thread threadA = new Thread(() -> {
            list1.parallelStream().forEach(integer -> {
                Thread thread = Thread.currentThread();
                // System.out.println("list1" + thread);
                threadSetTwo.add(thread);
            });
            countDownLatch.countDown();
        });
        Thread threadB = new Thread(() -> {
            list2.parallelStream().forEach(integer -> {
                Thread thread = Thread.currentThread();
                // System.out.println("list2" + thread);
                threadSetTwo.add(thread);
            });
            countDownLatch.countDown();
        });

        threadA.start();
        threadB.start();
        countDownLatch.await();
        System.out.println("threadSetTwo :" + threadSetTwo.size() + " threads");
        System.out.println("---------------------------");
        System.out.println(threadSetTwo);
        System.out.println("---------------------------");
        
        
        System.out.println("-------------threadSet & threadSetTwo---------");
        threadSetTwo.addAll(threadSet);
        System.out.println(threadSetTwo);
        System.out.println("" + threadSetTwo.size() + " threads");
        System.out.println("total cpu processor:"+Runtime.getRuntime().availableProcessors()+" cpus");
    }
}
