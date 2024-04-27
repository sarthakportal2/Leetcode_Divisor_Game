class Solution:
    def divisorGame(self, n: int) -> bool:
        #T(C(N)==O(1)) and S(C(N)==O(1)) as it requires non memory space allocation recursively 
        if n%2==0:return True#printing True to the Even Game Win
        else:return False#Printing False to Game's UnWin
