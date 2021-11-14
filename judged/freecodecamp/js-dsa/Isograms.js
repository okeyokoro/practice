function isIsogram(word)
{
  var words = word.toLowerCase();
  var bank = [];
  var hold = [];

  for (var i =0; i<words.length; i++)
  { bank.push(words[i]);
  }

  for (var j=0; j<words.length; j++)
  {
    for (var k=j+1; k<words.length; k++)
    {  if (words[j]==words[k]) {hold.push(-1)}else{hold.push(0)}
    }
  }

  var sum = hold.reduce( function (a,b) {return a+b;},0)

  if (sum<0){ return false} else { return true}
}
