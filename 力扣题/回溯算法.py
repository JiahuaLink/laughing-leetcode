# @Time    : 2021/12/20 23:32
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 回溯算法.py


def template(input: list):
        result = []
        global count
        count = 0
        def trace(path: list, choice):
            global count
            if len(path) == len(input):
                count += 1
                result.append(list(path))
                return
            for item in choice:
                if item in path: continue
                path.append(item)
                trace(path, choice)
                path.pop()

        trace([], input)
        return result


if __name__ == '__main__':
    input = [1, 2, 3, 4]

    print(template(input))
