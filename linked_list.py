class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Initialize a new Node with data and a None reference to next node.
        
        Args:
            data: Integer data to store in this node
        """
        self.data = data  # Store the data
        self.next = None  # Initialize next as None (no connection yet)


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        Initialize an empty linked list with head pointing to None.
        """
        self.head = None  # Start with an empty list

    def insert_at_front(self, data):
        """
        Insert a new node at the front of the list (O(1) operation).
        
        Args:
            data: Integer data for the new node
        """
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point new node to current head
        self.head = new_node  # Update head to the new node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list (O(n) operation).
        
        Args:
            data: Integer data for the new node
        """
        new_node = Node(data)  # Create a new node
        
        # If list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return
            
        # Helper function to recursively find the last node
        def find_last(current):
            if current.next is None:
                # Found the last node
                current.next = new_node
            else:
                # Keep searching
                find_last(current.next)
                
        # Start the recursive search from head
        find_last(self.head)

    def recursive_sum(self):
        """
        Calculate the sum of all node data using recursion.
        
        Returns:
            int: The sum of all node data in the list
        """
        # Helper function to calculate sum recursively
        def sum_helper(node):
            # Base case: if node is None, return 0
            if node is None:
                return 0
                
            # Recursive case: node's data + sum of remaining nodes
            return node.data + sum_helper(node.next)
            
        # Start recursion from the head
        return sum_helper(self.head)

    def recursive_reverse(self):
        """
        Reverse the linked list in-place using recursion.
        """
        # Helper function to recursively reverse the list
        def reverse_helper(prev, current):
            # Base case: if we've reached the end of the list
            if current is None:
                return prev  # prev becomes the new head
                
            # Save next node before changing pointers
            next_node = current.next
            
            # Reverse the pointer
            current.next = prev
            
            # Recurse with updated positions
            return reverse_helper(current, next_node)
            
        # Update head to the new head (originally the last node)
        self.head = reverse_helper(None, self.head)

    def recursive_search(self, target):
        """
        Search for a target value using recursion.
        
        Args:
            target: Integer value to search for
            
        Returns:
            bool: True if target exists in the list, False otherwise
        """
        # Helper function to search recursively
        def search_helper(node, target):
            # Base case 1: reached end of list without finding target
            if node is None:
                return False
                
            # Base case 2: found the target
            if node.data == target:
                return True
                
            # Recursive case: keep searching
            return search_helper(node.next, target)
            
        # Start recursion from the head
        return search_helper(self.head, target)

    def display(self):
        """
        Display the linked list in a user-friendly format.
        
        Returns:
            str: String representation of the list
        """
        # Helper function to build the string recursively
        def display_helper(node):
            if node is None:
                return "None"
            return f"{node.data} -> {display_helper(node.next)}"
            
        # Start recursion from the head
        result = display_helper(self.head)
        print(result)
        return result