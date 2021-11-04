public class ServiceQuote 
    {
        private Customer customer;
        private Employee employee;
        private double partsCharges;
        private double laborCharges;

        public ServiceQuote (Customer customer, Employee employee, double partsCharges, double laborCharges)
        {   }

        public double getTotalCharges()
        {
            return this.partsCharges + this.laborCharges;
        }

    }

