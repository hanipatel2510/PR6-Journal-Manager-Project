from datetime import datetime
import os

class JournalManager:
    def __init__(self, filename="Project-Task6-journal-Manager/journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry:\n")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if not os.path.exists(self.filename):
                with open(self.filename, "x") as f1:
                    pass
            with open(self.filename,"a") as f1:
                f1.write(f"[{timestamp}]\n{entry}\n\n")
            print("\nEntry added successfully!\n")
        except PermissionError:
            print("\nError: Permission denied to write to the file.\n")

    def view_entries(self):
        try:
            with open(self.filename,"r") as f2:
                data=f2.read()
        
            if data.strip():
                print("\nYour Journal Entries:")
                print("-------------------------")
                print(data)
                
            else:
                print("\nNo journal entries found. Start by adding a new entry!\n")
        
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.\n")

    def search_entry(self):
        try:
            user3 = input("\nEnter a keyword or date to search: ")
            with open(self.filename, "r") as f3:
                data = f3.read()

            entries = data.strip().split("\n\n")  
            found = False

            for line in entries:
                if user3.lower() in line.lower():
                    if not found:
                        print("\nMatching Entries:")
                        print("-------------------------")
                        found = True
                    print(line)
                    print()

            if not found:
                print(f"\nNo entries were found for the keyword: {user3}\n")

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.\n")


    def delete_entry(self):
        if not os.path.exists(self.filename):
            print("\nNo journal entries to delete.\n")
            return

        user4 = input("\nAre you sure you want to delete all entries? (yes/no): ")
        if user4.strip().lower() == "yes":
            try:
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.\n")
            except PermissionError:
                print("\nError: Permission denied to delete the file.\n")
        else:
            print("\nDeletion cancelled.\n")

journal = JournalManager()
print("Welcome to Personal Journal Manager!")

while True:
    print("Please select an option:\n")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")
    
    choice1 = input("User Input:\n").strip()
    
    match choice1:
        case "1":
            journal.add_entry()
        case "2":
            journal.view_entries()
        case "3":
            journal.search_entry()
        case "4":
            journal.delete_entry()
        case "5":
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break
        case _:
            print("\nInvalid option. Please select a valid option from the menu.\n")
