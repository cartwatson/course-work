# Study Guide

## Memory Safety, Mutex Locks, Semaphores, Busy Wait

### Memory Safety

- **Definition**: Ensuring a program only accesses memory allocated to it.
- **Importance**: Prevents unintended behavior, crashes, and vulnerabilities.

### Mutex Locks

- **Definition**: Mutual exclusion lock, used to prevent multiple threads from concurrently executing critical sections of code that access shared data.
- **Usage**: 
  - `lock()`: Acquire the lock.
  - `unlock()`: Release the lock.

### Semaphores

- **Definition**: A synchronization primitive that controls access based on a counter.
- **Types**:
  - **Binary Semaphore**: Acts like a mutex.
  - **Counting Semaphore**: Allows multiple accesses up to a defined count.
- **Operations**:
  - `wait()`: Decrease counter and access if non-negative, else block.
  - `signal()`: Increase counter and possibly release a waiting process.

### Busy Wait

- **Definition**: A method where a process repeatedly checks to see if a condition is true, such as whether a lock is available.
- **Disadvantages**: Wastes CPU cycles, inefficient.
- **Alternatives**: Block and wake mechanisms.


## CPU, GPU, Vector Processing

### CPU (Central Processing Unit)

- **Definition**: Primary component of a computer that performs most processing.
- **Architecture**: Pipelining, multi-core, hyper-threading, etc.

### GPU (Graphics Processing Unit)

- **Definition**: Designed for rapid parallelized mathematical calculations. Initially for graphics, now for general-purpose tasks (GPGPU).
- **Architecture**: Thousands of smaller cores designed for multitasking.

### Vector Processing

- **Definition**: Uses SIMD (Single Instruction, Multiple Data) to perform one operation on multiple data points simultaneously.
- **Usage**: Graphic applications, scientific computations, etc.


## Caches

### Definition

- Temporary storage area that holds frequently accessed data, improving speed and performance.

### Levels

- **L1, L2, L3**:
  - L1: Smallest, fastest, closest to the core.
  - L3: Largest, slowest, can be shared among multiple cores.

### Cache Coherence

- Ensures all processors in a multi-core system see a consistent view of memory.

### Cache Miss vs Cache Hit

- **Cache Hit**: Desired data is found in the cache.
- **Cache Miss**: Desired data is not in the cache, leading to main memory access.


## Task-Parallelism vs Data-Parallelism

### Task-Parallelism

- **Definition**: Distribute tasks (code) across multiple cores or processors.
- **Use Cases**: When different tasks or processes can run concurrently without depending on each other.

### Data-Parallelism

- **Definition**: Distribute data across multiple cores or processors, and each core does the same operation on its own data subset.
- **Use Cases**: Algorithms where the same operation needs to be performed on large datasets, e.g., vector addition.

