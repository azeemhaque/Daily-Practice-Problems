class Solution:
    def countVowelPermutation(self, n: int) -> int:
        prevA, prevE, prevI, prevO, prevU = 1,1,1,1,1
        MOD = 10**9 + 7
        
        for length in range(2, n+1):
            nextA = (prevE + prevU + prevI) % MOD
            nextE = (prevA + prevI) % MOD
            nextI = (prevE + prevO) % MOD
            nextO = prevI
            nextU = (prevO + prevI) % MOD
            
            prevA, prevE, prevI, prevO, prevU = nextA, nextE, nextI, nextO, nextU
            
        return(prevA + prevE + prevI + prevO + prevU) % MOD
    
