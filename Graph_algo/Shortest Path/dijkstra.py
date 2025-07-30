def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (距離, 節點)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


if __name__ =='__main__':

  graph = {
      'A': {'B': 4, 'C': 1, 'D': 3},
      'B': {'A': 4, 'D': 2},
      'C': {'A': 1, 'D': 5 , 'E':10},
      'D': {'A': 3, 'B': 2, 'C': 5, 'E': 6},
      'E': {'C':10, 'D': 6}
  }
  # 使用 Dijkstra 演算法計算最短路徑
  start_node = 'A'
  dijkstra_result = dijkstra(graph, start_node)
  print("Dijkstra 最短路徑距離：", dijkstra_result)

