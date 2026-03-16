package com.devsecops;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class App {
    public static void main(String[] args) {
        String userId = args.length > 0 ? args[0] : "1";

        try {
            Connection conn = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/testdb",
                    "root",
                    "password"
            );

            Statement stmt = conn.createStatement();

            // SQL Injection vulnerability
            String query = "SELECT * FROM users WHERE id = '" + userId + "'";
            stmt.executeQuery(query);

            System.out.println("Query executed: " + query);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
