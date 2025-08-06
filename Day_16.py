#Detect Cycle in a Linked List

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

n = int(input())
if n == 0:
    print('false')
else:
    values = list(map(int, input().split()))
    pos = int(input())
    nodes = [ListNode(values[i]) for i in range(n)]
    for i in range(n-1):
        nodes[i].next = nodes[i+1]
    head = nodes[0]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    print(str(hasCycle(head)).lower())
