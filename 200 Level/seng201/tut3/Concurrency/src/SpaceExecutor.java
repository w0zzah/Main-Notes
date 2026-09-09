import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

public class SpaceExecutor {
    private final ExecutorService executor;

    public SpaceExecutor(int numThreads) {
        this.executor = Executors.newFixedThreadPool(numThreads);
    }

    public void addTask(Callable<?> task) {
        executor.submit(task);
    }

    public ExecutorService getExecutor() {
        return this.executor;
    }

    public void killExecutor() {
        executor.shutdownNow();
    }

    static void main() {
        SpaceExecutor taskMgr = new SpaceExecutor(1);

        Callable<?> longTask = () -> {
            Thread.sleep(500);
            return null;
        };

        taskMgr.addTask(longTask);
        taskMgr.addTask(longTask);

        ThreadPoolExecutor exec = (ThreadPoolExecutor) taskMgr.getExecutor();
        System.out.printf("Number of threads: %s%n", exec.getPoolSize());
        System.out.printf("Number of tasks in queue: %s%n", exec.getQueue().size());

        System.out.printf("Executor is running: %s%n", !exec.isShutdown());
        taskMgr.killExecutor();
        System.out.printf("Executor is running: %s%n", !exec.isShutdown());
    }
}