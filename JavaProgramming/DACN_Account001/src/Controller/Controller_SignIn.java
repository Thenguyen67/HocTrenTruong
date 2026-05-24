package Controller;

import ConnectDB.Connect;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Controller_SignIn {
    
    public boolean ConnectLogin(String username, String password){
        
        Connection cnt = Connect.getConnection();
        
        String sql = "SELECT * FROM info_user WHERE user_name = ? AND password = ?";
        
        try {
            PreparedStatement ps = cnt.prepareStatement(sql);
            ps.setString(1, username);
            ps.setString(2, password);
            
            ResultSet rs = ps.executeQuery();
            
            if(rs.next()){
                return true;
            } else{
                return false;
            }
        } catch (SQLException ex) {
            Logger.getLogger(Controller_SignIn.class.getName()).log(Level.SEVERE, null, ex);
        }
        return false;
    }
}
