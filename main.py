import sys
import time
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть кількість секунд як аргумент.")
        sys.exit(1)
    try:
        seconds = int(sys.argv[1])
    except ValueError:
        print("Аргумент повинен бути цілим числом.")
        sys.exit(1)

    for _ in range(seconds):
        print(datetime.now().strftime("%H:%M:%S"))
        time.sleep(1)

if __name__ == "__main__":
    main()
