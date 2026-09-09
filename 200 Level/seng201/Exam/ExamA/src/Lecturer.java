public class Lecturer implements java.io.Serializable {
    public String name;
    public String address;
    public static String nhi;

    public int getUcnumber() {
        return ucnumber;
    }

    public void setUcnumber(int ucnumber) {
        this.ucnumber = ucnumber;
    }

    public static String getNhi() {
        return nhi;
    }

    public static void setNhi(String nhi) {
        Lecturer.nhi = nhi;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public transient int ucnumber;
}