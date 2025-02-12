import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;
/** Simple yet moderately fast I/O routines.
*
* Example usage:
*
* Kattio io = new Kattio(System.in, System.out);
*
* while (io.hasMoreTokens()) {
*    int n = io.getInt();
*    double d = io.getDouble();
*    double ans = d*n;
*
*    io.println("Answer: " + ans);
* }
*
* io.close();
*
*
* Some notes:
*
* - When done, you should always do io.close() or io.flush() on the
*   Kattio-instance, otherwise, you may lose output.
*
* - The getInt(), getDouble(), and getLong() methods will throw an
*   exception if there is no more data in the input, so it is generally
*   a good idea to use hasMoreTokens() to check for end-of-file.
*
* @author: Kattis
*/

class Kattio extends PrintWriter {
       public Kattio(InputStream i) {
           super(new BufferedOutputStream(System.out));
           r = new BufferedReader(new InputStreamReader(i));
       }
       public Kattio(InputStream i, OutputStream o) {
           super(new BufferedOutputStream(o));
           r = new BufferedReader(new InputStreamReader(i));
       }

       public boolean hasMoreTokens() {
           return peekToken() != null;
       }

       public int getInt() {
           return Integer.parseInt(nextToken());
       }

       public double getDouble() {
           return Double.parseDouble(nextToken());
       }

       public long getLong() {
           return Long.parseLong(nextToken());
       }

       public String getWord() {
           return nextToken();
       }



       private BufferedReader r;
       private String line;
       private StringTokenizer st;
       private String token;

       private String peekToken() {
           if (token == null)
               try {
                   while (st == null || !st.hasMoreTokens()) {
                       line = r.readLine();
                       if (line == null) return null;
                       st = new StringTokenizer(line);
                   }
                   token = st.nextToken();
               } catch (IOException e) { }
           return token;
       }

       private String nextToken() {
           String ans = peekToken();
           token = null;
           return ans;
       }
    }



public class largestIsland {

   
    char land = '@';  // Representerar land
    char water = '~';  // Representerar vatten

    // Riktningar som behövs när land position hittas
    int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

   
    //Hittar storleken på största ön på en 2D grid av land och vatten
    public int findLargestIsland(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }

        int rows = grid.length;
        int cols = grid[0].length;
        int largestIslandSize = 0;

        // For loopen går genom varje position i 2D griden
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // BFS börjar då vi stöter på land
                if (grid[i][j] == land) {
                    int currentIslandSize = bfs(grid, i, j, rows, cols);
                    largestIslandSize = Math.max(largestIslandSize, currentIslandSize);  // Lagrar tillfälliga största ön
                }
            }
        }
        return largestIslandSize;  // Returnerar största ö storleken
    }

    //Metoden använder BFS för att hitta öar i en 2D grid och antalet av de som befinner sig vid varandra
    private int bfs(char[][] grid, int startX, int startY, int rows, int cols) {
        // Använder deque för undersökande av olika positioner
        Deque<int[]> deque = new ArrayDeque<>();
        deque.add(new int[]{startX, startY});
        grid[startX][startY] = water;  // Markera start ön som vatten då vi redan räknat med den.
        int islandSize = 0;  // Lagrar storleken på nuvarande ön

        while (!deque.isEmpty()) {
            int[] current = deque.poll();  // Hämtar och tar bort nuvarande positionen från deque
            int x = current[0];
            int y = current[1];
            islandSize++;  // Ökar öns storlek med varje land position som besöks

            // Testar att gå upp ned höger och vänster om man land för att hitta ytterligare land
            for (int[] direction : directions) {
                int newX = x + direction[0];
                int newY = y + direction[1];

                // Avgränsar området som söks och undersöker om positionen är land
                if (newX >= 0 && newY >= 0 && newX < rows && newY < cols && grid[newX][newY] == land) {
                    deque.add(new int[]{newX, newY});  // Lägg till land positionen till deque
                    grid[newX][newY] = water;  // Markera land till vatten för att inte räkna med den en gång till
                }
            }
        }
        return islandSize;  // Returnerar öns storlek
    }

    public static void main(String[] args) {
        
        Kattio io = new Kattio(System.in,System.out); // Använd Kattio för att läsa in och skriva ut data

        // Läs in antalet rader och kolumner från indata
        int rows = io.getInt();
        int columns = io.getInt();

        // Skapa en matris för att hålla grid
        char[][] grid = new char[rows][columns];
        for (int i = 0; i < rows; i++) {
            grid[i] = io.getWord().toCharArray();
        }


        largestIsland islandFinder = new largestIsland();
        int result = islandFinder.findLargestIsland(grid);
        System.out.println( result); 
        io.close();
    }
}
