# will have to look into it deeply
 median(int arr[], int size){
   sort(arr, arr+size);
   if (size % 2 != 0)
      return (double)arr[size/2];
   return (double)(arr[(size-1)/2] + arr[size/2])/2.0;
}
def func(arr1, arr2):
    return

if __name__ == '__main__':
    arr1 = [ -5, 3, 6, 12, 15 ]
    arr2 = [ -12, -10, -6, -3, 4, 10 ]
    print(func(arr1, arr2))
