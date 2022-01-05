#example input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]

#solution
class MyHashSet:

    def __init__(self):
        #size of our hashset
        self.size = 10000
        
        #create empty hashset
        self.table = [None] * self.size
        
    def calculate_hash_value(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        #find hash value of given key
        val = self.calculate_hash_value(key)
        
        #if no bucket with desired hash value, create new bucket with that hash value and add the key
        if self.table[val] == None:
            self.table[val] = [key]
        
        #if hash value is in hashset, add key to the bucket
        else:
            self.table[val].append(key)

    def remove(self, key: int) -> None:
        val = self.calculate_hash_value(key)
        
        #if bucket with desired hash value is not empty
        if self.table[val] != None:
            
            #we want to remove all instances of the key if it is present
            while key in self.table[val]:
                self.table[val].remove(key)

    def contains(self, key: int) -> bool:
        val = self.calculate_hash_value(key)
        
        #if bucket with desired hash value is not empty
        if self.table[val] != None:
            
            #check if key is in bucket
            return key in self.table[val]
        
        #if bucket with desired hash value is empty, return false
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
