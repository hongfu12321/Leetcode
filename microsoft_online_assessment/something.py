# a data structure that supports get, set and setAll in O(1)

# Keep 2 sets of keys, one set of keys will be reset every-time setAll is called.
# Keep a variable to track the last value set in setAll.
class CustomMap:
    def __init__(self):
        self.h = {}
        self.g = set()
        self.all_keys = set()
        self.last_v = None
        
    def set(self, k, v):
        self.h[k] = v
        self.g.add(k)
        self.all_keys.add(k)
    
    def get(self, k):
        if k in self.all_keys:
            if k in self.g:
                return self.h[k]
            return self.last_v
        return None
    
    def setAll(self, v):
        self.g = set()
        self.last_v = v



# You have a 2d map and coins on this map. Find the most optimal way of traversing the map 
# while collecting all the coins.