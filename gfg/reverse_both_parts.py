

from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""


class Solution:
    def reverse(self, head: Optional['Node'], k: int) -> Optional['Node']:
        # read till k
        # store in an array
        first = []
        node = head
        for i in range(1, k):
            first.append(node.data)
            node = node.next
        # read rest
        second = []
        while node is not None:
            second.append(node.data)
            node = node.next
        # reverse and concat both
        data = first[::-1]+second[::-1]

        # create new ll
        head = Node(data[0])
        tail = head
        for i in data:
            tail.next = Node(i)
            tail = tail.next
        return head


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while (node != None):
        print(node.data, end=" ")
        node = node.next
    print()


def inputList():
    n = int(input())  # lenght of link list
    # all data of linked list in a line
    data = [int(i) for i in input().strip().split()]
    head = Node(data[0])
    tail = head
    for i in range(1, n):
        tail.next = Node(data[i])
        tail = tail.next
    return head


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        head = inputList()

        k = int(input())

        obj = Solution()
        res = obj.reverse(head, k)

        printList(res)


# } Driver Code Ends
