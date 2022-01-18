one = [ "", "one ", "two ", "three ", "four ",
"five ", "six ", "seven ", "eight ",
"nine ", "ten ", "eleven ", "twelve ",
"thirteen ", "fourteen ", "fifteen ",
"sixteen ", "seventeen ", "eighteen ",
“nineteen “]; ten = [ “”, “”, “twenty “, “thirty “, “forty “,
“fifty “, “sixty “, “seventy “, “eighty “,
“ninety “]; # This code only the range of 0 to 100
def numToWords(n, s): str = “”;
if (n > 19):
str += ten[n // 10] + one[n % 10];
else:
str += one[n];
if (n):
str += s; return str; # This is for 20 to almost infinity # Function to print a given number in words
def convertToWords(n):
out = “”;
out += numToWords((n // 10000000), “crore “);
out += numToWords(((n // 100000) % 100),”lakh “);
out += numToWords(((n // 1000) % 100),”thousand “);
out += numToWords(((n // 100) % 10),”hundred “); if (n > 100 and n % 100):
out += “and “;
out += numToWords((n % 100), “”); return out; print(convertToWords(8000));
