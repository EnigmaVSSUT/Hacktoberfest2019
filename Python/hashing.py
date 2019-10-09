class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size  # keep the keys
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashFunction(key, len(self.slots))

        if (self.slots[hashvalue] == None):
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if (self.slots[hashvalue] == key):
                self.data[hashvalue] = data
            else:
                nextSlot = self.rehash(hashvalue, len(self.slots))
                while(self.slots[nextSlot] != None and self.slots[nextSlot] != key):
                    nextSlot = self.rehash(nextSlot, len(self.slots))
                if (self.slots[nextSlot] == None):
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    self.data[nextSlot] = data

    def hashFunction(self, key, size):
        return key % size

    def rehash(self, oldHashValue, size):
        return (oldHashValue + 1) % size

    def get(self, key):
        startSlot = self.hashFunction(key, len(self.slots))
        position = startSlot
        while(self.slots[position] != None):
            if (self.slots[position] == key):
                return self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startSlot:
                    return None
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
print(H.slots)
# [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
print(H.data)
print(H[20])
print(H[17])
H[20] = "duck"
print(H[20])
print(H.data)
print(H[99])
