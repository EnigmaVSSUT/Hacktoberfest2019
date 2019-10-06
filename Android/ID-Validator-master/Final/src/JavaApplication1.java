/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */



/**
 *
 * @author mukhteerm8
 */
public class JavaApplication1 extends SignUpForm{
    
  public static boolean isIdValid (String id)
       {
            char[] idcharacters = id.toCharArray();
            int sum = 0;

            for (int i = 1; i <= idcharacters.length; i++) {
                int digit = Character.getNumericValue(idcharacters[idcharacters.length - i]);
                if ((i % 2) != 0) {
                    sum += digit;
                } else {
                    sum += digit < 5 ? digit * 2 : digit * 2 - 9;
                }
            }
            if((sum % 10) == 0)
            {
                System . out . println ("Valid id no."); 
                return true;
            }
            else 
            {
                 System . out . println ("Invalid id no."); 
            }
                return false;
                
        }




   public static void main(String [] args){
            
       JavaApplication1 application1 = new JavaApplication1();
        //insert your id number here
        application1.isIdValid("");
       
}
}
