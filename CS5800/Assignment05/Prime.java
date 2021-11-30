public class Prime {

        // method to check given number is prime or not
        public boolean isPrime(int number) {

                // declare a variable count and initialize with 0 used to store factor count
                int count = 0;
                for (int i = 1; i <= number; i++) {

                        // check number divisible by i
                        if (number % i == 0) {

                                // count increment by 1
                                count++;
                        }
                }

                // count value is equals to 2 then it is prime number
                if (count == 2) {
                        return true;
                } else {
                        return false;
                }
        }

}