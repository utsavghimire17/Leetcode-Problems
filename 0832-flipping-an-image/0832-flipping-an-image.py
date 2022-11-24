class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        temp = {0:1,1:0}
        for row in range(len(image)):
            start = 0
            end = len(image[row]) - 1
            while start <= end:
                image[row][start],image[row][end] = image[row][end], image[row][start]
                if start == end:
                    image[row][start] = temp[image[row][start]]
                    start += 1
                else:
                    image[row][start] = temp[image[row][start]]
                    image[row][end] = temp[image[row][end]]
                    start += 1
                    end -= 1
        return image