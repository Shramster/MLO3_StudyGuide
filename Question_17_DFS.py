graph = {
  'A' : ['B','D','E'],
  'B' : ['A', 'C', 'E'],
  'C' : ['B', 'F'],
  'D' : ['A', 'G' ],
  'E' : ['A', 'B', 'G'],
  'F' : ['C'],
  'G' : ['D', 'E','H'],
  'H' : ['G', 'I'],
  'I' : ['H'],
}

def dfs(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node) 

    while stack:
        s = stack.pop()
        print(s, end = " ")

        # reverse iterate through edge list so results match recursive version
        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)

def main():
    print("DFS: ")
    dfs(graph, 'A')

main()
