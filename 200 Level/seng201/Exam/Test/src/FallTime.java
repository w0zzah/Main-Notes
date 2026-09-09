import com.sun.tools.javac.Main;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static java.lang.Math.sqrt;

public class FallTime {

    public static List<Double> calculateTime(double height, List<Double> gravity) {
        List<Double> nas = new ArrayList<>();

        gravity.forEach(value -> {
            double curr = value;
            double curfix = Math.sqrt(Math.pow(curr, 2));
            double newval = Math.sqrt(Math.pow(height, 2) / curfix);
            nas.add(newval);
        });
        return nas;
    }

    static void main() {
        List<Double> gravity = Arrays.asList(9.81, 0.00);
        System.out.println(FallTime.calculateTime(10, gravity));
    }

}
