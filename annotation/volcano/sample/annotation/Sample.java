package volcano.sample.annotation;

import java.lang.annotation.Annotation;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import org.junit.Test;

public class Sample {
    @MySimpleAnno
    public void doSomething() {
        System.out.println("hello world");
    }

    
    
    public static void main(String[] args) throws Exception {

        Method method = Sample.class.getMethod("doSomething", null);
        if (method.isAnnotationPresent(MySimpleAnno.class))// 如果doSomething方法上存在注解@MyTarget，则为true
        {
            System.out.println(method.getAnnotation(MySimpleAnno.class));
        }
    }

    
    
    @MySimpleAnnoWithParm(hello = "beijing", world = "shanghai", array = {}, style = int.class)
    public class MyTest {
        @MySimpleAnnoWithParm(world = "shanghai", array = { 1, 2, 3 })
        @Deprecated
        @SuppressWarnings("")
        public void output() {
            System.out.println("output something!");
        }
    }

    @Test
    public void testMySimpleAnnoWithParm() throws IllegalAccessException, IllegalArgumentException,
            InvocationTargetException, NoSuchMethodException, SecurityException {
        MyTest myTest = new MyTest();
        Class<MyTest> c = MyTest.class;
        Method method = c.getMethod("output", new Class[] {});
        // 如果MyTest类名上有注解@MyAnnotation修饰，则为true
        if (MyTest.class.isAnnotationPresent(MySimpleAnnoWithParm.class)) {
            System.out.println("MyTest have annotation");
        }
        if (method.isAnnotationPresent(MySimpleAnnoWithParm.class)) {
            method.invoke(myTest, null); // 调用output方法
            // 获取方法上注解@MyAnnotation的信息
            MySimpleAnnoWithParm myAnnotation = method.getAnnotation(MySimpleAnnoWithParm.class);
            String hello = myAnnotation.hello();
            String world = myAnnotation.world();
            System.out.println(hello + ", " + world);// 打印属性hello和world的值
            System.out.println(myAnnotation.array().length);// 打印属性array数组的长度

            System.out.println(myAnnotation.style());
        }
        // 得到output方法上的所有注解，当然是被RetentionPolicy.RUNTIME修饰的
        Annotation[] annotations = method.getAnnotations();
        for (Annotation annotation : annotations) {
            System.out.println(annotation.annotationType().getName());
        }

    }
}
