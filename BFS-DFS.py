graph = {
  'A' : ['B','C'],
  'B' : ['D'],
  'C' : ['F'],
  'D' : ['E', 'F'],
  'E' : [],
  'F' : ['A']
}
 
visited = [] # Keep track of visited nodes.
queue = []   # Queue
 
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 
        for neighbour in graph[s]:
              if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
 
# Driver Code
bfs(visited, graph, 'A')
dfs(visited, graph,'A')
