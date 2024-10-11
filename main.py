from src.tic_tac_toe import tic_tac_toe
import sys

if __name__ == "__main__":
    try:
        if len(sys.argv) != 1:
            print("Usage: ./tic-tac-toe")
        else:
            tic_tac_toe()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(84)