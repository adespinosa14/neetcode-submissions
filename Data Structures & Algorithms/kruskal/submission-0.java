// Create a new class Union Find

class UnionFind
{
    Map<Integer, Integer> par;
    Map<Integer, Integer> rank;
    int count;

    public UnionFind(int n)
    {
        count = n;
        par = new HashMap();
        rank = new HashMap();

        for(int i = 0; i < n; i++)
        {
            par.put(i, i);
            rank.put(i, 0);
        }
    }

    public int find(int n)
    {
        int p = par.get(n);
        while(p != par.get(p))
        {
            par.put(p, par.get(par.get(p)));
            p = par.get(p);
        }
        return p;
    }

    public boolean union(int n1, int n2)
    {
        int p1 = this.find(n1);
        int p2 = this.find(n2);

        if(p1 == p2) return false;

        if(rank.get(p1) > rank.get(p2))
        {
            par.put(p2, p1);
        }else if(rank.get(p1) < rank.get(p2))
        {
            par.put(p1,p2);
        }else
        {
            par.put(p1, p2);
            rank.put(p2, rank.get(p2) + 1);
        }
        count--;
        return true;
    }

    public int getCount()
    {
        return count;
    }

}

// MAIN FUNCTION
class Solution 
{

    public int minimumSpanningTree(List<List<Integer>> edges, int n) 
    {

        // Create Priority Queue for ordering in acending order
        //  * Needs lambda function to redirect the sort

        Queue<List<Integer>> minHeap = new PriorityQueue<>((n1, n2) -> (n1.get(0) - n2.get(0)));

        for (List<Integer> edge : edges)    
        {

            // Break down edge definition
            int n1 = edge.get(0), n2 = edge.get(1), weight = edge.get(2);
            
            // Add our broken down edges into a list
            minHeap.add(Arrays.asList(weight, n1, n2));
        }
        
        System.out.println("Hello Worlddd");
        
        // Define UnionFind and our Total Weight
        UnionFind u_find = new UnionFind(n);
        int total_weight = 0;

        // Iterate through our priority queue
        while(!minHeap.isEmpty())
        {
            // Pull out each list in our priority queue
            List<Integer> cur = minHeap.remove();

            // Define our edges
            int w1 = cur.get(0);
            int n1 = cur.get(1);
            int n2 = cur.get(2);

            // Ensure it does NOT form a cycle
            if(u_find.union(n1,n2))
            {
                total_weight += w1;
            }
        }


        // If we go through without any cycles, return total weight otherwise -1
        return u_find.getCount() == 1 ? total_weight : -1;
    }
}
