def insert(self,k,value):
    if self._n==self._capacity:
        self._resize(2*self._capacity)
    for j in range(self._n,k,-1):
        self._A[j]=self._A[j-1]
    self._A[k]=value
    self._n += 1