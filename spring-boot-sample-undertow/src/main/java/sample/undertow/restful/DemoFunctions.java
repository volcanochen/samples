package sample.undertow.restful;


import java.io.ByteArrayInputStream;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.zip.GZIPInputStream;

import org.apache.http.impl.client.HttpClientBuilder;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.util.StreamUtils;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

import net.sf.json.JSONArray;

public class DemoFunctions {

    public static void testCompressionABAC() throws Exception {
        HttpHeaders requestHeaders = new HttpHeaders();

        requestHeaders.set("Accept-Encoding", "gzip");
        requestHeaders.set("Accept-Language", "cn");
        requestHeaders.set("Authorization",
                "Bearer eyJraWQiOiJuZy1jdmMiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJEZWZhdWx0XC9BUElcL0FCQUNBUEkiLCJhenAiOiJEZWZhdWx0XC9BUElcL0FCQUNBUEkiLCJzY29wZSI6ImFiYWMucG9saWN5LmRlY2lzaW9uIiwiaXNzIjoiaHR0cDpcL1wvYWNjb3VudC1tYW5hZ2VyLmFwcGRpc2NpLnNhbmRib3guYXBjZXJhLXRlc3QubmdjdmMuY29tXC9hY2NvdW50LW1hbmFnZXIiLCJleHAiOjE0OTY0MDY2MjAsImlhdCI6MTQ5NjM3MDYyMCwianRpIjoiNzRiOWE2YTUtYzMwYi00ZmVhLTgzYTQtNjY5Njg5ODMxZjVlIn0.GhFzSbH83jTx6ZNl4PXKjx768nchVr5sp3Hpj1YVvw6yBrpk4RmWyQCJWNb6NXVezcCgzTc1omGtR5rozVnDkqDJ87psr9hdR01pitou9GBBCeePJ9-MZE0z0EBdonrqw6znhbbNTSPRNyaisg2kokt6d5R0oMX76wj9R1j4st8");
        requestHeaders.set("Content-Type", "application/json");
        requestHeaders.set("X-Cc-Market", "market1");
        requestHeaders.set("X-Cc-Vin", "090000");

        // dummy
        Map<String, String> dummy = new LinkedHashMap<>();
        dummy.put("dummy", "dummy");

        // request
        Map<String, Object> request = new LinkedHashMap<>();
        List<Map> ll = new ArrayList<>();
        LinkedHashMap<String, String> a1 = new LinkedHashMap<>();
        a1.put("type", "ID");
        a1.put("externalId", "TestApp001-1");
        LinkedHashMap<String, String> a2 = new LinkedHashMap<>();
        a2.put("type", "ID");
        a2.put("externalId", "ADTestAPP3-1");

        ll.add(a1);
        ll.add(a2);

        request.put("subject", dummy);
        request.put("object", ll);

        UriComponentsBuilder builder = UriComponentsBuilder.fromHttpUrl(
                "http://abac-pdp.appdisci.sandbox.apcera-test.ngcvc.com/pdp/v1/evaluate-policies/application-discovery");

        // request entity
        HttpEntity<Map<String, Object>> requestEntity = new HttpEntity<>(request, requestHeaders);

        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<byte[]> entity = restTemplate.exchange(builder.build().encode().toUriString(), HttpMethod.POST,
                requestEntity, byte[].class);

        /*
         * ResponseEntity<List> entity =
         * this.restTemplate.exchange(builder.build().encode().toUriString(),
         * HttpMethod.POST,
         * requestEntity, List.class);
         */

        //assertThat(entity.getStatusCode()).isEqualTo(HttpStatus.OK);
        GZIPInputStream inflater = new GZIPInputStream(new ByteArrayInputStream(entity.getBody()));
        String cont;
        try {
            cont = StreamUtils.copyToString(inflater, Charset.forName("UTF-8"));
            System.out.println("================ " + cont);
            // org.springframework.http.converter.json.MappingJackson2HttpMessageConverter
            // converter = new
            // org.springframework.http.converter.json.MappingJackson2HttpMessageConverter();

            // converter.canRead(cont.getClass(),MediaType.APPLICATION_JSON_VALUE
            // );

            List<Object> llll = new ArrayList<>();
            JSONArray jsonArray = JSONArray.fromObject(cont);// 把String转换为json
            llll = (List) jsonArray;
            System.out.println("====!!!!!!!!!!!!!===== " + llll);

            System.out.println("====!!!!!!!!!!!!!===== " + ((Map<String, Object>) llll.get(0)).get("object"));
        } finally {
            inflater.close();
        }
    }

