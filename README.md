# Warehouse Order Picking System (Interactive CSV Layout Version)

This updated system allows you to dynamically manage warehouse layouts via a CSV file and manually input orders through an interactive command-line interface.

## New Features in this Version:
1. **Dynamic Warehouse Mapping**: The grid coordinates for all items are now stored in `locations.csv`. You can add new items or move existing ones without touching the Python code.
2. **Interactive CLI Prompt**: Instead of batch processing a static orders file, the program will ask you to type in the items you need to pick right when you run it.

## How to Run
1. Unzip the folder and navigate to it in your terminal.
2. Run the main script:
   ```bash
   python main.py
   ```
3. Type in the items you want to pick (e.g., `ITEM-002, ITEM-009, ITEM-012`).
4. To update the warehouse inventory or layout, open `locations.csv` and modify the coordinates.
