import csv

class Warehouse:
    def __init__(self, layout_file="locations.csv"):
        self.item_locations = {}
        self.load_locations(layout_file)

    def load_locations(self, filename):
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.item_locations[row['item_id']] = (int(row['x']), int(row['y']))
        except FileNotFoundError:
            print(f"Error: {filename} not found. Please ensure the layout file exists.")

    def get_location(self, item_id):
        return self.item_locations.get(item_id)

    def manhattan_distance(self, loc1, loc2):
        return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

    def distance_between_items(self, item1, item2):
        loc1 = self.get_location(item1)
        loc2 = self.get_location(item2)
        if not loc1 or not loc2:
            return float('inf')
        return self.manhattan_distance(loc1, loc2)
