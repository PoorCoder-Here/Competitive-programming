def lengthOfLongestSubstring(s):
        dict = {}
        l = -1
        ans = 0
        for i in range(len(s)):
            if s[i] in dict and dict[s[i]] > l:
                l = dict[s[i]]
            dict[s[i]] = i
            ans = max(ans, i-l)
        return ans
s=input()
print(lengthOfLongestSubstring(s))
