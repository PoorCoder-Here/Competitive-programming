def maxwater(height):
    i = 0
    j = len(height)-1
    maxArea = 0
    while i <= j:
          area = min(height[i], height[j])*(j-i)
          if area > maxArea:
             maxArea = area
          if height[i] < height[j]:
             i += 1
          else:
             j -= 1
                
    return maxArea
h=[7,1,3,8,2]
print(maxwater(h))
