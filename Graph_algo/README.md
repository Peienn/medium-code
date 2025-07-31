# 圖論筆記：Graph 基礎介紹

## 📌 圖的分類與表示方式

圖（Graph）是一種由 **節點（Vertices）**與**邊（Edges）** 所構成的資料結構，常用於表示網路、路徑或關係。可分成兩種 :

- **無向圖（Undirected Graph）**  
  邊沒有方向，`a — b` 表示雙向連接。

- **有向圖（Directed Graph）**  
  邊具有方向，`a → b` 表示從 a 指向 b。


## ✅ 兩種圖的特性說明

#### 無向圖（Undirected Graph）

- 所有節點的Degree = 2 x 邊數 ，因為每條邊會連接兩個節點。(必然為偶數)
- 使用鄰接矩陣時，矩陣為**對稱矩陣（Symmetric）**，可節省空間只存上三角或下三角。
- 所有節點皆可互相到達的話，稱 **Connected（連通）**：

(節點的Degree就是這個節點有幾個邊(Edge)的意思)
#### 有向圖（Directed Graph）

- 邊的總數等於所有節點的 **Out-degree** 總和 or **In-degree** 總和。 
- 鄰接矩陣不一定對稱。
- **Strongly Connected（強連通）**：任兩點之間皆存在**有向路徑**。

(有像圖有分Out-degree(節點指向誰) / In-degree(被節點指) )




## ✅ 圖的表示法

| 表示法             | 說明                                     |
|------------------|----------------------------------------|
| 鄰接矩陣（Adjacency Matrix） | 使用二維陣列表示，適合邊多的情況。 空間複雜度:O(V²) 。         |
| 鄰接串列（Adjacency List）  | 使用每個節點的串列記錄相鄰節點，適合邊少的情況。空間複雜度: O(V + E) 。 |

## ✅ 時間複雜度比較：Adjacency List vs Adjacency Matrix

> 註：`deg(u)` 表示頂點 `u` 的度數（degree），即與其相連的邊數。

| 操作                            | 無向圖 Adjacency Matrix | 無向圖 Adjacency List | 有向圖 Adjacency Matrix | 有向圖 Adjacency List |
|--------------------------------|---------------|--------------|----------------|--------------|
| 新增邊 `addEdge(u, v)`            | O(1)          | O(1)         | O(1)           | O(1)         |
| 刪除邊 `removeEdge(u, v)`           | O(1)          | O(deg(u))    | O(1)           | O(out_deg(u))|
| 檢查邊是否存在 `hasEdge(u, v)`      | O(1)          | O(deg(u))    | O(1)           | O(out_deg(u))|
| 走訪某頂點的所有相鄰頂點       | O(V)          | O(deg(u))    | O(V)           | O(out_deg(u))|
| 遍歷整張圖 (BFS / DFS)         | O(V²)         | O(V + E)     | O(V²)          | O(V + E)     |


![本地圖示](./11.png)

---

## 🧠 基於上述特性，在什麼情況下又會選擇哪種表示法？

| 頂點數 | 邊數 | 建議資料結構         | 原因                        |
|--------|------|----------------------|-----------------------------|
| 多     | 少   | Adjacency List       | 節省空間，Matrix 多為 0     |
| 多     | 多   | Adjacency Matrix     | 空間不浪費，查詢快         |
| 少     | 多   | Adjacency Matrix     | 不浪費空間，查詢快         |
| 少     | 少   | List / Matrix 均可   | 差異不大                   |

- **Adjacency List** 的空間複雜度是 $O(V + E)$，適合稀疏圖。
- **Adjacency Matrix** 的空間複雜度是 $O(V^2)$，查詢邊是否存在時間為 $O(1)$，適合密集圖。
- 稀疏圖：邊數接近 $O(V)$；密集圖：邊數接近 $O(V^2)$。


###  常見的演算法應用（BFS、DFS、Dijkstra）都會用  Adjacency List，就是因為多數實際應用中的圖（如社群網路、城市路網）通常是稀疏圖。



