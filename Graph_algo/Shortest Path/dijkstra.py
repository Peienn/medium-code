import heapq
from drawGraph import draw
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph} #找出每個節點最終需要的距離
    distances[start] = 0
    priority_queue = [(0, start)] 
   
    previous={node: 0 for node in graph}  # 找出前一位是誰
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                previous[neighbor] = (current_node,distance)
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    
    #將其轉換成List,畫圖用
    shortest_path_edges = []
    for i,value in previous.items():
        if value:
            shortest_path_edges.append( (i,value[0] , value[1]) )
    return distances , shortest_path_edges

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
  dijkstra_result,previous = dijkstra(graph, start_node)
  print("Dijkstra 最短路徑距離：", dijkstra_result)
  
  
  draw(graph,previous)
