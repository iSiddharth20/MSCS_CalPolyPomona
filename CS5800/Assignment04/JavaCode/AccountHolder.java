import java.util.Random;

public class AccountHolder {
  // AccountHolder holder = new AccountHolder();
  protected int ID;
  protected String address;

  public AccountHolder(int ID, String address)
  {   }

  public static int NextID()
  {  
      return new Random().nextInt(1000000);
  }

  public class Account {
    AccountHolder holder = new AccountHolder(ID, address);

    double balance = 0.0;

    public Account(double amt, AccountHolder holder){}

    
    public void deposit (double amt) {
      amt += balance;
    }

    public void Withdraw(double amt) {
      amt = balance - amt;
    }

    public double getBalance() {
      return this.balance;
    }

    AccountHolder getHolder() {
      return this.holder;
    }

    public void setBalance (double amt) {
      this.balance = amt;
    }

    public AccountHolder setHolder(AccountHolder holder)
    {  
      return holder;  
    }


  }

}

