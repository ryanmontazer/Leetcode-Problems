# Time: O(n)
# Space: O(1)
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        my_dict={5:0,10:0}
        for bill in bills:
            if bill==5:
                my_dict[5]+=1
            elif bill==10:
                my_dict[10]+=1
                if my_dict[5]>0:
                    my_dict[5]-=1
                else:
                    return False
            elif bill==20:
                if (my_dict[10]>0 and my_dict[5]>0):
                    my_dict[10]-=1
                    my_dict[5]-=1
                elif my_dict[5]>2:
                    my_dict[5]-=3
                else:
                    return False
        return True
