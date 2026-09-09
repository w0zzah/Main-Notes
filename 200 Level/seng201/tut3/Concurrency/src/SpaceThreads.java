class SpaceThread implements Runnable {

    SpaceCounter counter;

    SpaceThread(SpaceCounter counter) {
        this.counter = counter;
    }

    @Override
    public void run() {
        for (int i = 0; i < 5000; i++) {
            this.counter.increaseCount();
        }
    }
}