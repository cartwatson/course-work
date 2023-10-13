import java.math.BigInteger;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.math.MathContext;
// import classes that give computer information
import java.lang.Runtime;

/**
 * @author Carter Watson A02312565@usu.edu
 * Satisfies requirements for assign2 of CS3100
*/
public class Assign2 {
    public static void main(String[] args) {
        int length = args.length;

        // NOTE from assign desc: "If no arguments, do nothing.""
        // Cover cases with no params or invalid number of params
        // if (length == 0 || length % 2 != 0) {
        //     System.out.println(
        //         "--- Assign 1 Help ---"
        //         + "\n  -fib [n] : Compute the Fibonacci of [n]; valid range [0, 40]"
        //         + "\n  -fac [n] : Compute the factorial of [n]; valid range, [0, 2147483647]"
        //         + "\n  -e [n] : Compute the value of 'e' using [n] iterations; valid range [1, 2147483647]"
        //     );
        //     return;
        // }

        // get runtime instance
        Runtime runtime = Runtime.getRuntime();

        // iterate through parameters
        for (int i = 0; i < length; i++) {
            // figure out how param should be used
            switch (args[i]) {
                // -cpu : Reports the number of CPUs (physical and logical) available.
                case "-cpu":
                    System.out.println("Processors\t: " + runtime.availableProcessors());
                    break;
                // -mem : Reports the available free memory, total memory, and max memory.
                case "-mem":
                    // TODO: format output with commas
                    System.out.printf("Free Memory\t: %,15d%n",  runtime.freeMemory());
                    System.out.printf("Total Memory\t: %,15d%n", runtime.totalMemory());
                    System.out.printf("Max Memory\t: %,15d%n",   runtime.maxMemory());
                    break;
                // -dirs : Reports the process working directory and the user's home directory.
                case "-dirs":
                    System.out.println("Working Dir\t: "   + System.getProperty("user.dir"));
                    System.out.println("User Home Dir\t: " + System.getProperty("user.home"));
                    break;
                // -os : Reports the OS name and OS version.
                case "-os":
                    System.out.println("OS Name\t\t: "    + System.getProperty("os.name"));
                    System.out.println("OS Version\t: " + System.getProperty("os.version"));
                    break;
                // -java : Reports the following items about the JVM { Java Vendor, Java Runtime Name, Java Version, Java VM Version, Java VM Name }
                case "-java":
                    System.out.println("Java Vendor\t: "     + System.getProperty("java.vendor"));
                    System.out.println("Java Runtime\t: "    + System.getProperty("java.runtime.name"));
                    System.out.println("Java Version\t: "    + System.getProperty("java.version"));
                    System.out.println("Java VM Version\t: " + System.getProperty("java.vm.version"));
                    System.out.println("Java VM Name\t: "    + System.getProperty("java.vm.name"));
                    break;
                default:
                    // NOTE from assign desc: "For invalid arguments, do nothing."
                    // if (args[i].charAt(0) == '-') {
                    //     System.out.println("Unknown command line argument: " + args[i]);
                    // }
                    break;
            }
        }
    }
}