    public class insertion {
        public static void main(String[] args){
            float temp = 0;
            float[] a = {3, 1, 4, 2, 10, 646};
            for(int i = 1; i < a.length; i++){
                while(i-1>=0 && a[i] < a[i-1]){
                    temp = a[i];
                    a[i] = a[i-1];
                    a[i-1] = temp;
                    i--;
                    for(int j = 0; j < a.length; j++){
                        System.out.print(a[j] + " ");
                    }
                    System.out.println();
                }
            }
        }
    }
