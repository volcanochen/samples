package volcano.sample.mr;

import java.math.BigDecimal;

public class MockResource {
    public static BigDecimal getPrice(final String ticker) {

        try {
            Thread.sleep(1000);
        } catch (Exception e) {
            e.printStackTrace();
        }
        BigDecimal p = new BigDecimal(Math.random() * 1000);
        // System.out.printf("%s -> %s\n",ticker,p.toPlainString());
        return p;

    }
}