// Create a new class Union Find



// MAIN FUNCTION
class Solution 
{

    public int minimumSpanningTree(List<List<Integer>> edges, int n) 
    {
        List<int[]> edges_list = new ArrayList<>();
        DSU union_find = new DSU(n);
        int total_weight = 0;
        int edges_used = 0;

        for(List<Integer> edge : edges)
        {
            edges_list.add(new int[]{edge.get(2), edge.get(0), edge.get(1)});
        }

        Collections.sort(edges_list, (a, b) -> a[0] - b[0]);

        for(int[] edge_curr : edges_list)
        {
            int weight = edge_curr[0];
            int x = edge_curr[1];
            int y = edge_curr[2];

            if(union_find.union(x, y))
            {
                total_weight += weight;
                edges_used += 1;
            }
        }

        return (edges_used == n - 1) ? total_weight :  -1;
    }

}

class DSU
{

    int[] parent;
    int[] rank;

    public DSU(int n)
    {
        parent = new int[n];
        rank = new int[n];

        for(int i = 0; i < n; i++)
        {
            parent[i] = i;
            rank[i] = 0;
        }
            
    }

    public int find(int x)
    {
        if(parent[x] != x)
            parent[x] = find(parent[x]);

        return parent[x];
    }

    public boolean union(int x, int y)
    {
        int rootX = find(x);
        int rootY = find(y);

        if(rootX == rootY) return false;

        if(rank[rootX] < rank[rootY])
        {
            parent[rootX] = rootY; 

        }else if(rank[rootX] > rank[rootY])
        {
            parent[rootY] = rootX;

        }else
        {
            parent[rootX] = rootY;
            rank[rootY]++;
        }

        return true;
    }

}

