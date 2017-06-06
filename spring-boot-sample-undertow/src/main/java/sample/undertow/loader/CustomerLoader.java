package sample.undertow.loader;

import java.io.File;
import java.io.FilenameFilter;
import java.lang.reflect.Method;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.springframework.boot.SpringApplication;

public class CustomerLoader {

	public static List<Object> getBeans(String interfaceName) throws ClassNotFoundException{
		
		System.out.println("getBeans (" + interfaceName + ")");
		
		List<Object> listBean;
		//demo how to get multiply bean by class type
		String[] as = SpringContextUtil.getBeanNamesForType(Class.forName(interfaceName));
		listBean = new ArrayList<Object>();
		Arrays.asList(as).forEach((i) -> {
			listBean.add( SpringContextUtil.getBean(i));
			
		}); 
		
		return listBean;
	}
	public static void load(String pathForJars) {
		
		
		System.out.println(">>>>>> CustomerLoader.load");
		
		//String pathForJars ="C:/jars";
		File libPath = new File(pathForJars);

		// get .jar .zip
		File[] jarFiles = libPath.listFiles(new FilenameFilter() {
			public boolean accept(File dir, String name) {
				return name.endsWith(".jar") || name.endsWith(".zip");
			}
		});

		if (jarFiles != null) {
 
			Method method = null;
			try {
				method = URLClassLoader.class.getDeclaredMethod("addURL", URL.class);
			} catch (NoSuchMethodException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			} catch (SecurityException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			boolean accessible = method.isAccessible(); // get access
			try {
				if (accessible == false) {
					method.setAccessible(true); //
				}
				
				
				
				//get system loader
				//URLClassLoader classLoader = (URLClassLoader) ClassLoader.getSystemClassLoader();
				URLClassLoader classLoader = (URLClassLoader)SpringApplication.class.getClassLoader();
				if (classLoader == null) {
				    System.out.printf("FATAL: not a SpringApplication");
				    return;
				}
				for (File file : jarFiles) {
					URL url = file.toURI().toURL();
					try {
						method.invoke(classLoader, url);
						System.out.printf("Read jar [%s] \n", file.getName());
					} catch (Exception e) {
						System.out.printf("Failed read jar [%s]\n"+ file.getName());
					}
				}
			} catch (MalformedURLException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			} finally {
				method.setAccessible(accessible);
			}
		}
	}
}
