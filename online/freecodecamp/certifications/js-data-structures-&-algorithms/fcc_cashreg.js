function checkCashRegister(price, cash, cid) {
  var change = cash - price;
  var total = 0;
  var result = [["PENNY", 0.00], ["NICKEL", 0.00], ["DIME", 0.00], ["QUARTER", 0.00], ["ONE", 0.00], ["FIVE", 0.00], ["TEN", 0.00], ["TWENTY", 0.00], ["ONE HUNDRED", 0.000]];
  var final = [];

  for (var i=0; i<cid.length; i++){
    total += cid[i][1];
  }

if (total<change){ return "Insufficient Funds";} //more to do here
else if (total==change){ return "Closed";}
else{
  var xchange = change;
  while (xchange>0.000){

    if(xchange>=100 && cid[8][1] !== 0 ){
      cid[8][1] -= 100;
      result[8][1] += 100.00;
      xchange = (xchange-100).toFixed(2);
      continue;}
    else if(xchange>=20.0 && cid[7][1] !== 0 ){
      cid[7][1] -= 20;
      result[7][1]+= 20.00;
      xchange = (xchange-20).toFixed(2);
      continue;}
    else if(xchange>=10.0 && cid[6][1] !== 0 ){
      cid[6][1] -= 10;
      result[6][1]+= 10.00;
      xchange = (xchange-10).toFixed(2);
      continue;}
    else if(xchange>=5.0 && cid[5][1] !== 0 ){
      cid[5][1] -= 5;
      result[5][1] += 5.00;
      xchange = (xchange-5).toFixed(2);
      continue;}
    else if(xchange>=1.0 && cid[4][1] !== 0 ){
      cid[4][1] -= 1;
      result[4][1] += 1.00;
      xchange = (xchange-1).toFixed(2);
      continue;}
    else if(xchange>=0.25 && cid[3][1] !== 0 ){
      cid[3][1] -= 0.25;
      result[3][1] += 0.25;
      xchange = (xchange-0.25).toFixed(2);
      continue;}
    else if(xchange>=0.1 && cid[2][1] !== 0 ){
      cid[2][1] -= 0.1;
      result[2][1] += 0.10;
      xchange = (xchange-0.1).toFixed(2);
      continue;}
    else if(xchange>=0.05 && cid[1][1] !== 0 ){
      cid[1][1] -= 0.05;
      result[1][1] += 0.05;
      xchange = (xchange-0.05).toFixed(2);
      continue;}
    else if(xchange>=0.001 && cid[0][1] !== 0 ){
      cid[0][1] -= 0.001;
      result[0][1] += 0.001;
      xchange = (xchange-0.001).toFixed(3);
      }
      else{
        // console.log('Insufficient Funds');
        return 'Insufficient Funds';
      }

  }

  for (var j=result.length-1 ; j>=0; j--){
if( result[j][1] > 0){ result[j][1] = Math.round(result[j][1]*100)/100; final.push(result[j]);}
  }

  // console.log(final);
  // console.log(xchange);
  return final;
}

// main function
}


checkCashRegister(19.50, 20.00, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1.00], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]])
