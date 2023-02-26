from datetime import datetime


def actual_time():
    return str(datetime.utcnow())


if __name__ == "__main__":

    print(f"testing script - actual time {actual_time()}")
