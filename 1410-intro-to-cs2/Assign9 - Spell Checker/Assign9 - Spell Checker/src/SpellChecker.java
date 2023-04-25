import java.io.File;
import java.lang.reflect.Array;
import java.util.*;

public class SpellChecker {
    public static void main(String[] args) {

        // Step 1: Demonstrate tree capabilities
        System.out.println("Test Tree");
        testTree();

        // Step 2: Read the dictionary and report the tree statistics
        BinarySearchTree<String> dictionary = readDictionary();
        reportTreeStats(dictionary);

        // Step 3: Perform spell checking
        //read letter.txt--------------------------------------------------------------
        //code provided in assignment description
        //read in dictionary file
        System.out.println("-- Misspelled Words --");
        File file = new File("letter.txt");
        List<String> letter = new ArrayList<String>();
        try (Scanner input = new Scanner(file)) {
            while (input.hasNextLine()) {
                String word = input.next();
                //remove casing and punctuation
                word = word.replace(",", "");
                word = word.replace(":", "");
                word = word.replace(".", "");
                word = word.replace("!", "");
                word = word.replace("?", "");
                word = word.replace("(", "");
                word = word.replace(")", "");
                word = word.toLowerCase();
                //search and print misspelled words
                if (!dictionary.search(word)) {
                    //print word
                    System.out.println(word);
                }
            }

        }
        catch (java.io.IOException ex) {
            //output (to console) all misspelled words
            System.out.println("an error occurred trying to read the file. " + ex);
        }


    }

    /**
     * This method is used to help develop the BST, also for the grader to
     * evaluate if the BST is performing correctly.
     */
    public static void testTree() {
        BinarySearchTree<String> tree = new BinarySearchTree<>();

        //
        // Add a bunch of values to the tree
        tree.insert("Olga");
        tree.insert("Tomeka");
        tree.insert("Benjamin");
        tree.insert("Ulysses");
        tree.insert("Tanesha");
        tree.insert("Judie");
        tree.insert("Tisa");
        tree.insert("Santiago");
        tree.insert("Chia");
        tree.insert("Arden");

        //
        // Make sure it displays in sorted order
        tree.display("--- Initial Tree State ---");
        reportTreeStats(tree);

        //
        // Try to add a duplicate
        if (tree.insert("Tomeka")) {
            System.out.println("oops, shouldn't have returned true from the insert");
        }
        tree.display("--- After Adding Duplicate ---");
        reportTreeStats(tree);

        //
        // Remove some existing values from the tree
        tree.remove("Olga");    // Root node
        tree.remove("Arden");   // a leaf node
        tree.display("--- Removing Existing Values ---");
        reportTreeStats(tree);

        //
        // Remove a value that was never in the tree, hope it doesn't crash!
        tree.remove("Karl");
        tree.display("--- Removing A Non-Existent Value ---");
        reportTreeStats(tree);
    }

    /**
     * This method is used to report on some stats about the BST
     */
    public static void reportTreeStats(BinarySearchTree<String> tree) {
        System.out.println("-- Tree Stats --");
        System.out.printf("Total Nodes : %d\n", tree.numberNodes());
        System.out.printf("Leaf Nodes  : %d\n", tree.numberLeafNodes());
        System.out.printf("Tree Height : %d\n", tree.height());
    }

    /**
     * This method reads the dictionary and constructs the BST to be
     * used for the spell checking.
     */
    public static BinarySearchTree<String> readDictionary() {
        BinarySearchTree<String> tree = new BinarySearchTree<>();

        //code provided in assignment description
        //read in dictionary file
        File file = new File("dictionary.txt");
        List<String> dictionary = new ArrayList<String>();
        try (Scanner input = new Scanner(file)) {
            while (input.hasNextLine()) {
                String word = input.nextLine();
                //add to dictionary array
                dictionary.add(word);
            }
            //shuffle list (provided code)
            java.util.Collections.shuffle(dictionary, new java.util.Random(System.currentTimeMillis()));
            //initialize iterator
            ListIterator<String> iterator = dictionary.listIterator(0);
            //insert words into tree
            while (iterator.hasNext()) {
                tree.insert(iterator.next());
            }
        }
        catch (java.io.IOException ex) {
            System.out.println("an error occurred trying to read the file. " + ex);
        }

        return tree;
    }
}
