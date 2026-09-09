import java.io.*;
public class DeserializeDemo {
    public static void main(String[] args) {
        Lecturer e = null;
        try {
            FileInputStream fileIn = new FileInputStream("lecturer.ser");
            ObjectInputStream in = new ObjectInputStream(fileIn);
            e = (Lecturer) in.readObject();
            in.close();
            fileIn.close();
        } catch (IOException i) {
            i.printStackTrace();
            return;
        } catch (ClassNotFoundException c) {
            System.out.println("Lecturer class not found");
            c.printStackTrace();
            return;
        }
        System.out.println("Deserialized Lecturer...");
        System.out.println("Name: " + e.getName());
        System.out.println("Address: " + e.getAddress());
        System.out.println("NHI: " + Lecturer.getNhi());
        System.out.println("UC Number: " + e.getUcnumber());
    }
