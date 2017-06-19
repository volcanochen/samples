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
     * 这就是一个混合范式的应用，将主要的计算逻辑通过方法进行封装，然后将这些函数
     * 根据其所属的类型进行面向对象建模，比如getPrice方法属于类型MockResource。
     * 最后使用Stream类型和Lambda表达式完成需要执行的计算逻辑，得到最终结果。
     * <br/><br/>
     * 将计算逻辑封装成一个函数调用链的好处在于：<br/>
     * - 更简洁，代码量会少很多，从而代码也更容易被理解<br/>
     * - 提高了对象的不变性(Immutability)，从而更加容易并行化<br/>
     * - 调用链中的每一环都很容易被复用，如filter，sorted等<br/>
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
     * 命令式风格<br/>
     * - 对变量进行修改来实现计算逻辑<br/>
     * - 代码复用性比较差，当我们需要更改过滤条件的时候，就需要对它进行修改<br/>
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
     * 命令式风格<br/>
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
     * map, filter和reduce方法分别替代了三个for循环，而且代码也变的异常简洁。<br/>
     * 除了简洁之外，更重要的是这段代码随时可以被并行化。<br/>
     * <br/><br/>
     * 对于并发程序，首先需要避免的是竞态条件(Race Condition)，当多个线程试图去更新一个对象或者一个变量时，<br/>
     * 就有可能发生。所以对于这类更新，我们需要小心翼翼地维护其线程安全性。反过来，如果对象的状态是不可变的(状态变量被修饰为final)，<br/>
     * 那么滋生竞态条件的土壤也就不复存在了，而这一点正是函数式编程所一再强调和标榜的。<br/>
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
     * 命令式风格<br/>
     * 串行执行的调用方式<br/>
     */
    @Test
    public void test4()
    {
        
        findHighPriced(Tickers.symbols.stream());
    }
    /***
     * 命令式风格<br/>
     * 并行执行的调用方式<br/>
     */
    @Test
    public void test5()
    {
        
        findHighPriced(Tickers.symbols.parallelStream());
    }
}
