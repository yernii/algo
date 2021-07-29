from collections import defaultdict, deque
#         Pseudocode
# L —> An empty list that will contain the sorted elements
# S —> A set of all vertices with no incoming edges (i.e., having indegree 0)
 
# while S is non-empty do
#     remove a vertex n from S
#     add n to tail of L
#     for each vertex m with an edge e from n to m do
#         remove edge e from the graph
#         if m has no other incoming edges, then insert m into S
#             insert m into S
 
# if graph has edges then
#     return report “graph has at least one cycle”
# else
#     return L “a topologically sorted order”


# test case
numCourses=10
prerequisites=[[0,1],[1,4],[4,5]]


adj_list = defaultdict(list)
degree = {}
for dest, src in prerequisites:
    adj_list[src].append(dest)

    # Record degrees of incoming edjes
    degree[dest] = degree.get(dest, 0) + 1

# Queue with no in degree
queue = deque([k for k in range(numCourses) if k not in degree])

topSort_order = []

while queue:

    # Pop one node with 0 in-degree
    vertex = queue.popleft()
    topSort_order.append(vertex)

    # Reduce in-degree for all the neighbors
    if vertex in adj_list:
        for neighbor in adj_list[vertex]:
            degree[neighbor] -= 1

            # Add neighbor to Q for 0 case
            if degree[neighbor] == 0:
                queue.append(neighbor)
