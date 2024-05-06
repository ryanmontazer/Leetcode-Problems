class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        my_dict1,array={},[]
        for char in pattern:
            if char not in my_dict1:
                my_dict1[char]=len(my_dict1)
            array.append(my_dict1[char])
        my_dict2,array1,word={},[],""
        for i in range(len(s)):
            char=s[i]
            if char!=" " and i!=len(s)-1:
                word+=char
            elif (char!=" " and i==len(s)-1) or char==" ":
                if i==len(s)-1:
                    word+=char
                if word not in my_dict2:
                    my_dict2[word]=len(my_dict2)
                array1.append(my_dict2[word])
                word=""
        return array==array1
