function between(arr, x){
  for (var i=arr[0]; i<arr[1]; i++){
  if( (i == arr[1]-1 ) && x%i===0 ){return true;}
  else if (x%i===0){continue;}
  else{ return false;}
  }
}



function smallestCommons(arr) {
  arr = arr.sort((a,b)=>a-b);
  for (var n=1; n<1000; n++){
    var x = arr[1] * n;
    if ( between(arr, x) ){ return x;}
  }
}


console.log( smallestCommons([1,5]) );
