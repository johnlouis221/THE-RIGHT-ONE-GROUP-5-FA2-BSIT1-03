import time
from datetime import datetime, timedelta

users = {}
current_user = None

while True:
    if current_user == None:
        print("\n=== MAIN MENU ===")
        print("1. Register")
        print("2. Login")
        print("3. Help")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            user = input("Enter username: ")
            if user in users:
                print("Username already exists.")
            else:
                pw = input("Enter password: ")
                users[user] = {"pw": pw, "logs": []}
                print("Account created!")

        elif choice == "2":
            user = input("Username: ")
            pw = input("Password: ")
            if user in users and users[user]["pw"] == pw:
                print(f"Welcome, {user}!")
                current_user = user
            elif user not in users:
                print("User not found. Please try again.")
            else:
                print("Incorrect password. Please try again.")

        elif choice == "3":
            print("\n=== Help ===")
            print("Register Help:")
            print("-If you wanna register, Put number 1 to open the Register system.")
            print("-Put the Username and Password of your choice.")
            print("-After you register and make your own account, You can use it on the Log-in system.")
            print("Log-In:")
            print("-To access the Log-in system, Put number 2 on the Main Menu")
            print("-Put the Username and Password that you've created.")
            
            print("since we based our system into military time heres a                     simple guide to those who dont know a simple guide                      12:00 AM (midnight) → 00:00 1:00 AM → 01:00 2:00 AM → 02:00 3:00 AM → 03:00 4:00 AM → 04:00 5:00 AM → 05:006:00 AM → 06:007:00 AM → 07:00  8:00 AM → 08:0 09:00 AM → 09:00 10:00 AM → 10:00 11:00 AM → 11:00 2:00 PM (noon) → 12:00 1:00 PM → 13:00 2:00 PM → 14:00 3:00 PM → 15:00 4:00 PM → 16:00 5:00 Pm → 17:00 6:00 PM → 18:00 7:00 PM → 19:00 8:00 PM → 20:00 9:00 PM → 21:00 10:00 PM → 22:00 11:00 PM → 23:00")
            
        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please put the correct number")

    elif current_user != None:
        print(f"\n=== Welcome {current_user} ===")
        print("1. Add Log")
        print("2. View Logs")
        print("3. Dashboard")
        print("4. History")
        print("5. Tips")
        print("6. Reminder")
        print("7. Logout")
        choice = input("Choose: ")

        if choice == "1":
            s = input("Sleep time (HH:MM): ")
            e = input("Wake time (HH:MM): ")
            fmt = "%H:%M"
            t1 = datetime.strptime(s, fmt)
            t2 = datetime.strptime(e, fmt)
            if t2 < t1:
                t2 += timedelta(days=1)
            hours = round((t2 - t1).total_seconds() / 3600, 2)

            if hours < 4:
                quality = "Very Poor"
            elif hours < 6:
                quality = "Poor"
            elif hours < 7:
                quality = "Fair"
            elif hours <= 9:
                quality = "Good"
            else:
                quality = "Overslept"

            if hours < 7:
                print("Less than 7 hours of sleep!")

            users[current_user]["logs"].append({
                "date": datetime.now().strftime("%Y-%m-%d"),
                "hours": hours,
                "quality": quality
            })
            print(f"recorded: {hours} hrs | {quality}")

        elif choice == "2":
            logs = users[current_user]["logs"]
            if len(logs) == 0:
                print("No logs yet.")
            else:
                for i, l in enumerate(logs, 1):
                    print(f"{i}. {l['date']} - {l['hours']}h - {l['quality']}")

        elif choice == "3":
            logs = users[current_user]["logs"]
            if len(logs) == 0:
                print("No data.")
            else:
                total = 0
                good = 0
                for l in logs:
                    total += l["hours"]
                    if l["hours"] >= 7:
                        good += 1
                avg = total / len(logs)
                print(f"Total: {len(logs)} | Avg: {round(avg,2)}h | Enough Sleep: {good} | Lack: {len(logs)-good}")

        elif choice == "4":
            logs = users[current_user]["logs"][-7:]
            if len(logs) == 0:
                print("No logs.")
            else:
                for l in logs:
                    print(f"{l['date']} | {''*int(l['hours'])} {l['hours']}h")

        elif choice == "5":
            print("\n=== Sleep Tips ===")
            print("1. try working out 1hr before going to sleep to get your body exhaust and get comfy.")
            print("2. Avoid using phone before bedtime.")
            print("3. try playing classical or lofi music while on the bed.")
            print("4. Don't take any Caffeine before bedtime")
            print("5. counting sheep while on the bed")
            print("6. stop overthinking let every though release and be comfortable")

        elif choice == "6":
            sec = input("Seconds before reminder: ")
            try:
                sec = int(sec)
                print("Reminder set...")
                time.sleep(sec)
                print(" Time is up GO TO SLEEP NOW!")
            except:
                print("Invalid input.")

        elif choice == "7":
            print("Logged out.")
            current_user = None

        else:
            print("Invalid choice.")