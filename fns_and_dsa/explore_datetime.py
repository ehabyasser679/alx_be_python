import datetime

def display_current_datetime():
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d-%H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date (number_of_days: int):
    future = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
    future_date = future.strftime("%Y-%m-%d-%H:%M:%S")
    print(f"Future date: {future_date}")

def main():
    display_current_datetime()
    
    number_of_days = int(input("Enter a number of days: "))

    calculate_future_date(number_of_days)

if __name__ == "__main__":
    main()