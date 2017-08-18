package volcano.sample.annotaionprocessor;

import java.util.Set;

import javax.annotation.processing.*;
import javax.lang.model.SourceVersion;
import javax.lang.model.element.TypeElement;

import javax.lang.model.element.Element;

import javax.tools.Diagnostic;
import com.google.auto.service.AutoService;


@SuppressWarnings("restriction")
@SupportedAnnotationTypes({"volcano.sample.annotaionprocessor.PrintMe"})
@AutoService(Processor.class)
public class MyProcessor extends AbstractProcessor {

    @Override
    public SourceVersion getSupportedSourceVersion() {
        return SourceVersion.latestSupported();
    }

    @Override
    public boolean process(Set<? extends TypeElement> annotations, RoundEnvironment env) {
        Messager messager = processingEnv.getMessager();
/*        for (TypeElement te : annotations) {
            for (Element e : env.getElementsAnnotatedWith(te)) {
                messager.printMessage(Diagnostic.Kind.NOTE, "Printing: " + e.toString());
            }
        }*/
        messager.printMessage(Diagnostic.Kind.NOTE, "++++++++++++++++++ " );
        
        Set<? extends Element> elementSet = env.getElementsAnnotatedWith(PrintMe.class);
        for (Element e : elementSet) {
            messager.printMessage(Diagnostic.Kind.NOTE, "Printing: " + e.toString());
        }

        return true;
    }
}