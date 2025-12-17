#!/usr/bin/env python3
from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date(number_of_days: int):
    future = datetime.now() + timedelta(days=number_of_days)
    future_date = future.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {future_date}")

def main():
    display_current_datetime()
    
    try:
        number_of_days = int(input("Enter a number of days to look ahead: "))
        calculate_future_date(number_of_days)
    except ValueError:
        print("Please enter a valid whole number for the days.")

if __name__ == "__main__":
    main()
