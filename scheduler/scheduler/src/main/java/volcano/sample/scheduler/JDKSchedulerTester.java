package volcano.sample.scheduler;

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

public class JDKSchedulerTester {
    // ������ƾ��
    private static ScheduledFuture<?> beeperHandle = null;
    // ����һ������
    private static ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);

    
    public static void main(String[] args){
        new JDKSchedulerTester();
    }
    
    /**
     * ����lazy-init=false��
     * spring�����Ĭ�ϵĹ��췽����ʼ������������,���ǵ�taskҲ����ִ����
     */
    public JDKSchedulerTester() {

        // ����ʵ��
        Runnable tast = new Runnable() {
            int count = 0;

            @Override
            public void run() {
                if (count == 5) {

                    int i = 1 / 0; // �����쳣��Ŀ��,��ʾ���ģʽ�����������쳣���Զ��˳�,���׳��쳣.���û���쳣,һֱ������ȥ

                }
                System.out.println(count++);
            }
        };

        // ������,����һ��������ȡ������ִ�е��������5����λ������,ÿ1����λִ��һ��task.run()
        beeperHandle = scheduler.scheduleAtFixedRate(tast, 5, 1, TimeUnit.SECONDS);

        // ����ͨ��bepperHandle����task
        Runnable killer = new Runnable() {
            @Override
            public void run() {
                System.out.println("Cancel!");
                beeperHandle.cancel(true); // �Ƿ�Ҫ�ж����������߳� TODO true��false
                                           // ������Ӱ��?
                scheduler.shutdown();

            }
        };

        // ֻ����һ�ε�����
        scheduler.schedule(killer, 15, TimeUnit.SECONDS);

    }

}