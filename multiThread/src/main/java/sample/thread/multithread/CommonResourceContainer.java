package sample.thread.multithread;

import java.util.Random;

class CommonResourceContainer {

    private int id;

    private int resource = 0;

    // serve as lock object
    private byte[] lock = new byte[0];

    public CommonResourceContainer(int i) {

        id = i;
    }

    void randomSleep() {
        try {
            Random r = new Random();
            int n3 = r.nextInt(11);
            Thread.sleep(n3);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    /*
     * private synchronized int getV(String who) {
     * System.out.println("                   !!!!! "+who+" getV @" + id );
     * return v;
     * }
     */
    public int getV(String who) {
        synchronized (lock) {
            System.out.println("                   !!!!! " + who + " getV @" + id);
            return resource;
        }

    }

    /*
     * private synchronized void setV(String who, int v) throws Exception {
     * 
     * System.out.println("<<< "+who+" setV start @" + id);
     * this.v = v;
     * randomSleep();
     * 
     * Random r = new Random();
     * int n = r.nextInt(2);
     * if(n == 1){
     * System.out.println("    "+who + " setV exception >>> @" + id);
     * throw new Exception();
     * }
     * System.out.println("    "+who + " setV stop >>> @" + id);
     * }
     */
    public void setV(String who, int v) throws Exception {
        synchronized (lock) {
            System.out.println("<<< " + who + " setV start @" + id);
            this.resource = v;
            randomSleep();

            // anther jump out
            Random r = new Random();
            int n = r.nextInt(2);
            if (n == 1) {
                System.out.println("    " + who + " setV exception >>> @" + id);
                throw new Exception();
            }

            System.out.println("    " + who + " setV stop >>> @" + id);
        }

    }

    class ThreadResource {

        private CommonResourceContainer owner;

        public ThreadResource(int i, CommonResourceContainer owner) {
            // super(i);
            this.owner = owner;
        }

        void useResource(String who) {
            // System.out.println(who + " REST out");

            try {
                owner.setV(who, owner.getV(who));
                // setV(who, getV(who));
            } catch (Exception e) {
                // System.out.println(" "+who + " setV exception >>> @" + id);
            }
        }
    }

    void action(String who, int in) {

        new ThreadResource(id, this).useResource(who + " " + in);

    }

}
