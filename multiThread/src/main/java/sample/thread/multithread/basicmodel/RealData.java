package sample.thread.multithread.basicmodel;

public class RealData implements Data {
    protected String data;
 
    public RealData(String data) {
        //利用sleep方法来表示RealData构造过程是非常缓慢的
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        this.data = data;
    }
 
    public String getResult() {
        return data;
    }
}