# run_start_job.py <number_of_iterations>
import sys
from start_job import start_job  # Import the start_job function from the start_job.py file

def main():
    if len(sys.argv) != 2:
        print("Usage: python run_start_job.py <number_of_iterations>")
        sys.exit(1)

    try:
        iterations = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for the number of iterations.")
        sys.exit(1)

    for _ in range(iterations):
        start_job()

if __name__ == "__main__":
    main()