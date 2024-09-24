/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
 function myfunc(nums,start,end){
    
    if(start>end){
        return null
    }
    
    let mid=Math.floor((start+end)/2)
    return new TreeNode(nums[mid],myfunc(nums,start,mid-1),myfunc(nums,mid+1,end))
    
    }
return myfunc(nums,0,nums.length-1)
};