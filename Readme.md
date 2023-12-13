## Approach:

**Data Retrieval:**

* I have retrieved the data from given URL and stored the retrieved data as a list of sub-lists, each containing the latitude, longitude and ID.

**Optimization Algorithm:**

* I have used Binary Search Algorithm to find the optimal delivery schedule.
* We start from the maximum distance each agent can travel and iteratively checks if it’s possible to assign order within that limit.
* If feasible, we assign orders to agents while minimizing the total distance travelled. Else, we decrease the maximum distance and tries again.

**Assigning Orders:**

* For each iteration, I have created a temporary empty list of sub-lists, each representing an agent.
* After that I have calculated the distance from the store to each order.
* For each order, I find the closest agent with available capacity and add the order to their list.
* If an agent reaches their capacity, it moves to the next agent.
* This process continues until all orders are assigned or it’s clear the current distance limit is not feasible.

**Balancing Assignments:**

* After finding the optimal distance limit, I check if any agents have no orders.
* If so, I distribute leftover order from agents with more than one order to ensure everyone has at least one delivery.

**Output:**

* The code ultimately outputs a list of sub-lists, each representing the orders assigned to a specific delivery agent.
