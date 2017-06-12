package volcano.sample.flatten_map_converter;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * tool class for convert map to flatten map
 * 
 */
public class MapConverter {

	protected class ConvertReturnPair {
        private String value;
        private String keyOpt;
        
		protected ConvertReturnPair(String k, String v) {

			this.keyOpt = k;
			this.value = v;
		}

		protected String getKeyOpt() {
			return keyOpt;
		}

		protected String getValue() {
			return value;
		}

		@Override
		public String toString() {
			return "{{" + keyOpt + "=" + value + "}}";

		}
	}
    /**
     * convert to flatten map
     * 
     * @param in a multiply layers map structure
     * 
     * @return the two layer map after key connected, or called flatten
     */
    public Map<String, Object> convertToFlattenMap(Map<String, Object> in) {
    
        Map<String, Object> rt = new LinkedHashMap<>();

        Map<String, Object> co = convert(in);
        for (ConvertReturnPair i : brick("", co)) {
            rt.put(i.getKeyOpt(), i.getValue());
        }
        return rt;
    
    }
	
	String connectKey(String k, String k2) {

		if ("".equals(k) ) {
			return k2;
		}
		if ("".equals(k2) ) {
			return k;
		} else {
			return k + "." + k2;
		}

	}

	
	Map<String, Object> convert(Object o) {

		Map<String, Object> rt = new LinkedHashMap<>();
		if (o instanceof String) {
			rt.put("", o.toString());
		}
		if (o instanceof List) {
			int i = 0;
			// covert to map first
			for (Object l : (List) o) {
				rt.put(Integer.toString(i), convert(l));
				i++;
			}
		}
		if (o instanceof Map) {
			for (Map.Entry<String, Object> en : ((Map<String, Object>) o).entrySet()) {
				rt.put(en.getKey(), convert(en.getValue()));
			}
		}
		return rt;
	}



	List<ConvertReturnPair> brick(String k, Object v) {
		List<ConvertReturnPair> rt = new ArrayList<>();
		if (v instanceof String) {
			ConvertReturnPair n = new ConvertReturnPair(k, v.toString());
			rt.add(n);
			return rt;
		}
		if (v instanceof Map) {
			Map<String, Object> vmap = (Map<String, Object>) v;
			for (Map.Entry<String, Object> vmap_i : vmap.entrySet()) {
				List<ConvertReturnPair> vmapBrickList = brick(vmap_i.getKey(), vmap_i.getValue());
				for (ConvertReturnPair i : vmapBrickList) {
					ConvertReturnPair n = new ConvertReturnPair(connectKey(k, i.getKeyOpt()), i.getValue());
					rt.add(n);
				}
			}
		}
		return rt;
	}

}
