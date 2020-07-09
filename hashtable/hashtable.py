class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / len(self.data)



    def __str__(self):
        return f'There are {self.count} values in the Hash Table. The capacity is: {self.capacity} & The load capacity is {self.get_load_factor()}'



    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = ( hash * 33) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.data[index]

        if node is None:
            self.count += 1
            self.data[index] = HashTableEntry(key, value)
            return
        if node.key == key:
            self.count += 1
            self.data[index] = HashTableEntry(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        self.count += 1
        prev.next = HashTableEntry(key, value)

        # if node is not None:
        #     # print('Collision, overwriting the entry!')
        #     prev = node
        #     while node.next is not None:
        #         prev = node
        #         node = node.next
        #     prev.next = HashTableEntry(key, value)
        #     return
        # else:
        #     self.data[index] = HashTableEntry(key, value)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        current_entry = self.data[index]
        last_entry = None

        while current_entry is not None and current_entry.key != key:
            last_entry = current_entry
            current_entry = last_entry.next

        if current_entry is None:
            print("ERROR: Unable to remove entry with key " + key)
        else:
            if last_entry is None:  # Removing the first element in the LL
                self.data[index] = current_entry.next
            else:
                last_entry.next = current_entry.next


        # index = self.hash_index(key)
        # node = self.data[index]
        # # print("Key:", node.key, "Value:", node.value)
        # prev = node
        # while node is not None and node.key != key:
        #     prev = node
        #     node = node.next
        # if node is None:
        #     return None
        # else:
        #     # if prev is None:
        #     #     self.data[index] = node.next
        #     if node.next is not None:
        #         prev.next = node.next
        #         self.count -= 1
        #     else:
        #         prev.next = None
        #         self.count -= 1


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        index = self.hash_index(key)
        node = self.data[index]

        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

        # while node is not None and node.key != key:
        #     node = node.next
        # if node is None:
        #     return None
        # else:
        #     # while node.next is not None and node.key != key:
        #     #     prev = node
        #     #     node = node.next
        #     return node.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # load_factor = self.get_load_factor()

        # if load_factor > .7:
        #     self.capacity * 2

        new_arr = [None] * new_capacity

        for x in range(len(self.data)):
            curr = self.data[x]
            if curr is None:
                return
            new_arr[x] = HashTableEntry(curr.key, curr.value)
            # new_arr.put(curr.key, curr.value)
            while curr.next is not None:
                prev = curr
                new_arr[x].next = HashTableEntry(prev.next.key, prev.next.value)
                curr = curr.next

        # print(len(new_arr))
        # self.capacity = new_capacity

        self.data = new_arr

        # print(len(self.data))

        # new_array = [None] * new_capacity

        # for x in range(len(self.data)):
        #     curr = self.data[x]
        #     prev = curr
        #     new_array[x] = HashTableEntry(self.data[x].key, self.data[x].value)
        #     while self.data[x].next is not None:
        #         # curr = self.data[x]
        #         prev = curr
        #         curr = curr.next
        #     new_array[x].next = prev


        # self.data = new_array

        # # print(len(self.data))



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    # ht.resize(1024)
    # print(ht.get_num_slots())
    print(ht.__str__())
    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity1 = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity1}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
