class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lower = max(weights)
        higher = sum(weights)
        while lower<higher:
            mid = (lower+higher)//2
            if self.check_status(mid,weights,days):
                higher = mid
            else:
                lower = mid+1
        return higher
            
            
    def check_status(self,limit,weights,days):
        day_ct =1
        capacity = 0
        for weight in weights:
            capacity+=weight
            if capacity>limit:
                day_ct+=1
                capacity = weight
        return day_ct<=days