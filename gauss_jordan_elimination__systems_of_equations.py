#The Gauss Jordan elimination method to solve systems of equations

import numpy as np

#step 1
#check if the first element of the row is 0
#if it is a 0, swap that row with another column
def check_if_zero(matrix_check,i_row,j_column):
    end=0
    j=1
    if matrix_check[i_row,j_column]==0:
        if matrix_check[i_row,j_column+j]!=0:
            temp=matrix_check[:,j_column]
            matrix_check[:,j_column]= matrix_check[:,j_column+j]
            matrix_check[:,j_column+j]= temp=matrix_check[:,j_column]
        else:
            j=j+1
    return matrix_check

#step2
#if the term in question is not 1, multiply the first row by a scalar
#in order to make the first term 1
def scalar_mult(matrix_scalar, a_matrix ,i_row,j_column):
    #if the term given is not equal to 1, perform the scalar multiplication
    if matrix_scalar[i_row][j_column]!=1:
        scalar=matrix_scalar[i_row,j_column]
        #print(scalar)
        for j in range (len(matrix_scalar[0])):
            matrix_scalar[i_row,j]=matrix_scalar[i_row,j]*1/scalar
            #print(matrix_scalar)
        a_matrix[i_row]=a_matrix[i_row]*1/scalar
        #print(a_matrix)
    return matrix_scalar,a_matrix

#step3
#sum all the rows below that row, a, with a multiple of the first element
#of row a that is not 0 in order to make their first coefficient 0
def step3(matrix_step3,a_matrix_step3,i_row,j_column):
    for i in range(i_row):
        multiplier=matrix_step3[i,j_column]
        #print(multiplier)
        for j in range (len(matrix_step3[0])):
            matrix_step3[i,j]= matrix_step3[i,j]-matrix_step3[i_row,j]*multiplier
            #print(matrix_step3)
        a_matrix_step3[i]=a_matrix_step3[i]-a_matrix_step3[i_row]*multiplier
    for i in range (i_row+1,len(matrix_step3[0])):
        multiplier=matrix_step3[i,j_column]
        #print(multiplier)
        for j in range (len(matrix_step3[0])):
            matrix_step3[i,j]= matrix_step3[i,j]-matrix_step3[i_row,j]*multiplier
            #print(matrix_step3)
        a_matrix_step3[i]=a_matrix_step3[i]-a_matrix_step3[i_row]*multiplier
        #print(a_matrix_step3)
    return matrix_step3,a_matrix_step3

#step4
#repeat the procedure (steps 1-3) diagonally

#define the gauss jordan function at this time
def gaussjordan(matrix_gauss,c_matrix):
    for i in range (len(matrix_gauss)):
        matrix_step1=check_if_zero(matrix_gauss,i,i)
        #print(matrix_step1)
        matrix_step2,c_matrix_step2=scalar_mult(matrix_step1,c_matrix,i,i)
        #print(matrix_step2)
        #print(c_matrix_step2)
        matrix_final,c_matrix_final=step3(matrix_step2,c_matrix_step2,i,i)
        #print(matrix_final)
        #print(c_matrix_final)
    return matrix_final,c_matrix_final


#for testing-
#equation 1 coefficients- x=1, y=-2, z=3, a=7
#equation 2 coefficients- x=2, y=1, z=1, a=4
#equation 3 coefficients- x=-3, y=2, z=-2, a=-10
#answers- x=2, y=-1, z=1

coefficients=np.array([[1,1,1],[2,3,5],[4,0,5]])
a=np.array([[5],[8],[2]])

xyz,answers=gaussjordan(coefficients,a)


print(xyz)
print(answers)






