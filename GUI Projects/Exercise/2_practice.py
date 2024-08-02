# Event Management System with File Handling

# Initialize events.txt file with some initial events
def initialize_events_file():
    try:
        with open('events.txt', 'w') as file:
            file.write('1|Event 1|2023-03-01|10:00 AM\n')
            file.write('2|Event 2|2023-03-15|2:00 PM\n')
            file.write('3|Event 3|2023-04-01|5:00 PM\n')
    except Exception as e:
        print(f"Error initializing events file: {e}")

# Read and display all events from events.txt
def read_events():
    try:
        with open('events.txt', 'r') as file:
            events = file.readlines()
            for event in events:
                id, name, date, time = event.strip().split('|')
                print(f"ID: {id}, Name: {name}, Date: {date}, Time: {time}")
    except FileNotFoundError:
        print("Events file not found.")
    except Exception as e:
        print(f"Error reading events: {e}")

# Update an event by its ID
def update_event(id, name, date, time):
    try:
        with open('events.txt', 'r') as file:
            events = file.readlines()
        with open('events.txt', 'w') as file:
            for event in events:
                event_id, event_name, event_date, event_time = event.strip().split('|')
                if event_id == id:
                    file.write(f"{id}|{name}|{date}|{time}\n")
                else:
                    file.write(event)
    except FileNotFoundError:
        print("Events file not found.")
    except Exception as e:
        print(f"Error updating event: {e}")

# Delete an event by its ID
def delete_event(id):
    try:
        with open('events.txt', 'r') as file:
            events = file.readlines()
        with open('events.txt', 'w') as file:
            for event in events:
                event_id, _, _, _ = event.strip().split('|')
                if event_id != id:
                    file.write(event)
    except FileNotFoundError:
        print("Events file not found.")

# Main program
def main():
    initialize_events_file()
    while True:
        print("\nEvent Management System")
        print("1. Read all events")
        print("2. Update an event")
        choice = input("Choose an option: ")
        if choice == '1':
            read_events()
        elif choice == '2':
            id = input("Enter event ID: ")
            name = input("Enter new event name: ")
            date = input("Enter new event date: ")
            time = input("Enter new event time: ")
            update_event(id, name, date, time)

print(main())