    /***
     * test using httpClient for RestTemplate
     * 
     * @throws Exception
     */
    public static void testCompressionABAC_2() throws Exception {
        HttpHeaders requestHeaders = new HttpHeaders();

        requestHeaders.set("Accept-Encoding", "gzip");
        requestHeaders.set("Accept-Language", "cn");
        requestHeaders.set("Authorization",
                "Bearer eyJraWQiOiJuZy1jdmMiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJEZWZhdWx0XC9BUElcL0FCQUNBUEkiLCJhenAiOiJEZWZhdWx0XC9BUElcL0FCQUNBUEkiLCJzY29wZSI6ImFiYWMucG9saWN5LmRlY2lzaW9uIiwiaXNzIjoiaHR0cDpcL1wvYWNjb3VudC1tYW5hZ2VyLmFwcGRpc2NpLnNhbmRib3guYXBjZXJhLXRlc3QubmdjdmMuY29tXC9hY2NvdW50LW1hbmFnZXIiLCJleHAiOjE0OTY0MDY2MjAsImlhdCI6MTQ5NjM3MDYyMCwianRpIjoiNzRiOWE2YTUtYzMwYi00ZmVhLTgzYTQtNjY5Njg5ODMxZjVlIn0.GhFzSbH83jTx6ZNl4PXKjx768nchVr5sp3Hpj1YVvw6yBrpk4RmWyQCJWNb6NXVezcCgzTc1omGtR5rozVnDkqDJ87psr9hdR01pitou9GBBCeePJ9-MZE0z0EBdonrqw6znhbbNTSPRNyaisg2kokt6d5R0oMX76wj9R1j4st8");
        requestHeaders.set("Content-Type", "application/json");
        requestHeaders.set("X-Cc-Market", "market1");
        requestHeaders.set("X-Cc-Vin", "090000");

        // dummy
        Map<String, String> dummy = new LinkedHashMap<>();
        dummy.put("dummy", "dummy");

        // request
        Map<String, Object> request = new LinkedHashMap<>();
        List<Map> ll = new ArrayList<>();
        LinkedHashMap<String, String> a1 = new LinkedHashMap<>();
        a1.put("type", "ID");
        a1.put("externalId", "TestApp001-1");
        LinkedHashMap<String, String> a2 = new LinkedHashMap<>();
        a2.put("type", "ID");
        a2.put("externalId", "ADTestAPP3-1");

        ll.add(a1);
        ll.add(a2);

        request.put("subject", dummy);
        request.put("object", ll);

        UriComponentsBuilder builder = UriComponentsBuilder.fromHttpUrl(
                "http://abac-pdp.appdisci.sandbox.apcera-test.ngcvc.com/pdp/v1/evaluate-policies/application-discovery");

        // request entity
        HttpComponentsClientHttpRequestFactory clientHttpRequestFactory = new HttpComponentsClientHttpRequestFactory(
                HttpClientBuilder.create().build());

        RestTemplate restTemplate = new RestTemplate(clientHttpRequestFactory);
        /*
         * HttpEntity<Map<String, Object>> requestEntity = new
         * HttpEntity<>(request, requestHeaders);
         * 
         * ResponseEntity<String> entity =
         * restTemplate.exchange(builder.build().encode().toUriString(),
         * HttpMethod.POST,
         * requestEntity, String.class);
         * 
         * 
         * assertThat(entity.getStatusCode()).isEqualTo(HttpStatus.OK);
         * 
         * String cont = entity.getBody();
         * 
         * 
         * System.out.println("================ " + cont);
         * 
         * 
         * List<Object> llll = new ArrayList<>();
         * JSONArray jsonArray = JSONArray.fromObject(cont);//把String转换为json
         * llll = (List)jsonArray;
         * System.out.println("====!!!!!!!!!!!!!===== " + llll);
         * 
         * 
         * System.out.println("====!!!!!!!!!!!!!===== " + ((Map<String,
         * Object>)llll.get(0)).get("object"));
         */

    }

