although python provides a highly optimised dynamic array
of course we cannot actually grow the array its size is fized.If an element is appended to a list at atime when the underlying array is full we perform following
1. allocate a new array with large capacity like B for array A
2. set B[i]=A[i], for i=0,......,n-1 , where n denotes the current number
3. set A=B i.e. we hence use B as the array supporting the list
4. insert the new element in new array