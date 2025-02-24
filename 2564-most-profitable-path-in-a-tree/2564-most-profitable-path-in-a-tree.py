class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = { i:[] for i in range(len(amount)) }
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
  
        def bob_path(node, parent, time):
            if node == 0:
                bob_time[node] = time
                return True
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if bob_path(neighbor, node, time + 1):
                    bob_time[node] = time
                    return True
            return False
        
        bob_time = {}
        bob_path(bob, -1, 0)

  
        def alice(node, parent, alice_time, total_profit):
            if alice_time < bob_time.get(node, float(inf)): 
                total_profit += amount[node]
            elif alice_time == bob_time.get(node, float(inf)):
                total_profit += amount[node]//2

            isLeaf = True
            max_profit = float(-inf)
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    isLeaf = False 
                    max_profit = max(max_profit, alice(neighbor, node, alice_time + 1, total_profit))
            
            if isLeaf:
                return total_profit
            return max_profit
        
        return alice(0, -1, 0, 0)