def product(l: list[int]) -> int:
    total = 1
    for val in l:
        total *= val

    return total


def product_of_array_except_self(nums: list[int]) -> list[int]:
    # NOTE: This calls product() n times!

    local_array: list[int] = []
    for i, _ in enumerate(nums):
        test_list = nums[:i] + nums[i + 1:]
        product_for_local_array = product(test_list)
        local_array.append(product_for_local_array)
    return local_array


def product_of_array_except_self_02(nums: list[int]) -> list[int]:
    # NOTE:  this calls product() ONCE!

    local_array: list[int] = []
    product_of_entire_array = product(nums)

    for val in nums:
        ans_for_local_array = product_of_entire_array // val
        local_array.append(ans_for_local_array)
    return local_array


def product_of_array_except_self_03(nums: list[int]) -> list[int]:
    # This solves it in a way that doesn't call an external function
    # and solves it with O(n).
    n = len(nums)
    local_array = [1] * len(nums)
    # print(local_array)  # [1, 1, 1, 1]
    current = 1
    for i in range(n):
        local_array[i] *= current
        current *= nums[i]
    # print(local_array)  # [1, 1, 2, 6]
    current = 1
    for i in range(n - 1, -1, -1):
        local_array[i] *= current
        current *= nums[i]
    # print(local_array)  # [24, 12, 8, 6]

    return local_array


def main() -> None:
    val = product_of_array_except_self_03([1, 2, 3, 4])
    print(val)
    # OUTPUT: [24,12,8,6]


if __name__ == '__main__':
    main()

    # public int[] productExceptSelf(int[] nums) {
    #     int n = nums.length;
    #     int ans[] = new int[n];
    #     Arrays.fill(ans, 1);
    #     int curr = 1;
    #     for(int i = 0; i < n; i++) {
    #         ans[i] *= curr;
    #         curr *= nums[i];
    #     }
    #     curr = 1;
    #     for(int i = n - 1; i >= 0; i--) {
    #         ans[i] *= curr;
    #         curr *= nums[i];
    #     }
    #     return ans;
    # }
