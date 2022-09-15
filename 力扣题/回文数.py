class Solution:
    def isPalindrome(self, x):
        # 利用转字符串 再用切片得到逆序字符串
        if str(x) == str(x)[::-1]:
            return True
        return False

if __name__ == '__main__':
    x = 121
    print(Solution().isPalindrome(x))