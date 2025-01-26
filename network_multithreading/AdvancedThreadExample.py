import concurrent.futures
import time

def task(number):
    time.sleep(1)  # Simulate some work
    return number * 2

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    # Create a ThreadPoolExecutor with 3 worker threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the executor and get Future objects
        futures = [executor.submit(task, number) for number in numbers]

        # Process results as they become available
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                print(f"Task completed with result: {result}")
            except Exception as e:
                print(f"Task failed with exception: {e}")