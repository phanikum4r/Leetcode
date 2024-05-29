class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)-1):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            j1,j2=0,len(matrix[0])-1
            while j1<j2:
                matrix[i][j1],matrix[i][j2]=matrix[i][j2],matrix[i][j1]
                j1+=1
                j2-=1