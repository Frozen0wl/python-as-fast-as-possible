public class sortingSystem {
    public sortingSystem() {
    }

    public static void main(String[] var0) {
        int[] var1 = new int[]{23, 124, 142, 214, 32};

        int var2;
        for(var2 = 0; var2 < var1.length; ++var2) {
            for(int var3 = 1; var3 < var1.length - var2; ++var3) {
                if (var1[var3] < var1[var3 - 1]) {
                    int var4 = var1[var3];
                    var1[var3] = var1[var3 - 1];
                    var1[var3 - 1] = var4;
                }
            }
        }

        for(var2 = 0; var2 < var1.length; ++var2) {
            System.out.print(var1[var2] + " ");
        }

    }
}