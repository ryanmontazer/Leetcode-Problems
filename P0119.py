class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        previous_row_index=[1]
        current_row_index=[1,1]
        for i in range(2,rowIndex+1):
            #length of the i'th current_row_index will be i+1
            previous_row_index=[1]
            for j in range(0,i-1):
                previous_row_index.append(current_row_index[j]+current_row_index[j+1])
            previous_row_index.append(1)
            previous_row_index,current_row_index=current_row_index,previous_row_index
        return current_row_index
