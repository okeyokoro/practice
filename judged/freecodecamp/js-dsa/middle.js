function getMiddle(s)
{
  var x = Math.floor(s.length/2);
  if (s.length%2 == 0) {console.log(s[x-1]+s[x]) ;}
  else {console.log(s[x]); }
}

getMiddle("A")
