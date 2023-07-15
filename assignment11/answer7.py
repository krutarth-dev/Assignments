def search_range(nums, target):
    def find_left_position(nums, target):
        left = 0
        right = len(nums) - 1
        position = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

            if nums[mid] == target:
                position = mid

        return position

    def find_right_position(nums, target):
        left = 0
        right = len(nums) - 1
        position = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

            if nums[mid] == target:
                position = mid

        return position

    left_pos = find_left_position(nums, target)
    right_pos = find_right_position(nums, target)

    return [left_pos, right_pos]
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(search_range(nums, target)) 
