package volcano.sample.scheduler;

import org.springframework.scheduling.concurrent.ThreadPoolTaskScheduler;  
import org.springframework.scheduling.support.CronTrigger;  
  
import javax.annotation.PostConstruct;  
import javax.annotation.PreDestroy;  
public class SpringThreadPoolTaskSchedulerTester implements Runnable{  
    private ThreadPoolTaskScheduler tpts=null;  
      
    private String cronExpression="1 * * ? * *";  
      
    @PostConstruct  
    private void start() {  
        tpts=new ThreadPoolTaskScheduler();  
        //�����ʼ��������  
        tpts.initialize();  
          
          
        CronTrigger ct=new CronTrigger(cronExpression);  
          
        tpts.schedule(this,ct);  
  
    }  
      
    @PreDestroy  
    private void stop() {  
        tpts.shutdown();  
  
    }  
      
    @Override  
    public void run() {  
        System.out.println("yes , a task running based on cron expression!@");   
    }  
      
}  
