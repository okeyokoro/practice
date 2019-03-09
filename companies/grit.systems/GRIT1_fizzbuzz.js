for (var count=1; count < 101 ; count++) {
	var result = count;
	if (count%15 == 0){result = "FizzBuzz";}
  else if (count%3 == 0){result = "Fizz";}
  else if (count%5 == 0){result = "Buzz";}
	console.log(result)
}
