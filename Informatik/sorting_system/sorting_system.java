class sorting_system {
    public static void main(String[] args){
        int[] a = {3, 1, 4, 2, 10};

        for(int i = 0; i < a.length; i++){
            for(int j = 1; j < a.length - i; j++){
                if(a[j] < a[j - 1]){
                    int temp = a[j];
                    a[j] = a[j - 1];
                    a[j - 1] = temp;
                }
            }
        }
            
        for(int i = 0; i < a.length; i++){
            System.out.print(a[i] + " ");
        }
    }
}
