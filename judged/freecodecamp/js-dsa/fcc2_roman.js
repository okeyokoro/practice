
function convertToRoman(num) {
  var roman, arr = Array.from(""+num).map(function (x){return parseInt(x,10);}).reverse(), ray = [];

  for (var i =0; i<arr.length; i++){ ray.push(arr[i]*(Math.pow(10, i))); }

  ray = ray.reverse();

  for(var j =0; j<ray.length; j++) {

    switch (ray[j]){
    case 0:
       ray[j] = "";
      break;
    case 1:
      ray[j] = "I";
      break;
    case 2:
      ray[j] = "II";
      break;
    case 3:
      ray[j] = "III";
      break;
    case 4:
      ray[j] = "IV";
      break;
    case 5:
      ray[j] = "V";
      break;
    case 6:
      ray[j] = "VI";
      break;
    case 7:
      ray[j] = "VII";
      break;
    case 8:
      ray[j] = "VIII";
      break;
    case 9:
      ray[j] = "IX";
      break;
    case 10:
      ray[j] = "X";
      break;
    case 20:
      ray[j] = "XX";
      break;
    case 30:
      ray[j] = "XXX";
      break;
    case 40:
      ray[j] = "XL";
      break;
    case 50:
      ray[j] = "L";
      break;
    case 60:
      ray[j] = "LX";
      break;
    case 70:
      ray[j] = "LXX";
      break;
    case 80:
      ray[j] = "LXXX";
      break;
    case 90:
      ray[j] = "XC";
      break;
    case 100:
      ray[j] = "C";
      break;
    case 200:
      ray[j] = "CC";
      break;
    case 300:
      ray[j] = "CCC";
      break;
    case 400:
      ray[j] = "CD";
      break;
    case 500:
      ray[j] = "D";
      break;
    case 600:
      ray[j] = "DC";
      break;
    case 700:
      ray[j] = "DCC";
      break;
    case 800:
      ray[j] = "DCCC";
      break;
    case 900:
      ray[j] = "CM";
      break;
    case 1000:
      ray[j] = "M";
      break;
    case 2000:
      ray[j] = "MM";
      break;
    case 3000:
      ray[j] = "MMM";
      break;
    case 4000:
      ray[j] = "MV";
      break;
    case 5000:
      ray[j] = "V";
      break;
    case 6000:
      ray[j] = "VM";
      break;
    case 7000:
      ray[j] = "VMM";
      break;
    case 8000:
      ray[j] = "VMMM";
      break;
    case 9000:
      ray[j] = "MX";
      break;
  }

  }


return ray.join("");
}

convertToRoman(36);
