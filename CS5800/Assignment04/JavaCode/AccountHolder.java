import java.util.Random;

public class AccountHolder 
    {
        protected int ID;
        protected String address;

        public AccountHolder(int ID, String address)
        {   }

        public static int NextID()
        {  
            return new Random().nextInt(1000000);
        }

    }

public class Account
    {
        private AccountHolder holder;
        private double balance = 0.0;

        public Account(double amt, AccountHolder holder)
        {   }

        public void deposit(double amt)
        {   }

        public void withdraw(double amt)
        {   }

        public double getBalance(double balance)
        {  
            return this.balance;
        }

        public AccountHolder getHolder(AccountHolder holder)
        {  
            return this.holder;
        }

        public void setBalance(double balance)
        {  
            this.balance = balance;
        }

        public AccountHolder setHolder(AccountHolder holder)
        {  
            return this.holder;
        }

    }    

