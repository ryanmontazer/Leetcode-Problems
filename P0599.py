# Time: O((m+n)*l)
# Space: O(m*l)
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        my_dict={}
        #index2 is index of common string in list2 and min_value is the minimum i+j in description
        min_value, result=len(list1)+len(list2),[]
        for i in range(len(list1)):
            my_dict[list1[i]]=i
        for j in range(len(list2)):
            if list2[j] in my_dict:
                my_dict[list2[j]]+=j
                if my_dict[list2[j]]<min_value:
                    min_value=my_dict[list2[j]]
                    index2=[j]
                elif my_dict[list2[j]]==min_value:
                    index2.append(j)
        for index in index2:
            result.append(list2[index])
        return result
