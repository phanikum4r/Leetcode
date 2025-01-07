class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        days = 0
        last = {}
        for task in tasks:
            day = last.get(task, -1)
            days_passed = days - day
            # task never encountered or cooldown completed
            if day == -1 or days_passed >= space:
                days += 1
                last[task] = days
            else:
                # calculate remaining days to wait
                days += space - days_passed + 1
                last[task] = days
        return days