import datetime

def main():
    # List of days for future dates
    days_from_now = [7, 21, 28, 30, 45, 90]
    
    # Get the current date
    today = datetime.date.today()
    print(f" Today is {today.strftime('%m-%d-%Y')}\n\n Days     SELL BY\n--------------------")
    # Calculate and display future dates for days_from_now
    for days in days_from_now:
        future_date = today + datetime.timedelta(days=days)
        if days > 9:
            print(f"  {days}  |  {future_date.strftime('%m-%d-%Y')}")
        else:
            print(f"  {days}   |  {future_date.strftime('%m-%d-%Y')}")

        
if __name__ == "__main__":
    main()
