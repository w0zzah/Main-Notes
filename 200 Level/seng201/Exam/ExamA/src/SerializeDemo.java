import java.io.*;
public class SerializeDemo {
    public static void main(String[] args) {
        Lecturer e = new Lecturer();
        e.setName("Ernest Rutherford");
        e.setAddress("Brightwater, NZ");
        Lecturer.setNhi("ERR1871");
        e.setUcnumber(1);
        try {
            FileOutputStream fileOut = new FileOutputStream("lecturer.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(e);
            out.close();
            fileOut.close();
            System.out.printf("Serialized data is saved in /lecturer.ser");
        } catch (IOException i) {
            i.printStackTrace();
        }
    }
}