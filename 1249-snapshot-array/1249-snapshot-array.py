class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.result = [{} for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.result[index][self.id] = val

    def snap(self) -> int:
        self.id += 1
        return self.id-1

    def get(self, index: int, snap_id: int) -> int:
        changes = self.result[index]
        if snap_id in changes:
            return changes[snap_id]
        
        # Otherwise, we need to find the most recent snap_id <= requested snap_id
        # This can be done by checking keys in reverse order
        for id in sorted(changes.keys(), reverse=True):
            if id <= snap_id:
                return changes[id]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)