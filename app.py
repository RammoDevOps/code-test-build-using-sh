import sys
from utils import is_disk_usage_high

def main():
    try:
        used = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Usage: python app.py <disk_usage_percent>")
        sys.exit(2)

    if is_disk_usage_high(used):
        print(f"WARNING: Disk usage is high ({used}%)")
        sys.exit(1)

    print(f"OK: Disk usage is normal ({used}%)")
    sys.exit(0)


if __name__ == "__main__":
    main()
