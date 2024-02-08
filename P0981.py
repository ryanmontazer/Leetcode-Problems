#Time get: O(log(n))
#Space: O(n)
class TimeMap:

    def __init__(self):
        self.my_map={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.my_map:
            self.my_map[key].append([timestamp,value])
        else:
            self.my_map[key]=[[timestamp,value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_map or timestamp<self.my_map[key][0][0]:
            return ""
        else:
            result=self.my_map[key]        
            n=len(result)
            left,right=0,n-1
            while right>left:
                mid=(right+left)//2
                if timestamp>=result[mid+1][0] :
                    left=mid+1
                else:
                    right=mid
            return result[left][1]
                

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
