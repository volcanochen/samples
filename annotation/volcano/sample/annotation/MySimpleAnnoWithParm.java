package volcano.sample.annotation;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)
public @interface MySimpleAnnoWithParm {
    
    String hello() default "gege";

    String world();

    int[] array() default { 2, 4, 5, 6 };

    //EnumTest.TrafficLamp lamp();

    //TestAnnotation lannotation() default @TestAnnotation(value = "ddd");

    Class style() default String.class;
}
