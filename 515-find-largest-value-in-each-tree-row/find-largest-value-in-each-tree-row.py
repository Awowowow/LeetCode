from collections import deque
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            queueSize = len(queue)
            maxNum = float("-inf")
            for _ in range(queueSize):
                node = queue.popleft()
                maxNum = max(maxNum, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(maxNum)
        return ans