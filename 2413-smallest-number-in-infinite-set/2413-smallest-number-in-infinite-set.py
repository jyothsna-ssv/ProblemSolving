class SmallestInfiniteSet:

    def __init__(self):
        self.next=1
        self.h=[]
        self.in_heap=set()
        

    def popSmallest(self) -> int:
        if self.h and self.h[0]<self.next:
            x=heapq.heappop(self.h)
            self.in_heap.remove(x)
            return x
        #else
        x=self.next
        self.next +=1
        return x


    def addBack(self, num: int) -> None:
        if num < self.next and num not in self.in_heap:
            heapq.heappush(self.h, num)
            self.in_heap.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)