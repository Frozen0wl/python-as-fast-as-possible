import java.util.Arrays;

public class swap_sort{

    static int[] a = {6, 3, 9, 7, 4, 1, 8, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2};

    public static void main(String[] args){
        swapsort(a);
        print();

    }
    static int i = 0;
    public static void swapsort(int[] arr){
        while(i < arr.length - 1){
            
            int m = 0; //2
            int temp = 0;
            for(int j = 0; j<arr.length; j++){
                // System.out.print(arr[j]);
                if(arr[i] > arr[j]){
                    m++;
                }                
            }
            System.out.println(Arrays.toString(a));

            temp = arr[i];   //1
            arr[i] = arr[m]; //1
            arr[m] = temp;   //1
            

            if(m == i){
                i++;
            }
        }
    }

    public static void print(){
        System.out.print(Arrays.toString(a));
    }
}        

