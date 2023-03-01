from collections import deque

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

def bfs(graph, node):
    visited = []
    # the video has queue as an array. I changed this to deque because popping the first element is O(1) instead of O(n).
    # see this link for more: https://wiki.python.org/moin/TimeComplexity.
    queue = deque()

    visited.append(node)
    queue.append(node)

    while queue:
        # popleft is O(1). for an array, pop(0) is O(n). hence the change to deque from array.
        s = queue.popleft()
        print(s, end = " ")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

def main():
    print("BFS: ")
    bfs(graph, 'A')

main()
