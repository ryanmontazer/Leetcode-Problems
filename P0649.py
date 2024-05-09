class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        if senate.count("R")==0:
            return "Dire"
        if senate.count("D")==0:
            return "Radiant"
        array,array_dict=[],{"R":0,"D":0}
        for i in range(len(senate)):
            char=senate[i]
            if not array or char==array[-1]:
                array.append(char)
                array_dict[char]+=1
            #At this point char!=array[-1]
            elif  array_dict[array[-1]]>0:
                array_dict[array[-1]]-=1
            else:
                array_dict[char]+=1
                array.append(char)
            i+=1
            if i==len(senate) and array_dict[array[-1]]>0:
                char=array[-1]
                for j in range(array_dict[array[-1]]):
                    array.pop()
                    array.insert(0,char)
        return self.predictPartyVictory(array)
