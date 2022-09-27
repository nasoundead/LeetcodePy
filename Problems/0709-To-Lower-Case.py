"""
709. 转换成小写字母
给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。


示例 1：

输入：s = "Hello"
输出："hello"
示例 2：

输入：s = "here"
输出："here"
示例 3：

输入：s = "LOVELY"
输出："lovely"

提示：

1 <= s.length <= 100
s 由 ASCII 字符集中的可打印字符组成
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in s)


# print(ord("a"), ord("z"), ord("A"), ord("Z"))


def test1():
    s = Solution()
    ans = s.toLowerCase("Hello")
    print(ans)


test1()
