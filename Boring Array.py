from tkinter import N


"""
0<=k<= (n:=len(a))
1<=i1<=....<=ik<=n => add 1 to these indices
permute a 
can a be equal to b?
"""
class Solution():
    def solve(a,b):
        if len(a) != len(b) : return False


        x = [a[i]]