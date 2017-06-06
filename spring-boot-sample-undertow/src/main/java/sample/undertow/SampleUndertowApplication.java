/*
 * Copyright 2012-2014 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package sample.undertow;


import java.util.Arrays;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import org.springframework.context.ConfigurableApplicationContext;



@SpringBootApplication(scanBasePackages = { "sample.undertow", "sample.undertow.loader" })
public class SampleUndertowApplication {

	public static void main(String[] args) throws Exception {
		
		// load jar file
		String pathForJars ="C:/jars";
		sample.undertow.loader.CustomerLoader.load(pathForJars);
		
		ConfigurableApplicationContext context = SpringApplication.run(SampleUndertowApplication.class, args);

/*		System.out.println("===== DEBUG list all beans ====");
		String[] names = context.getBeanDefinitionNames();
		Arrays.sort(names);
		for (String string : names) {
			System.err.println("==== " + string);
		}
		System.out.println("===== DEBUG list all beans end ====");*/
		

		sample.undertow.loader.DemoFunctions.getBeanFromContxtUnderName();
		
		
		
		
		
	}

}

