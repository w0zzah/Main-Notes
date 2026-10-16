
## One thread, many jobs
An embedded system like the UCFK4 has no operating system and no threads. Yet the program must refresh a multiplexed LED matrix, poll a button and count time all at once.
This lab focuses on how to **Fake Concurrency** by using **time-sliced polling**

### General
- Each task is successive, so minimize the impact on other tasks by making each as small as possinle
- Time is measured in ticks of a fixed rate loop
- Hardware that shares pins (The LED matrix and navswitch) is handled by taking turns (multiplexing)

#### Replace the task scheduler with a pacer
We use a pacer as it give a steady rate for the program to follow accounting for any loss time
```c
pacer_init(PACER_RATE);
while (1) {
	pacer_wait(); // Sleep until the next tick
	// ... do the work required for this tick
}
```

pacer_wait() blocks until the next tick boundary so the loop body runs exactly PACER_RATE times per second, provided the body takes less than one tick. At 500 Hz you have a budget of 2ms per iteration. Overrun it and you runn slower than intended

#### The OG, function pointers and a task table
```c
task_t tasks[] =
{
	{.func = name_task, .period = TASK_RATE / 2, .data = &state},
	{.func = name_task, .period = TASK_RATE / 3, .data = &state},
};
task_schedule(tasks, ARRAY_SIZE(tasks));
```

The scheduler is data-driven. Adding a task means adding a row.

The pacer approach is more mannual but more transparent. Each task gets a tick counter and the loop calls the task when the counter reaches the task's period in ticks.

**Choosing the rates in the real decision**

| Task      | Constraint                                                                                                                                               | Sensible Rate                      |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| Display   | The matrix shows one column at a time. With 5 columns, a full frame takes 5 calls. To avoid visible flicker you want a fram rate of about 100 Hz or more | 500 Hz (5 columns * 100 Hz frames) |
| Button    | Fast enough to feel instant, slow enough to be cheap. Human presses last tens of ms.                                                                     | 100 Hz or lower                    |
| Stopwatch | Whatever resolution you display at                                                                                                                       | 10Hz                               |

**The pacer rate must be at least the fastest task, and ideally every task rate divides it evenly (500/100 = 5,500/10 = 50), so there is no rounding drift.**

```c

```
