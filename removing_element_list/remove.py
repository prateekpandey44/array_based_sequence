def remove(self,value):
    for k in range(self.n):
        if self._A[k]==value:
            for j in range(k,self._n - 1):
                self._A[j]=self._A[j+1]
            self._A[self._n -1]=None
            self._n -= 1
            return
        raise ValueError('value not found')
