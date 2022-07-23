# This repo contains solutions to all LeetCode problems I've solved

| No. | Problem Name | Description | Solution | Implementation |
| --- | ------------ | ----------- | -------- | -------------- |

217. |[Contains Duplicate](leetcode/containsDuplicate/containsDuplicate.py)  | check if there are duplicates in the array | go through the array and store every number in a hashmap checking the hashmap if the number already exists...if it already exists then there's a duplicate otherwise not | with python we can use the Counter from collections framework to get a dictionary of the items with their counts. Then we can take the maximum value out of the values array of the dictionary and check if its greater than 1...if it is greater than 1 that means there exists a item that occurs twice/ has a duplicate
            |Content Cell  | Content Cell
