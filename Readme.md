## Approach

### Data Retrieval:
- I have retrieved the data from the given URL and stored it as a list of sub-lists, each containing latitude, longitude, and ID.

### Optimization Algorithm:
- Utilizing the Binary Search Algorithm to determine the optimal delivery schedule.
- Starting from the maximum distance each agent can travel and iteratively checking if it's possible to assign orders within that limit.
- If feasible, assigning orders to agents while minimizing the total distance traveled. Otherwise, decreasing the maximum distance and trying again.

### Assigning Orders:
- For each iteration, creating a temporary empty list of sub-lists, each representing an agent.
- Calculating the distance from the store to each order.
- For each order, finding the closest agent with available capacity and adding the order to their list.
- If an agent reaches their capacity, moving to the next agent.
- This process continues until all orders are assigned or it's clear the current distance limit is not feasible.

### Balancing Assignments:
- After finding the optimal distance limit, checking if any agents have no orders.
- If so, distributing leftover orders from agents with more than one order to ensure everyone has at least one delivery.

### Output:
- The code ultimately outputs a list of sub-lists, each representing the orders assigned to a specific delivery agent.
