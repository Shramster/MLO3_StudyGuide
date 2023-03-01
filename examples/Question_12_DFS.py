graph = {
  '8' : ['3','10'],
  '3' : ['1', '6'],
  '10' : ['14'],
  '1' : [],
  '6' : ['4', '7'],
  '14' : ['13'],
    '4' : [],
    '7' : [],
  '13' : [],
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
    dfs(graph, '8')

main()
