from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    employee_ids = LinkedList()
    print("Created a new Linked List for employee IDs.")

    # 2) Insert some sample data using insert_at_front or insert_at_end
    print("\nAdding employee IDs to the list...")
    employee_ids.insert_at_front(101)
    employee_ids.insert_at_front(205)
    employee_ids.insert_at_end(307)
    employee_ids.insert_at_front(432)
    employee_ids.insert_at_end(568)

    # 3) Display the list to verify insertion
    print("\nCurrent employee ID list:")
    employee_ids.display()

    # 4) Call recursive_sum and print the result
    total = employee_ids.recursive_sum()
    print(f"\nSum of all employee IDs: {total}")

    # 5) Call recursive_search with a target and print result
    search_id = 307
    found = employee_ids.recursive_search(search_id)
    print(f"\nSearching for employee ID {search_id}: {'Found' if found else 'Not found'}")
    
    search_id = 999
    found = employee_ids.recursive_search(search_id)
    print(f"Searching for employee ID {search_id}: {'Found' if found else 'Not found'}")

    # 6) Call recursive_reverse, then display the reversed list
    print("\nReversing the employee ID list...")
    employee_ids.recursive_reverse()
    print("Reversed employee ID list:")
    employee_ids.display()

    print("\nAll operations completed successfully!")