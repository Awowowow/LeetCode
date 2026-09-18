class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        index = 1
        front = curr.next

        firstCritical = -1
        prevCritical = -1
        minDistance = float('inf')

        while curr and curr.next:
            isCritical = (
                (curr.val < prev.val and curr.val < front.val)
                or
                (curr.val > prev.val and curr.val > front.val)
            )

            if isCritical:
                if firstCritical == -1:
                    firstCritical = index
                else:
                    minDistance = min(minDistance,index - prevCritical)
                prevCritical = index

            prev = curr
            curr = curr.next
            index += 1
            front = curr.next
        if firstCritical == -1 or firstCritical == prevCritical:
            return [-1, -1]
        maxDistance = prevCritical - firstCritical
        return [minDistance, maxDistance]