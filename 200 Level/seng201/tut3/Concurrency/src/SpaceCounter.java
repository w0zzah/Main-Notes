public class SpaceCounter {
    int count = 0;
    public synchronized void increaseCount() {
        count++;
    }
    public synchronized int getCount() {
        return count;
    }

    static void main() throws InterruptedException {
        SpaceCounter counter = new SpaceCounter();
        Thread c1 = new Thread(() -> {
            for(int i = 0; i < 4999; i++) {
                counter.increaseCount();
            }
        });
        Thread c2 = new Thread(() -> {
            for (int i = 0; i < 4999; i++) {
                counter.increaseCount();
            }
        });

        c1.start();
        c2.start();
        c1.join();
        c2.join();
        System.out.println(counter.count);
    }
}