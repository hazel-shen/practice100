# 53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

### Solution
```java
class Solution {
    public int maxSubArray(int[] nums) {
        
      int max = nums[0];
      int curr = nums[0];
      
      for (int i=1;i<nums.length;i++) {
          // 將現在的總和跟把下個元素加起來的總和比較，如果比較大的話就變成現在的總和
        curr = Math.max(curr + nums[i], nums[i]);
          // 將現在的總和和上一次加起來最大的總和比較，誰比較大就是最大的總和
        max = Math.max(curr, max);
      }
      return curr;
    }
}
```

### 思考方式
Test case: [-2,1,-3,4,-1,2,1,-5,4]


index-value curr max
1           1    1
-3          -2   1
4           4    4 
-1          3    4
2           5    5
1           6    6 
-5          1    6
4           5    6

### Reference

[Wiki - 最大子數列問題](https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98)