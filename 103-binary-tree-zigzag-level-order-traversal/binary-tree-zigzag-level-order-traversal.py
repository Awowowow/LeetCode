from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []
        isLeft = True

        while queue:
            level = deque()
            levelSize = len(queue)
            for _ in range(levelSize):
                node = queue.popleft()
                if isLeft:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(level))
            isLeft = not isLeft
        return result