// Reference for Lanterna 3: https://github.com/mabe02/lanterna/blob/master/docs/contents.md
import com.googlecode.lanterna.TerminalSize;
import com.googlecode.lanterna.graphics.TextGraphics;
import com.googlecode.lanterna.screen.Screen;
import com.googlecode.lanterna.screen.TerminalScreen;
import com.googlecode.lanterna.terminal.DefaultTerminalFactory;
import com.googlecode.lanterna.terminal.Terminal;

public class ConwaysLife {
    public static void main(String[] args) {
        try {
            //laterna initializations
            Terminal terminal = new DefaultTerminalFactory().createTerminal();
            Screen screen = new TerminalScreen(terminal);
            TextGraphics graphics = screen.newTextGraphics();

            TerminalSize size = screen.getTerminalSize();
            //initialize instance of LifeSimulator
            LifeSimulator simulation = new LifeSimulator(size.getColumns(), size.getRows());

            //more laterna
            screen.startScreen();
            screen.setCursorPosition(null);

            //add patterns
            simulation.insertPattern(new PatternBlock(), 0, 0);
            simulation.insertPattern(new PatternBlinker(), 0, 10);
            simulation.insertPattern(new PatternGlider(), 15, 15);
            simulation.insertPattern(new PatternAcorn(), 10,10);

            //start simulation loop
            for (int i = 0; i < 50; i++) {
                render(simulation, screen, graphics);    // Render the current state of the simulation
                Thread.yield();                             // Let the JVM have some time to update other things
                Thread.sleep(100);                       // Sleep for a bit to make for a nicer paced animation
                simulation.update();                      // Tell the simulation to update
            }

            screen.stopScreen();
        } catch (Exception ex) {
            System.out.println("Something bad happened: " + ex.getMessage());
        }
    }

    public static void render(LifeSimulator simulation, Screen screen, TextGraphics graphics) {
        screen.clear();

        //loop through X values
        for (int i = 0; i < simulation.getSizeX(); i++) {
            //loop through Y values
            for (int j = 0; j < simulation.getSizeY(); j++) {
                //only render living cells
                if (simulation.getCell(i, j)) {
                    graphics.setCharacter(i, j, 'X');
                }
            }
        }

        // This is what causes the console to render the new state, it is required
        try {
            screen.refresh();
        } catch (Exception ex) {
        }
    }
}
