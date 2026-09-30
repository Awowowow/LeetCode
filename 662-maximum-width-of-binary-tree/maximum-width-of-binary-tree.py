from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        queue = deque([(root, 0)])
        ans = 1
        
        while queue:
            lenSize = len(queue)
            currentMax = 0
            value,startPosition = queue[0]
            valueTwo, endPosition = queue[-1]
            maxWidth = endPosition - startPosition + 1
            ans = max(maxWidth,ans)
            for i in range(lenSize):
                node,position = queue.popleft()
                if node.left:
                    queue.append((node.left,2 * position))
                if node.right:
                    queue.append((node.right,2 * position + 1))
        return ans