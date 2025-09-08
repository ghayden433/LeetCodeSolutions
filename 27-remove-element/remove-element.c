int removeElement(int* nums, int numsSize, int val) {
    int* pointer = nums;
    int* end = nums + numsSize;
    while (pointer < end) {
        if (*pointer == val){
            end--;
            *pointer = *end;
        }
        else pointer++;
    }
    return end - nums;
}