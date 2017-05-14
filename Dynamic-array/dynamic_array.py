import ctypes

class DynamicArray:
    """a dynamic array class link to a simplified python list"""

    def __init__(self):
        """create an empty array"""
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)
    def __len__(self):
        """returns no of elements stored in the array"""
        return self._n
    def __getitem__(self,k):
        """return k index element"""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self.A[k]

    def append(self,obj):
        """add object to the end of array"""
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        self.A[self._n]=obj
        self._n += 1

    def _resize(self,c):
        """resize internal array to capacity"""
        B=self._make_array(c)
        for k in range(self._n):
            B[k]=self._A[k]
        self._A=B
        self._capacity=c

    def _make_array(self,c):
        """return new array with capacity c"""
        return (c* ctypes.py_object)()