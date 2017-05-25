package volcano.example.cyclomaticcomplexity;

public class All {
    public static class C1 {

        public static void function1(int a, int b) {

            if (a > 0 && b > 0) {
                // cmpx 3
            }
            
            if (a <= 0 || b <= 0) {
                // cmpx 3
            }
            
            /*else if (a <= 0){
                
            } else if (a > 0 && b<= 0){
                
            }*/
        }
        static boolean condition(int a, int b){
           return  a > 0 && b > 0;
        }
        static boolean condition2(int a, int b){
            if  (a <= 0) {
                return false;
            }
            if (b > 0) {
                   return true;
                   }
            return false;
         }
        public static void function1Fix(int a, int b) {

            if (condition(a,b)) {
                // cmpx 3
            }

        }
        
        
        public static  void function1Challege(int a) {
            // cmpx 4
            if (a > 0 && a < 10) {
               
            }else if (a <= 0){
                
            }else { //(a>= 10)
                
            }
        }
        
        public static void function1ChallegeFix(int a) {
            // cmpx 3
            if (a <= 0) {
                
            } else if (a >= 10) {
                
            } else {
                
            }

        }

    }
    public class C1P {

        void function1(int a, int b) {

            if (a > 0 & b > 0) {
             // cmpx 4
            }

        }
        
        void function1p(int a, int b) {

            if (((a > 0 ? 1 : 0) & (b > 0 ? 1 : 0)) != 0) {
             // cmpx 4
            }

        }

    }

    public class C2 {

        void function2(int a, int b) {
            // cmpx 3
            if (a > 0) {
                if (b > 0) {
 
                }
            }
        }
        void function2c(int a, int b) {
            // cmpx 4
            if (a > 0) {

            }
            if (b > 0) {
                
            }
        }
        void function2p(int a, int b) {
         // cmpx 4
            if (a > 0) {
                if (b > 0) {
                    
                }else{
                    
                }
            }else{
                if (b > 0) {
                }else{
                    
                }
            }
        }
    }

    public class C3 {
        void function3(int a, int b, int c) {

            if (a > 0) {
                if (b > 0) {
                    if (c > 0) {
                     // cmpx 4
                    }
                }
            }
        }
    }

    public class C4 {
        
        
        
        public C4() {
            super();
            // TODO Auto-generated constructor stub
        }

        void function4(int a, int b, int c) {

            if ((a > 0) && (b > 0) && (c > 0)) {
             // cmpx 4
            }
        }
    }

    public class C5 {
        void function5(int a, int b, int c) {

            if ((a > 0) && ((b > 0) && (c > 0))) {
             // cmpx 4
            }
        }

    }

}
