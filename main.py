from warehouse import Warehouse
from tsp_solver import TSPSolver

def main():
    # Load warehouse layout from CSV
    warehouse = Warehouse("locations.csv")
    solver = TSPSolver(warehouse)
    
    print("==================================================")
    print("   Warehouse Order Picking Management System      ")
    print("==================================================")
    
    while True:
        print("\nEnter the items you want to pick, separated by commas ")
        print("Type 'exit' or 'quit' to close the program.")
        
        user_input = input("> ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting system. Goodbye!")
            break
            
        if not user_input:
            continue
            
        # Clean and parse the input
        items = [item.strip() for item in user_input.split(',') if item.strip()]
        
        # Validate items against warehouse database
        invalid_items = [item for item in items if not warehouse.get_location(item)]
        if invalid_items:
            print(f"Error: The following items were not found in the warehouse layout: {', '.join(invalid_items)}")
            print("Please try again.")
            continue
            
        print(f"\nProcessing Order for {len(items)} items...")
        
        # Calculate optimal route
        route, distance = solver.solve_exact(items)
        
        print(f"Optimal Route: {' -> '.join(route)}")
        print(f"Total Travel Distance : {distance} units")

if __name__ == "__main__":
    main()
