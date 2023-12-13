import requests
import math

# Function to calculate distance between two points
def calculate_distance(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to retrieve data from the given URL
def retrieve_data(url):
    response = requests.get(url)
    data = response.json()
    order_list = []
    for item in data:
        order_list.append([item["latitude"], item["longitude"], item["_id"]])
    return order_list

# Function to optimize the delivery schedule using binary search
def optimize_delivery_schedule(order, store_location):
    l = 0
    r = 10**10
    agent_deliveries = []
    
    while l <= r:
        mid = (l + r) / 2
        temp_order = [[] for _ in range(10)]

        # Function to check if the given delivery schedule is feasible
        def check(mid):
            total = 0
            temp = list(order)
            total_distance = 0
            a, b = store_location
            while total < 10 and len(temp) > 0:
                distances = []
                index = 0
                for i, j, k in temp:
                    distances.append([calculate_distance([i, j], [a, b]), i, j, k, index])
                    index += 1
                distances.sort()
                total_distance += distances[0][0]
                final_distance = calculate_distance([store_location[0], store_location[1]], [distances[0][1], distances[0][2]])
                if total_distance + final_distance <= mid:
                    a, b = distances[0][1], distances[0][2]
                    temp_order[total].append(distances[0][3])
                    temp.pop(distances[0][4])
                else:
                    total += 1
                    total_distance = 0
                    a, b = store_location
            if len(temp) == 0:
                return temp_order
            else:
                return False

        if check(mid):
            agent_deliveries = temp_order.copy()
            r = mid - 1
        else:
            l = mid + 1

    remaining = 0
    for i in agent_deliveries:
        if len(i) == 0:
            remaining += 1

    leftover_orders = []
    for i in range(len(agent_deliveries)):
        if remaining == 0:
            break
        while len(agent_deliveries[i]) > 1 and remaining > 0:
            leftover_orders.append(agent_deliveries[i].pop())
            remaining -= 1

    for i in range(len(agent_deliveries)):
        if agent_deliveries[i] == []:
            agent_deliveries[i].append(leftover_orders.pop())

    return agent_deliveries

if __name__ == "__main__":
    # URL for retrieving data
    url = "https://zorang-recrutment.s3.ap-south-1.amazonaws.com/addresses.json"
    # Location of the store
    store_location = [28.9428, 77.2276]
    # Retrieve data from url
    orders = retrieve_data(url)
    # Optimize the delivery schedule
    optimized_schedule = optimize_delivery_schedule(orders, store_location)
    print(optimized_schedule)
