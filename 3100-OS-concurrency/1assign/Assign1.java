import java.math.BigInteger;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.math.MathContext;

/**
 * @author Carter Watson A02312565@usu.edu
 * Satisfies requirements for assign1 of CS3100
*/
public class Assign1 {
    public static void main(String[] args) {
        int length = args.length;

        // Cover cases with no params or invalid number of params
        if (length == 0 || length % 2 != 0) {
            System.out.println(
                "--- Assign 1 Help ---"
                + "\n  -fib [n] : Compute the Fibonacci of [n]; valid range [0, 40]"
                + "\n  -fac [n] : Compute the factorial of [n]; valid range, [0, 2147483647]"
                + "\n  -e [n] : Compute the value of 'e' using [n] iterations; valid range [1, 2147483647]"
            );
            return;
        }

        // iterate through parameters
        for (int i = 0; i < length; i++) {
            // figure out how param should be used
            switch (args[i]) {
                case "-fib":
                    try {
                        int n = Integer.parseInt(args[i + 1]);
                        // make sure value is in valid range
                        if (n >= 0 && n <= 40) {
                            System.out.println("Fibonacci of " + args[i + 1] + " is " + fibonacci(n));
                        } else {
                            System.out.println("Fibonacci valid range is [0, 40]");
                        }
                    } catch (Exception e) {
                        System.out.println("ERROR: -fib must be followed by an integer in range [0, 40]!");
                    }
                    break;
                case "-fac":
                    try {
                        int n = Integer.parseInt(args[i + 1]);
                        // make sure value is in valid range
                        if (n >= 0 && n <= 2147483647) {
                            System.out.println("Factorial of " + args[i + 1] + " is " + factorial(n));
                        } else {
                            System.out.println("Factorial valid range is [0, 2147483647]");
                        }
                    } catch (Exception e) {
                        System.out.println("ERROR: -fac must be followed by an integer in range [0, 2147483647]!");
                    }
                    break;
                case "-e":
                    try {
                        int n = Integer.parseInt(args[i + 1]);
                        // make sure value is in valid range
                        if (n >= 1 && n <= 2147483647) {
                            System.out.println("Value of e using " + args[i + 1] + " is " + calculateE(n));
                        } else {
                            System.out.println("Valid e iterations range is [1, 2147483647]");
                        }
                    } catch (Exception e) {
                        System.out.println("ERROR: -e must be followed by an integer in range [0, 2147483647]!");
                    }
                    break;
                default:
                    if (args[i].charAt(0) == '-') {
                        System.out.println("Unknown command line argument: " + args[i]);
                    }
                    break;
            }
        }
    }

    /**
     * @author Carter Watson A02312565@usu.edu
     * @param fib value in the fibonacci sequence
     * @return value of fib in the fibonacci sequence
     */
    private static int fibonacci(int fib) {
        if (fib <= 1) {
            return 1;
        }
        return fibonacci(fib - 1) + fibonacci(fib - 2);
    }

    /**
     * @author Carter Watson A02312565@usu.edu
     * @param fac number to compute the factorial of
     * @return computed factorial of fac
     */
    private static BigInteger factorial(int fac) {
        BigInteger result = new BigInteger("1");
        for (int i = 1; i <= fac; i++) {
            result = result.multiply(BigInteger.valueOf(i));
        }
        return result;
    }

    /**
     * @author Carter Watson A02312565@usu.edu
     * @param iterations how many iterations should be applied to computing e
     * @return computed value of e
     */
    private static BigDecimal calculateE(int iterations) {
        // init result, use a BigDecimal with a value of 2 to calculate e^2
        BigDecimal result = new BigDecimal("1");
        // calculate e^2
        for (int i = 1; i < iterations; i++) {
            result = result.add(new BigDecimal("2").pow(i).divide(factorialEHelper(i), 32, RoundingMode.HALF_UP));
        }
        // convert from e^2
        return result.sqrt(new MathContext(16));
    }

    /**
     * @desc computes factorial returning a BigDecimal
     * @author Carter Watson A02312565@usu.edu
     * @param fac number to compute the factorial of
     * @return computed factorial of fac
     */
    private static BigDecimal factorialEHelper(int fac) {
        if (fac == 1) {
            return new BigDecimal(1);
        }
        return new BigDecimal(fac).multiply(factorialEHelper(--fac));
    }
}