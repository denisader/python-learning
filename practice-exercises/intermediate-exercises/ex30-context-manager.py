class DatabaseConnection:
    # this runs the moment with block starts
    def __enter__(self):
        print("Connecting to Database...")
        return self

    # this is the cleanup phase
    # it recieves information about any errors that
    #   happened inside the block (through exc_type, and so)
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing Database Connection safely.")
        return False

try:
    with DatabaseConnection as db:
        print("Processing data...")
        raise Exception("something went wrong")
except Exception as e:
    print(f"Error: {e}")