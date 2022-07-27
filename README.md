# This repo contains solutions to all LeetCode problems I've solved

> The python programs are mine, the C++ solutions are mostly generated by GitHub Copilot. I'm trying to learn C++ by comparing the solutions to the solutions I've already written in python.

| No.  | Problem Name                                                                                   | Description                                                                                                                               | Solution                                                                                                                                                                        | Implementation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 217. | [Contains Duplicate](leetcode/containsDuplicate/containsDuplicate.py)                          | check if there are duplicates in the array                                                                                                | go through the array and store every number in a hashmap checking the hashmap if the number already exists...if it already exists then there's a duplicate otherwise not        | with python we can use the Counter from collections framework to get a dictionary of the items with their counts. Then we can take the maximum value out of the values array of the dictionary and check if its greater than 1...if it is greater than 1 that means there exists a item that occurs twice/ has a duplicate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 53.  | [Maximum Subarray](leetcode/maxSubarray/maxSubarray.py)                                        | Find the subarray with largest sum and return it                                                                                          | Kadane's algorithm is used in this problem.                                                                                                                                     | First we assume the first element to be the largest then we go through the array finding the current sum... if the current sum is greater than the maximum sum we update the max value to be equal to the current sum and return the max at the end. To find the current sum we take the max out of current value and the current value  + the current sum                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 1.   | [Two sum](leetcode/twoSum/twoSum.py)                                                           | Find the two numbers that add up to the target                                                                                            | we can use a hashmap to store the values of the array and then check if the target - the current value is in the hashmap if it is then we have found the two numbers            | in python enumerate can be used to avoid lookup times with index values.....other stuff is pretty much the same                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 88.  | [Merge Sorted arrays](leetcode/mergeSortedArray/mergeSortedArray.py)                           | Merge two arrays into one sorted array                                                                                                    | there are zeroes in the array that we have to avoid in the nums1 array the first m elements are the numbers other n are zeroes that we don't have to include in the final array | in python its really easy...we just delete all the elements after m index with the del operator and slicing then we can extend the nums1 in place and sort it in place with the .sort() method                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 350. | [Intersection of Two Arrays II](leetcode/intersectionOfTwoArrays2/intersectionOfTwoArrays2.py) | Return the intersection of two arrays preserving each element                                                                             | duplicate elements should be preserved therefore we cant use set in this                                                                                                        | we use Counter from collections framework to get their count. then we check if a number of nums1 is in nums2 if it is there then what is the minimum count...we append the number to our result that many times                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 121. | [Best Time to Buy and Sell Stock](leetcode/buyAndSellStock/buyAndSellStock.py)                 | Find the maximum profit that can be made by buying and selling a stock                                                                    | we go through the array finding the least price to buy and highest price to sell after that                                                                                     | **There are two ways to approach this problem:**</br></br>**1.** We take two pointers left and right and go through the list till right pointer reaches end if we find a right value that is greater than left one we set maxProfit to the maximum of the difference b/w two pointer values and the previous maxProfit....Otherwise we set left equal to right because that is the smallest value from left till right at the end of each iteration we increment right by 1...maxProfit value is returned in the end </br></br>**2.** We go through the list checking if the currentPrice-minPrice is greater than maxProfit if it is so we set maxProfit to the difference...we also check if the currentPrice is smaller than the minPrice if so we set the minPrice to currentPrice.....maxProfit is returned in the end |
| 704. | [Binary Search](leetcode/binarySearch/binarySearch.py)                                         | find target in the given array and return the index of the target if it exists                                                            | we can use the binary search algorithm to find the target in the array                                                                                                          | find mid point and check if the mid point is the target if it is then return mid point index if it is not then check if the mid point is greater than target if it is then we can search in the left half of the array else we can search in the right half of the array                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 278. | [First Bad Version](leetcode/firstBadVersion/firstBadVersion.py)                               | find the first bad version of a version control system                                                                                    | we can use the binary search algorithm to find the first bad version of a version control system                                                                                | if the midpoint is a bad version then we set the right pointer to mid because everything after it may or may not be bad but before it everything defo is bad....if we dont find a bad version then we increment the left pointer and continue....if left and right pointers are the same and its a bad version we return one of them                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 35.  | [Search insert position](leetcode/searchInsertPosition/searchInsertPosition.py)                | find the insert position of a number in a sorted array                                                                                    | we can use the binary search algorithm to find the insert position of a number in a sorted array                                                                                | its binary search except we return the left pointer if the item is not found because that will be the place to put the element if it were to be included in the array                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 977. | [Squares of a sorted array](leetcode/squaresOfSortedArray/squaresOfSortedArray.py)             | Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order. | we imploy two pointers                                                                                                                                                          | here we initialize the pointer at far ends of the array and then we check which value squared is greater the greater one is added to the array and left gets increment and if right is greater it gets decremented.... this way we have an decreasing array of squares so we return a reversed array which is in increasing order                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 189. | [Rotate Array](leetcode/rotateArray/rotateArray.py)                                            | Rotate an array of n elements to the right by k steps IN PLACE                                                                            |                                                                                                                                                                                 | **I've used two ways to solve this:**</br></br>**1.** simple way just go over the array k times and insert the last element at the first position with pop and insert....uses similar space but lot of time </br></br>**2.** first we mod the value k with the length of the array so if k was a big value it gets reduced then we rotate the whole array first then we rotate from start to k and then from k to end                                                                                                                                                                                                                                                                                                                                                                                                       |