    public static void testCompressionABAC_3() throws Exception {
        HttpHeaders requestHeaders = new HttpHeaders();

        requestHeaders.set("Accept-Encoding", "gzip");
        requestHeaders.set("Accept-Language", "cn");
        requestHeaders.set("Authorization",
                "Bearer eyJraWQiOiJuZy1jdmMiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJEZWZhdWx0XC9BUElcL0FCQUNBUEkiLCJhenAiOiJEZWZhdWx0XC9BUElcL0FCQUNBUEkiLCJzY29wZSI6ImFiYWMucG9saWN5LmRlY2lzaW9uIiwiaXNzIjoiaHR0cDpcL1wvYWNjb3VudC1tYW5hZ2VyLmFwcGRpc2NpLnNhbmRib3guYXBjZXJhLXRlc3QubmdjdmMuY29tXC9hY2NvdW50LW1hbmFnZXIiLCJleHAiOjE0OTY0MDY2MjAsImlhdCI6MTQ5NjM3MDYyMCwianRpIjoiNzRiOWE2YTUtYzMwYi00ZmVhLTgzYTQtNjY5Njg5ODMxZjVlIn0.GhFzSbH83jTx6ZNl4PXKjx768nchVr5sp3Hpj1YVvw6yBrpk4RmWyQCJWNb6NXVezcCgzTc1omGtR5rozVnDkqDJ87psr9hdR01pitou9GBBCeePJ9-MZE0z0EBdonrqw6znhbbNTSPRNyaisg2kokt6d5R0oMX76wj9R1j4st8");
        requestHeaders.set("Content-Type", "application/json");
        requestHeaders.set("X-Cc-Market", "market1");
        requestHeaders.set("X-Cc-Vin", "090000");

        // dummy
        Map<String, String> dummy = new LinkedHashMap<>();
        dummy.put("dummy", "dummy");

        // request
        Map<String, Object> request = new LinkedHashMap<>();
        List<Map> ll = new ArrayList<>();
        LinkedHashMap<String, String> a1 = new LinkedHashMap<>();
        a1.put("type", "ID");
        a1.put("externalId", "TestApp001-1");
        LinkedHashMap<String, String> a2 = new LinkedHashMap<>();
        a2.put("type", "ID");
        a2.put("externalId", "ADTestAPP3-1");

        ll.add(a1);
        ll.add(a2);

        request.put("subject", dummy);
        request.put("object", ll);

        UriComponentsBuilder builder = UriComponentsBuilder.fromHttpUrl(
                "http://abac-pdp.appdisci.sandbox.apcera-test.ngcvc.com/pdp/v1/evaluate-policies/application-discovery");

        // request entity
        HttpComponentsClientHttpRequestFactory clientHttpRequestFactory = new HttpComponentsClientHttpRequestFactory(
                HttpClientBuilder.create().build());

        RestTemplate restTemplate = new RestTemplate(clientHttpRequestFactory);

        HttpEntity<Map<String, Object>> requestEntity = new HttpEntity<>(request, requestHeaders);

        ResponseEntity<List> entity = restTemplate.exchange(builder.build().encode().toUriString(), HttpMethod.POST,
                requestEntity, List.class);

        //assertThat(entity.getStatusCode()).isEqualTo(HttpStatus.OK);

        String cont = entity.getBody().toString();

        System.out.println("================ " + cont);

        System.out.println("====!!!!!!!!!!!!!===== " + entity.getBody());
        Map<String, Object> a = (Map<String, Object>) (entity.getBody().get(0));

        System.out.println("====!!!!!!!!!!!!!===== " + a.get("object"));

    }

}
