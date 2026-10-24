import json
import os

DATA_FILE = "records.json"


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_data(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


# --- DSA Algorithms ---

def merge_sort(arr, key, reverse=False):
    """Merge Sort implementation - O(n log n) time complexity."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key, reverse)
    right = merge_sort(arr[mid:], key, reverse)

    return merge(left, right, key, reverse)


def merge(left, right, key, reverse):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        condition = left[i][key] > right[j][key] if reverse else left[i][key] < right[j][key]
        if condition:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def binary_search_by_roll(students_sorted, target_roll):
    """Binary Search implementation - O(log n) time complexity."""
    low = 0
    high = len(students_sorted) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_roll = str(students_sorted[mid]["roll"])

        if mid_roll == str(target_roll):
            return students_sorted[mid]
        elif mid_roll < str(target_roll):
            low = mid + 1
        else:
            high = mid - 1

    return None


# --- Core System Operations ---

def add_student(students):
    roll = input("Enter Roll Number: ").strip()

    # Check for duplicate roll number
    for s in students:
        if str(s["roll"]) == roll:
            print("Error: Student with this Roll Number already exists!")
            return

    name = input("Enter Student Name: ").strip()
    try:
        marks = float(input("Enter Marks (0-100): "))
        if not (0 <= marks <= 100):
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Invalid input for marks. Must be a number.")
        return

    students.append({"roll": roll, "name": name, "marks": marks})
    save_data(students)
    print("Student added successfully!")


def display_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n" + "=" * 45)
    print(f"{'Roll No':<12} | {'Name':<20} | {'Marks':<6}")
    print("-" * 45)
    for s in students:
        print(f"{s['roll']:<12} | {s['name']:<20} | {s['marks']:<6.2f}")
    print("=" * 45)


def search_student(students):
    if not students:
        print("No student records available to search.")
        return

    roll = input("Enter Roll Number to search: ").strip()
    sorted_by_roll = merge_sort(students, key="roll")
    found = binary_search_by_roll(sorted_by_roll, roll)

    if found:
        print("\nStudent Found:")
        print(f"  Roll Number: {found['roll']}")
        print(f"  Name:        {found['name']}")
        print(f"  Marks:       {found['marks']}")
    else:
        print("Student not found.")


def delete_student(students):
    roll = input("Enter Roll Number to delete: ").strip()

    for i, s in enumerate(students):
        if str(s["roll"]) == roll:
            deleted = students.pop(i)
            save_data(students)
            print(f"Student '{deleted['name']}' (Roll: {roll}) deleted successfully!")
            return

    print("Student not found.")


def sort_menu(students):
    if not students:
        print("No student records to sort.")
        return students

    print("\n--- Sort Options ---")
    print("1. Sort by Roll Number (Ascending)")
    print("2. Sort by Marks / Merit List (Descending)")
    sub_choice = input("Select an option (1-2): ").strip()

    if sub_choice == "1":
        sorted_list = merge_sort(students, key="roll")
        print("\nRecords sorted by Roll Number:")
        display_students(sorted_list)
        return sorted_list
    elif sub_choice == "2":
        sorted_list = merge_sort(students, key="marks", reverse=True)
        print("\nMerit List (Highest Marks First):")
        display_students(sorted_list)
        return sorted_list
    else:
        print("Invalid choice.")
        return students


def main():
    students = load_data()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM (DSA) =====")
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Search by Roll Number (Binary Search)")
        print("4. Sort Records (Merge Sort)")
        print("5. Delete Student Record")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            students = sort_menu(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            save_data(students)
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid selection. Please choose 1-6.")


if __name__ == "__main__":
    main()
