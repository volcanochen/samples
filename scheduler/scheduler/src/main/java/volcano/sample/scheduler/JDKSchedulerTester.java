package volcano.sample.scheduler;

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

public class JDKSchedulerTester {
    // 任务控制句柄
    private static ScheduledFuture<?> beeperHandle = null;
    // 定义一个服务
    private static ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);

    
    public static void main(String[] args){
        new JDKSchedulerTester();
    }
    
    /**
     * 配置lazy-init=false后
     * spring会调用默认的构造方法初始化这个任务对象,我们的task也就能执行了
     */
    public JDKSchedulerTester() {

        // 任务实体
        Runnable tast = new Runnable() {
            int count = 0;

            @Override
            public void run() {
                if (count == 5) {

                    int i = 1 / 0; // 出现异常的目的,演示这个模式的任务遇到异常是自动退出,不抛出异常.如果没有异常,一直进行下去

                }
                System.out.println(count++);
            }
        };

        // 启动并,返回一个可用于取消或检查执行的任务对象。5个单位后启动,每1个单位执行一次task.run()
        beeperHandle = scheduler.scheduleAtFixedRate(tast, 5, 1, TimeUnit.SECONDS);

        // 用来通过bepperHandle结束task
        Runnable killer = new Runnable() {
            @Override
            public void run() {
                System.out.println("Cancel!");
                beeperHandle.cancel(true); // 是否要中断这个任务的线程 TODO true与false
                                           // 带来的影响?
                scheduler.shutdown();

            }
        };

        // 只启动一次的任务
        scheduler.schedule(killer, 15, TimeUnit.SECONDS);

    }

}