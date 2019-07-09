

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity



# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hashed_num = 5381
    
    for character in string:
        hashed_num = (( hashed_num << 5) + hashed_num) + ord(character)
    return hashed_num % max 


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hash_index = hash(key, hash_table.capacity)

    if hash_table.storage[hash_index]:
        #sets current to current hash index
        current = hash_table.storage[hash_index]
        #while current.next
        while current.next:
            #if key matches current.value = value
            if current.key == key:
                current.value = value
                return 
            #else move to next
            else:
                current.next
        #set current next to key/value pair     
        current.next = LinkedPair(key, value)
        
    else:
        hash_table.storage[hash_index] = LinkedPair(key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):

    hash_index = hash(key, hash_table.capacity)

    if hash_table.storage[hash_index]:
        found = False
        previous = None
        current = hash_table.storage[hash_index]

        while current.next:
            #while current.next if current.key == key then set found to the current key/value pair and break.
            if current.key == key:
                found = current
                break
            #else set previous to current and current to current.next to move to next node.
            else:
                previous = current
                current = current.next
        #if current.key == key then set found to the current key/value pair
        if current.key == key:
            found = current

        if found:
            if previous and previous is not current:
                previous.next = found.next
            elif previous:
                previous.next = None
            else:
                hash_table.storage[hashed_index] = None
            hash_table.count -= 1
            return None
        else:
            print(f"Can't find {hashed_index}. Can't delete")
            return None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    
    hash_index = hash(key, hash_table.capacity)
    
    if hash_table.storage[hash_index]:
        current = hash_table.storage[hash_index]
        while current.next:
            if current.key == key:
                return current.value
            else:
                current = current.next
        if current.key == key:
            return current.value
        else:
            return None
    else:
        return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
