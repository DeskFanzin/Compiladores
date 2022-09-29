import java.util.*;
public class test{
    public static void main(String[] args){
        ArrayList<Integer> intArray = new ArrayList<Integer>();
        Scanner reader = new Scanner(System.in);
        for (int i = 0; i < 10; i++){
            int n = reader.nextInt();
            intArray.add(n);
        }
        reader.close();
        for (int i = 0; i < 10; i++){
            System.out.println(intArray.get(i));
        }
    }
}