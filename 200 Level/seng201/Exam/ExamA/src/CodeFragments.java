public class CodeFragments {


    void a() {
        System.out.println("Question 1.a :");
        int $villainEnergy = -1;
        System.out.println($villainEnergy++ + " and " + $villainEnergy);
    }

    void b() {
        System.out.println("\n Question 1.b :");
        String s1 = "SENG201";
        String s2 = "SENG202";
        s2 = s1;
        String s3 = "SENG" + "201";
        System.out.println(s3==s2);
    }

    void c() {
        System.out.println("\n Question 1.c :");
        int up = 10;
        int down = 4;
        System.out.println(up/down);
    }

    void d() {
        System.out.println("\n Question 1.d :");
        /*(String switch = "OFF"; <--Stop's compile as var name cant be a keyword*/
        /* if (switch == "ON")
        {
            System.out.println("The washing machine is on.");
        }
        else
        {
            System.out.println("The washing machine is off.");
        }
        */
        System.out.println("No Output! This will not compile as you cannot name variables under keywords");

    }
    public static void main(String[] args) {
        CodeFragments cf = new CodeFragments();
        cf.a();
        cf.b();
        cf.c();
        cf.d();
    }
}