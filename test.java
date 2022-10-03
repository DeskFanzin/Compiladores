import java.util.*;
public class test{
    public static void main(String[] args){
        String string = "2 + 4 - 20 test 20test*+";
        List<String> list = new ArrayList<String>();
        for (String s : string.split(" ")) {
            // finding only numbers
            if (s.matches("[0-9]+")) {
                list.add(s);
            }
            // finding only operators
            else if (s.matches("[+*]")) {
                list.add(s);
            }
        }
            System.out.println(list);
    }
}