"""
【最大括号嵌套深度】
题目：一字符串仅由三种（6个）括号组成，求嵌套深度，若不合法，输出0
分析：栈的应用，左括号入栈，遇到右括号出栈判断两个括号是否匹配，若匹配，继续，不匹配，则不合法，直至遍历完
"""


class Solution:
    def calculate_maxdepth(self, tasks: str) -> int:
        # 用于存放入栈的括号
        stack = []
        depth = 0
        # 用于判断字符串是否合法
        flag = True
        for i in tasks:
            if (i == '(') or (i == '[') or (i == "{"):
                stack.append(i)
                depth = max(depth, len(stack))
                continue
            if i == ")":
                if stack.pop() == "(":
                    continue
                else:
                    flag = False
                    break
            if i == "}":
                if stack.pop() == "{":
                    continue
                else:
                    flag = False
                    break
            if i == "]":
                if stack.pop() == "[":
                    continue
                else:
                    flag = False
                    break
        if flag:
            return depth if len(stack) == 0 else 0
        else:
            return 0


p = Solution()
print(p.calculate_maxdepth("([]{()})"))
