package sample.undertow.loader;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.NoSuchBeanDefinitionException;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.stereotype.Component;


@Component("contextutil")
public class SpringContextUtil implements ApplicationContextAware {
  private static ApplicationContext applicationContext;     
 
  /**
  * @param applicationContext
  * @throws BeansException
  */
  public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
    SpringContextUtil.applicationContext = applicationContext;
  }
 
  /**
  * @return ApplicationContext
  */
  public static ApplicationContext getApplicationContext() {
    return applicationContext;
  }
 
  public static String[] getBeanNamesForType(Class<?> type){
	  
	  return applicationContext.getBeanNamesForType(type);
  }
  
  /**
  * 
  * @param name
  * @return Object 
  * @throws BeansException
  */
  public static Object getBean(String name) throws BeansException {
    return applicationContext.getBean(name);
  }
 
  /**

  * @param name      
  * @param requiredType 
  * @return Object 
  * @throws BeansException
  */
  public static Object getBean(String name, Class requiredType) throws BeansException {
    return applicationContext.getBean(name, requiredType);
  }
 
  /**
  * @param name
  * @return boolean
  */
  public static boolean containsBean(String name) {
    return applicationContext.containsBean(name);
  }
 
  /**
  * @param name
  * @return boolean
  * @throws NoSuchBeanDefinitionException
  */
  public static boolean isSingleton(String name) throws NoSuchBeanDefinitionException {
    return applicationContext.isSingleton(name);
  }
 
  /**
  * @param name
  * @return Class 
  * @throws NoSuchBeanDefinitionException
  */
  public static Class getType(String name) throws NoSuchBeanDefinitionException {
    return applicationContext.getType(name);
  }
 
  /**
  * @param name
  * @return
  * @throws NoSuchBeanDefinitionException
  */
  public static String[] getAliases(String name) throws NoSuchBeanDefinitionException {
    return applicationContext.getAliases(name);
  }
}
