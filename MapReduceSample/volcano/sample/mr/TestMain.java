package volcano.sample.mr;

import static org.junit.Assert.*;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.junit.Test;

public class TestMain {

    
    /***
     * �����һ����Ϸ�ʽ��Ӧ�ã�����Ҫ�ļ����߼�ͨ���������з�װ��Ȼ����Щ����
     * ���������������ͽ����������ģ������getPrice������������MockResource��
     * ���ʹ��Stream���ͺ�Lambda���ʽ�����Ҫִ�еļ����߼����õ����ս����
     * <br/><br/>
     * �������߼���װ��һ�������������ĺô����ڣ�<br/>
     * - ����࣬���������ٺܶ࣬�Ӷ�����Ҳ�����ױ����<br/>
     * - ����˶���Ĳ�����(Immutability)���Ӷ��������ײ��л�<br/>
     * - �������е�ÿһ���������ױ����ã���filter��sorted��<br/>
     */
    
    @Test
    public void test() {
        final BigDecimal HUNDRED = new BigDecimal("100");
        System.out.println("Stocks are \n" + Tickers.symbols.toString());
        System.out.println("Stocks priced over $100 are \n"
                + Tickers.symbols.stream().filter(symbol -> (MockResource.getPrice(symbol).compareTo(HUNDRED) > 0))
                        .sorted().
                        collect(Collectors.toList()));
    }

    /***
     * ����ʽ���<br/>
     * - �Ա��������޸���ʵ�ּ����߼�<br/>
     * - ���븴���ԱȽϲ��������Ҫ���Ĺ���������ʱ�򣬾���Ҫ���������޸�<br/>
     */
    @Test
    public void test2() {
        final List<StockInfo> stocks = new ArrayList<>();
        for (String symbol : Tickers.symbols) {
            stocks.add(StockUtil.getPrice(symbol));
        }

        final List<StockInfo> stocksPricedUnder500 = new ArrayList<>();
        final Predicate<StockInfo> isPriceLessThan500 = StockUtil.isPriceLessThan(500);
        for (StockInfo stock : stocks) {
            if (isPriceLessThan500.test(stock))
                stocksPricedUnder500.add(stock);
        }

        System.out.println("Stocks priced over $100 are \n" + stocksPricedUnder500.toString());
        
        StockInfo highPriced = new StockInfo("", BigDecimal.ZERO);
        for (StockInfo stock : stocksPricedUnder500) {
            highPriced = StockUtil.pickHigh(highPriced, stock);
        }

        System.out.println("High priced under $500 is " + highPriced);
    }
    
    /***
     * ����ʽ���<br/>
     */
    
    @Test
    public void test3(){
        StockInfo highPriced = new StockInfo("", BigDecimal.ZERO);
        final Predicate<StockInfo> isPriceLessThan500 = StockUtil.isPriceLessThan(500);

        for(String symbol : Tickers.symbols) {
            StockInfo stockInfo = StockUtil.getPrice(symbol);
            if(isPriceLessThan500.test(stockInfo))
                highPriced = StockUtil.pickHigh(highPriced, stockInfo);
        }

        System.out.println("High priced under $500 is " + highPriced);
    }
    
    /***
     * map, filter��reduce�����ֱ����������forѭ�������Ҵ���Ҳ����쳣��ࡣ<br/>
     * ���˼��֮�⣬����Ҫ������δ�����ʱ���Ա����л���<br/>
     * <br/><br/>
     * ���ڲ�������������Ҫ������Ǿ�̬����(Race Condition)��������߳���ͼȥ����һ���������һ������ʱ��<br/>
     * ���п��ܷ��������Զ���������£�������ҪС�������ά�����̰߳�ȫ�ԡ�����������������״̬�ǲ��ɱ��(״̬����������Ϊfinal)��<br/>
     * ��ô������̬����������Ҳ�Ͳ��������ˣ�����һ�����Ǻ���ʽ�����һ��ǿ���ͱ��ġ�<br/>
     * 
     * @param symbols
     */
    public static void findHighPriced(final Stream<String> symbols) {
        final StockInfo highPriced = symbols
            .map(StockUtil::getPrice)
            .filter(StockUtil.isPriceLessThan(500))
            .reduce(StockUtil::pickHigh)
            .get();

        System.out.println("High priced under $500 is " + highPriced);
    }
    
    /***
     * ����ʽ���<br/>
     * ����ִ�еĵ��÷�ʽ<br/>
     */
    @Test
    public void test4()
    {
        
        findHighPriced(Tickers.symbols.stream());
    }
    /***
     * ����ʽ���<br/>
     * ����ִ�еĵ��÷�ʽ<br/>
     */
    @Test
    public void test5()
    {
        
        findHighPriced(Tickers.symbols.parallelStream());
    }
}
