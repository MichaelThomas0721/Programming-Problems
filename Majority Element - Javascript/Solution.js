/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    map.set(nums[i], map.get(nums[i]) + 1 || 1);
  }
  return ([...map.entries()].reduce((a, e) => (e[1] > a[1] ? e : a)))[0];
};

//nums = [3, 2, 3];
nums = [2,2,1,1,1,2,2];
console.log(majorityElement(nums));
