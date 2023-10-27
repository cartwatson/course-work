# High Performance Computing Study Guide

## Module 1: High Performance Computing (HPC)

### 1. Architecture of Supercomputers
- **Components**:
  - Processors (CPUs, GPUs, and other accelerators)
  - Memory (hierarchical design: cache, main memory, secondary storage)
  - Interconnection networks (topologies, bandwidth, latency)
  - I/O subsystems (storage hierarchies, data transfer rates)
- **Classification**:
  - Vector processors
  - MIMD machines
  - SIMD architectures
  - Hybrid systems (e.g., CPU-GPU systems)
- **Scalability and Modularity**:
  - Cluster architecture vs. Massively Parallel Processing (MPP)
  - Shared memory vs. Distributed memory models
- **Performance Metrics**:
  - Peak performance vs. Sustained performance
  - FLOPS
  - Bandwidth and latency
  - Efficiency and speedup

### 2. Parallel Hardware
- **Processor Design**:
  - Multicore processors
  - Symmetric Multiprocessing (SMP)
  - Hardware multithreading
- **Memory Architecture**:
  - Shared memory
  - Distributed memory
  - Cache coherence protocols
- **Interconnects**:
  - Buses, crossbars, and rings
  - Mesh, torus, and hypercube topologies
  - Switched networks (e.g., InfiniBand)
- **Specialized Accelerators**:
  - Graphics Processing Units (GPUs)
  - Field-Programmable Gate Arrays (FPGAs)
  - Application-specific integrated circuits (ASICs)
  - Tensor Processing Units (TPUs)

### 3. Parallel Software
- **Parallel Programming Paradigms**:
  - Shared memory programming (e.g., OpenMP)
  - Distributed memory programming (e.g., MPI - Message Passing Interface)
  - Partitioned Global Address Space (PGAS) languages
  - Data parallelism (e.g., CUDA for GPUs)
- **Parallel Algorithms & Patterns**:
  - Divide and conquer
  - Pipelining
  - Task parallelism
  - Data decomposition
  - Load balancing
- **Software Tools**:
  - Compilers and interpreters optimized for parallelism
  - Debuggers for parallel software (e.g., TotalView, DDT)
  - Performance analysis tools (e.g., TAU, PAPI)
- **Challenges**:
  - Deadlocks and race conditions
  - Load imbalance
  - Communication overhead
  - Scalability issues

## Module 2: Pthreads (POSIX Threads)

### 1. Introduction
- Definition: A POSIX standard for writing multithreaded programs.
- Benefits: Maximize CPU utilization, concurrent execution, responsive applications.
- **Basic Concepts**:
  - Thread
  - Thread Creation
  - Thread Termination
  - Thread ID
- **Synchronization**:
  - Mutexes (Mutual Exclusion)
  - Condition Variables
  - Deadlocks
- **Attributes**:
  - Thread Attributes
  - Mutex Attributes
  - Condition Variable Attributes
- **Challenges**:
  - Thread safety, race conditions, load balancing, overhead.
- **Code Sample**
```c++
#include <pthread.h>
#include <stdio.h>

void* printHello(void* arg) {
    printf("Hello from thread %ld!\n", (long)arg);
    pthread_exit(NULL);
}

int main() {
    pthread_t thread1, thread2;
    
    // Create two threads
    pthread_create(&thread1, NULL, printHello, (void*)1);
    pthread_create(&thread2, NULL, printHello, (void*)2);
    
    // Wait for the threads to finish
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    
    printf("Main thread exiting.\n");
    return 0;
}
```
**Advantages**:
1. **Flexibility**: Provides fine-grained control over thread behavior.
2. **Portability**: POSIX standard ensures cross-platform compatibility.
3. **Performance**: Potential for high performance due to manual control.

**Disadvantages**:
1. **Complexity**: Writing thread-safe code requires careful management of shared state, locks, and synchronizations.
2. **Error-prone**: Higher chances of bugs like race conditions, deadlocks, etc.
3. **No High-level Constructs**: Lacks higher-level parallelism constructs, increasing development time.

## Module 3: OpenMP (Open Multi-Processing)

### 1. Introduction
- Definition: API for multi-platform shared-memory parallel programming in C, C++, and Fortran.
- Key Features: Compiler directives, library routines, and environment variables.
- **Basic Directives**:
  - Parallel Regions
  - Work Sharing Constructs
  - Data Scope
- **Synchronization**:
  - Critical Sections
  - Locks
  - Barrier
  - Atomic
- **Tasking**:
  - Task creation
- **Environment & Configuration**:
  - Runtime Routines
  - Environment Variables
- **Code Sample**
```c++
#include <omp.h>
#include <stdio.h>

int main() {
    #pragma omp parallel for
    for(int i = 0; i < 10; i++) {
        printf("Thread %d executing iteration %d\n", omp_get_thread_num(), i);
    }

    printf("Main thread done.\n");
    return 0;
}
```
**Advantages**:
1. **Ease of Use**: Simple compiler directives make it easy to parallelize a serial program.
2. **Portability**: OpenMP is platform-independent.
3. **Scalability**: Easily scales by just increasing the number of threads.
4. **Shared Memory Model**: Allows easy access to shared variables.
5. **Flexible**: Offers both task and data parallelism.

