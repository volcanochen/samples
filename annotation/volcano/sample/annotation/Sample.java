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
        if (method.isAnnotationPresent(MySimpleAnno.class))// ���doSomething�����ϴ���ע��@MyTarget����Ϊtrue
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
        // ���MyTest��������ע��@MyAnnotation���Σ���Ϊtrue
        if (MyTest.class.isAnnotationPresent(MySimpleAnnoWithParm.class)) {
            System.out.println("MyTest have annotation");
        }
        if (method.isAnnotationPresent(MySimpleAnnoWithParm.class)) {
            method.invoke(myTest, null); // ����output����
            // ��ȡ������ע��@MyAnnotation����Ϣ
            MySimpleAnnoWithParm myAnnotation = method.getAnnotation(MySimpleAnnoWithParm.class);
            String hello = myAnnotation.hello();
            String world = myAnnotation.world();
            System.out.println(hello + ", " + world);// ��ӡ����hello��world��ֵ
            System.out.println(myAnnotation.array().length);// ��ӡ����array����ĳ���

            System.out.println(myAnnotation.style());
        }
        // �õ�output�����ϵ�����ע�⣬��Ȼ�Ǳ�RetentionPolicy.RUNTIME���ε�
        Annotation[] annotations = method.getAnnotations();
        for (Annotation annotation : annotations) {
            System.out.println(annotation.annotationType().getName());
        }

    }
}
