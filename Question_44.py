graph = {
  'A' : ['B','D','G'],
  'B' : ['A', 'E'],
  'C' : ['D'],
  'D' : ['A', 'C', 'H'],
  'E' : ['B', 'H'],
  'F' : ['G', 'H'],
  'G' : ['A', 'F','H'],
  'H' : ['D', 'E', 'F', 'G'],
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
    dfs(graph, 'B')

main()