**Disadvantages**:
1. **Memory Model**: Limited to shared memory systems (typically on a single node).
2. **Complexity**: Managing shared state can lead to synchronization overhead and race conditions.
3. **Granularity**: May not be ideal for fine-grained parallelism.


## Module 4: MPI (Message Passing Interface)

### 1. Introduction
- Definition: Standardized and portable message-passing system.
- Key Features: Designed for distributed memory systems.
- **Basic Concepts**:
  - Process
  - Communicator
- **Core MPI Functions**:
  - Initialization & Termination
  - Rank & Size
  - Point-to-Point Communication
  - Collective Operations
- **Advanced Topics**:
  - Derived Data Types
  - Virtual Topologies
  - Groups and Communicators
  - Asynchronous Communication
  - Persistent Communication Requests
- **Performance & Debugging**:
  - Profiling Interface
  - Performance Considerations
  - Common Errors
- **Code sample**
```c++
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    int rank, size;
    
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0) { // Master process
        int message = 123;
        MPI_Send(&message, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
        printf("Process 0 sent message %d to process 1\n", message);
    } else if (rank == 1) { // Worker process
        int received;
        MPI_Recv(&received, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Process 1 received message %d from process 0\n", received);
    }

    MPI_Finalize();
    return 0;
}
```
**Advantages**:
1. **Distributed Memory Model**: Allows for parallelism on distributed memory systems, including multi-node clusters.
2. **Scalability**: Easily scales to a large number of processes.
3. **Explicit Control**: Provides explicit control over message passing, allowing for optimized communication patterns.
4. **Portability**: MPI is a standard and can be used on various platforms and networks.

**Disadvantages**:
1. **Complexity**: Requires manual message passing which can be error-prone.
2. **Latency**: Communication between processes can introduce latency.
3. **Overhead**: Sending and receiving messages, especially on large systems, can introduce overhead.
4. **Learning Curve**: Requires understanding the distributed memory model and message-passing semantics.


## Module 5: Parallel I/O

### 1. Introduction to Parallel I/O
- **Definition**: Concurrent reading/writing operations to/from storage by multiple processes/threads.
- **Importance**: Avoiding I/O bottlenecks, optimizing data access for parallel applications.

### 2. Basic Concepts
- **Data Partitioning**: Blocking vs. non-blocking, or strided vs. contiguous.
- **Collective vs. Independent I/O**: Collective I/O involves synchronized operations among a group of processes.
- **Data Sieving**: Reading a large block containing desired data, then extracting needed parts.
- **Two-Phase I/O**: A combination of data sieving and collective I/O.

### 3. Parallel File Systems
- **Introduction**: File systems designed to support the concurrent I/O operations of parallel applications.
- **Examples**:
  - Lustre
  - GPFS (IBM's General Parallel File System)
  - PVFS (Parallel Virtual File System)
- **Features**: Striping data across multiple disks, redundancy, fault tolerance.

### 4. Parallel I/O Libraries and APIs
- **MPI-IO**: An extension of the MPI standard for parallel I/O.
  - Key Functions: `MPI_File_open()`, `MPI_File_read()`, `MPI_File_write()`, etc.
  - Derived datatypes and collective I/O.
- **HDF5 (Hierarchical Data Format)**:
  - Hierarchical data model and file format for storing complex data relationships, including metadata.
  - API for parallel I/O operations.
- **NetCDF (Network Common Data Form)**:
  - Set of software libraries and machine-independent data formats that support array-oriented scientific data.

### 5. Performance Optimization & Best Practices
- **Data Alignment**: Aligning data accesses with the boundaries in the file system to optimize I/O.
- **Data Aggregation**: Combining multiple small I/O operations into fewer larger operations.
- **Prefetching and Caching**: Reading data ahead of time and maintaining frequently accessed data in cache.
- **I/O Scheduling**: Prioritizing and scheduling I/O operations for better throughput.
- **Concurrency**: Maximizing the number of simultaneous I/O operations.

### 6. Challenges in Parallel I/O
- **Consistency and Coherency**: Ensuring data is consistent across multiple operations and processes.
- **Load Balancing**: Avoiding I/O hotspots and ensuring efficient utilization of I/O resources.
- **Scalability**: Ensuring I/O performance scales with the number of processes and size of data.

## Flynn's Taxonomy of Parallel Architectures

| Category | Description                                           | Use Cases                                                                 | Advantages                               | Limitations                             |
|----------|-------------------------------------------------------|---------------------------------------------------------------------------|------------------------------------------|-----------------------------------------|
| SISD     | Single processor executes a single instruction stream | Traditional general-purpose computing                                      | Simplicity, Deterministic behavior      | Can't exploit parallelism               |
| SIMD     | Single instruction on multiple data elements         | Large datasets where each operation is independent (e.g., image processing) | High data throughput                     | Depends on uniformity of operations     |
| MISD     | Different instructions on the same piece of data     | Fault-tolerant computing, certain signal processing tasks                  | Redundancy, Diverse computations on data | Limited practical use cases             |
| MIMD     | Different instructions on different data             | Complex applications with diverse tasks (e.g., simulations, AI)             | Flexibility, Exploits data & task parallelism | Communication overhead, Coordination challenges |

