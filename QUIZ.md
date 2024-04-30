### How does the DevBoard handle received serial messages? How does this differ from the naïve approach?

The DevBoard now use interrupt to receive serial message. The naive way is to continuously read in the main `loop` for any coming signal. This "polling" is bad because we essentially waste CPU doing nothing but polling for data

### What does `detached_callback` do? What would happen if it wasn't used?

We need this to spawn new thread for every callback. Without this when we have any serial code that get stuck or just takes a long time, our UI will freeze for that time.

### What does `LockedSerial` do? Why is it _necessary_?

We need this to avoid race condition. Because we now spawn multiple threads, multiple threads could try to access the same serial port at once and this is undefined behavior - and we don't want this. The `LockSerial` essentially create a lock around the serial port such that only one thread can access it at a time