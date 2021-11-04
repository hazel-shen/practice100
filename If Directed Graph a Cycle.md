Description
Given a directed graph, detect whether the graph contains a cycle or not.

Solution: 
/* package whatever; // don't place package name! */
import java.io.*;
import java.util.LinkedList;
// O(v+e)
class myCode {

    static class Graph {
        int vertices;
        LinkedList < Integer > [] adjList;

        Graph(int vertices) {
            this.vertices = vertices;
            adjList = new LinkedList[vertices];
            for (int i = 0; i < vertices; i++) {
                adjList[i] = new LinkedList < > ();
            }
        }
        public void addEgde(int source, int destination) {
            adjList[source].addFirst(destination);
        }
        public boolean isCycle() {
            boolean visited[] = new boolean[vertices];
            boolean recursiveArr[] = new boolean[vertices];

            //do DFS from each node
            for (int i = 0; i < vertices; i++) {
                if (isCycleUtil(i, visited, recursiveArr))
                    return true;
            }
            return false;
        }

        public boolean isCycleUtil(int vertex, boolean[] visited, boolean[] recursiveArr) {
            visited[vertex] = true;
            recursiveArr[vertex] = true;

            //recursive call to all the adjacent vertices
            for (int i = 0; i < adjList[vertex].size(); i++) {
                //if not already visited
                int adjVertex = adjList[vertex].get(i);
                if (!visited[adjVertex] && isCycleUtil(adjVertex, visited, recursiveArr)) {
                    return true;
                } else if (recursiveArr[adjVertex])
                    return true;
            }
            //if reached here means cycle has not found in DFS from this vertex
            //reset
            recursiveArr[vertex] = false;
            return false;
        }
    }

    public static void main(String[] args) throws java.lang.Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int nodeNum = Integer.valueOf(br.readLine());
        Graph graph = new Graph(nodeNum);
        String input;
        while ((input = br.readLine()) != null) {
            graph.addEgde(Integer.valueOf(input.split(" ")[0]), (Integer.valueOf(input.split(" ")[1])));
        }

        boolean result = graph.isCycle();
        System.out.println(result);
    }
}
