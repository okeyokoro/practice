function sumAll(arr) {
  var sum = 0;
  for (var i=arr.sort()[0];i<(arr.sort()[1])+1;i++ ){ sum+=i; }
  console.log( sum);
}

function test(arr){
  console.log(Math.max(arr[0],arr[1]))
}

test([10, 5])
