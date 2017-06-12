package volcano.sample.flatten_map_converter;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;


import volcano.sample.flatten_map_converter.MapConverter.ConvertReturnPair;



public class MapConverterTests {
	
	Map<String, Object> a1 = new LinkedHashMap<String, Object>();
	
	@Before
	public void init(){
		
        a1.put("applicationId", "A-cqk00kotyczfcai");
        a1.put("ownerId", "P-40000ogTVq7");
        a1.put("ownerName", "Ericsson Ltd.");
        a1.put("type", "WEBAPPLICATION");
        a1.put("globalId", "Overwatch");
        a1.put("name",new LinkedHashMap<String, String>(){{put("en", "OverWatch");}});
        a1.put("description",new LinkedHashMap<String, String>(){{
        	put("en", "This is an OVERWATCH APP");
        	put("ch", "This xxxxxxx");}});
        a1.put("version",1);
        a1.put("releaseNote",new LinkedHashMap<String, String>(){{
        	put("en", "The first release");
        	put("ch", "xxxxx");}});

        a1.put("iconUrl", "http://ecnshxenlx0203:8290/service-manager-api/store/P-y0000EIRjV_/i/d/i/app.png");
        a1.put("validFrom", "2017-03-22T09:01:09.016Z");
        a1.put("validUntil", "2017-03-22T09:01:09.016Z");
        a1.put("created", "2017-03-22T09:01:09.016Z");
        a1.put("lastModified", "2017-03-22T09:01:09.016Z");
        a1.put("status", "200");
        a1.put("locales", new ArrayList<String>(Arrays.asList("en","ch")));
        a1.put("extensions",new LinkedHashMap<String, String>(){{put("ext1", "ext1value");put("ext2", "ext2value");}});

	}
	//TEST Map<String, Object> convert(Object o)
	@Test
	public void testconvert(){
		MapConverter n = new MapConverter();

        Map<String, Object> map = n.convert(a1);
		System.out.println(map.toString());
		
		Assert.assertTrue(((Map<String,Object>) ((Map<String,Object>) map.get("locales")).get("0")).get("").equals("en"));
		Assert.assertTrue(((Map<String,Object>) map.get("applicationId")).get("").equals("A-cqk00kotyczfcai"));

	}
	
	//List<ConvertReturnPair> brick(String k, Object v) {
	@Test
	public void testbrick(){
		MapConverter n = new MapConverter();
		List<ConvertReturnPair> rt = n.brick("a", "s1");
		System.out.println(rt);
		
		Assert.assertTrue(rt.get(0).getKeyOpt().equals("a"));
		Assert.assertTrue(rt.get(0).getValue().equals("s1"));
		

		Map<String, Object> testmap = new LinkedHashMap<String, Object>();
		testmap.put("level2_1", "String1");
		testmap.put("level2_2", "String2");
		List<ConvertReturnPair> rt2 = n.brick("level1", testmap);

		System.out.println(rt2);
		
		Assert.assertTrue(rt2.get(0).getKeyOpt().equals("level1.level2_1"));
		Assert.assertTrue(rt2.get(1).getKeyOpt().equals("level1.level2_2"));

	}
	

	@Test
	public void testconvertToFlattenMap(){
		MapConverter n = new MapConverter();
		
		Map<String, Object> testmapl1 = new LinkedHashMap<String, Object>();
		Map<String, Object> testmap = new LinkedHashMap<String, Object>();
		testmap.put("level2_1", "String1");
		testmap.put("level2_2", "String2");
		testmapl1.put("level1", testmap);
		
		Map<String, Object> te = n.convertToFlattenMap(testmapl1);
		System.out.println(te);
		
		Assert.assertTrue(te.get("level1.level2_1").equals("String1"));
		Assert.assertTrue(te.get("level1.level2_2").equals("String2"));
		
	}
	

	
	
	
}
