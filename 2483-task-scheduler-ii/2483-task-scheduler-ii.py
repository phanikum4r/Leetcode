class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        days = 0
        last = {}
        for task in tasks:
            day = last.get(task, -1)
            days_passed = days - day
            if day == -1 or space <= days_passed:
                last[task] = days + 1
                days += 1
            else:
                days += space - days_passed + 1
                last[task] = days
        return days