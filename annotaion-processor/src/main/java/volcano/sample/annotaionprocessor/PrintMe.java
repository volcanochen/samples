package volcano.sample.annotaionprocessor;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target({ ElementType.METHOD, ElementType.LOCAL_VARIABLE, ElementType.TYPE, ElementType.FIELD })
@Retention(RetentionPolicy.SOURCE)
public @interface PrintMe {
}
