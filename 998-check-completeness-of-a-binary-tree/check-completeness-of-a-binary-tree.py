from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        queue = deque([root])
        ans = True
        NodeIsNone = False
        while queue:
            queueSize = len(queue)
            for _ in range(queueSize):
                node = queue.popleft()
                if node.left:
                    if NodeIsNone:
                        return False
                    queue.append(node.left)
                else:
                    NodeIsNone = True
                if node.right:
                    if NodeIsNone:
                        return False
                    queue.append(node.right)
                else:
                    NodeIsNone = True
        return ans
                

