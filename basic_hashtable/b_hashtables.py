

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    
    hashed_num = 5381
   
    for character in string:
        hashed_num = (( hashed_num << 5) + hashed_num) + ord(character)
    return hashed_num % max 
    

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    key_value_pair = Pair(key, value)

    hash_index = hash(key, hash_table.capacity)
    
    if hash_table.storage[hash_index] is not None:
        print(f"You're about to Overwrite the value at index {hash_index} of hash table.")
    
    hash_table.storage[hash_index] = key_value_pair




# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
   
    hash_index = hash(key, hash_table.capacity)

    if hash_table.storage[hash_index] is None:
        print(f"At index {hash_index} no value exists")
    else:
        hash_table.storage[hash_index] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    
    hash_index = hash(key, hash_table.capacity)
    
    if hash_table.storage[hash_index] is not None:
        return hash_table.storage[hash_index].value
    else:
        return None


# def insert_test():
#         # creates Hash Table stored under ht
#     ht = BasicHashTable(16)

#     hash_table_insert(ht, "line", "Yoooo")
#     hash_table_insert(ht, "second", "This is the second value")
#         # Retrieves key "second" and prints the value stored.
#     print(hash_table_retrieve(ht, "second"))

# insert_test()

# def remove_test():
#     #creates Hash Table stored under ht
#     ht = BasicHashTable(16)

#     #inserts key/value pair into ht(hashtable)
#     hash_table_insert(ht, "line", "Yoooo")
#     hash_table_insert(ht, "second", "This is the second value")

#     #removes key "second" from ht(hashtable)
#     hash_table_remove(ht, "second")

#     #attempts to retrieve removed key from ht(hashtable) and returns None
#     print(hash_table_retrieve(ht, "second"))

# remove_test()

def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    
    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
