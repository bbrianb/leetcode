# Definition for singly-linked list.
from typing import Optional


class ListNode:
    # noinspection PyShadowingBuiltins
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        outputNode = ListNode()
        newNode = outputNode
        carry = 0
        while node1 is not None or node2 is not None or carry != 0:
            if node1 is not None or node2 is not None:
                value = carry
                if node1 is not None:
                    value += node1.val
                if node2 is not None:
                    value += node2.val
                if value > 9:
                    newNode.next = ListNode(value-10)
                    carry = 1
                else:
                    newNode.next = ListNode(value)
                    carry = 0
                newNode = newNode.next
                if node1 is not None:
                    node1 = node1.next
                if node2 is not None:
                    node2 = node2.next
                print(value, carry)
            else:
                newNode.next = ListNode(carry)
                carry = 0

        return outputNode.next

test_cases = (
    {
        'input': (
        ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
        ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    ),
    'output': (ListNode(),)
    },
)