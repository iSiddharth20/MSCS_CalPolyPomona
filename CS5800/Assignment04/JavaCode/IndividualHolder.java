public class IndividualHolder 
    {
        private String name;
        private String SSN;

        public IndividualHolder(int ID, String address, String name, String SSN)
            {   }

        public String getName()
            {
                return this.name;
            }
        
        public String getSSN()
            {
                return this.SSN;
            }

        public void setName(String name)
            {
                this.name = name;
            }

        public void setSSN(String SSN)
            {
                this.SSN = SSN;
            }
    }

