class Solution:
    def isPalindrome(self, s: str) -> bool:
        mapping={"A":"a","B":"b","C":"c","D":"d","E":"e","F":"f","G":"g","H":"h","I":"i","J":"j","K":"k","L":"l","M":"m","N":"n","O":"o","P":"p","Q":"q","R":"r","S":"s","T":"t","U":"u","V":"v","W":"w","X":"x","Y":"y","Z":"z"}
        mapping.update({"a":"a","b":"b","c":"c","d":"d","e":"e","f":"f","g":"g","h":"h","i":"i","j":"j","k":"k","l":"l","m":"m","n":"n","o":"o","p":"p","q":"q","r":"r","s":"s","t":"t","u":"u","v":"v","w":"w","x":"x","y":"y","z":"z"})
        mapping.update({"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"})
        new_s=[]
        for char in s:
            if char in mapping :
                new_s.append(mapping[char])
        left,right=0,len(new_s)-1
        while left<right:
            if new_s[left]!=new_s[right]:
                return False
            else:
                left+=1
                right-=1
        return True
