var twoSum = function (nums, target) {

    if (nums.length < 2) return;
    if (nums.length === 2) return [0, 1];


    for (var i = 0; i < nums.length; i++) {

        for (var j = i + 1; j < nums.length; j++) {

            if (nums[i] + nums[j] === target) {

                return [i, j];
            }
        }

    }

};