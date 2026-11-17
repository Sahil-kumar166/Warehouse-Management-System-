import itertools

class TSPSolver:
    def __init__(self, warehouse):
        self.warehouse = warehouse

    def solve_nearest_neighbor(self, order_items):
        unvisited = order_items[:]
        current_location = "START"
        route = [current_location]
        total_distance = 0

        while unvisited:
            nearest_item = min(unvisited, key=lambda item: self.warehouse.distance_between_items(current_location, item))
            distance = self.warehouse.distance_between_items(current_location, nearest_item)
            total_distance += distance
            route.append(nearest_item)
            current_location = nearest_item
            unvisited.remove(nearest_item)

        total_distance += self.warehouse.distance_between_items(current_location, "START")
        route.append("START")
        
        return route, total_distance

    def solve_exact(self, order_items):
        if len(order_items) > 9:
            print("  -> Order too large for exact solver. Using Nearest Neighbor heuristic...")
            return self.solve_nearest_neighbor(order_items)
        
        best_route = None
        min_distance = float('inf')

        for perm in itertools.permutations(order_items):
            route = ["START"] + list(perm) + ["START"]
            dist = 0
            for i in range(len(route) - 1):
                dist += self.warehouse.distance_between_items(route[i], route[i+1])
            
            if dist < min_distance:
                min_distance = dist
                best_route = route

        return best_route, min_distance
