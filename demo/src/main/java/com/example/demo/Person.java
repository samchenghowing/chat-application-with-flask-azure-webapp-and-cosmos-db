package com.example.demo;

import javax.persistence.*;

@Entity
public class Person {

    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private int userID;
    private String userName;

    public int getUserID() {
        return userID;
    }
    public void setUserID(int userID) {
        this.userID = userID;
    }
    public String getUserName() {
        return userName;
    }
    public void setUserName(String userName) {
        this.userName = userName;
    }
    @Override
    public String toString() {
        return "User [userID=" + userID + ", userName=" + userName + "]";
    }
    public Person() {
    }
    public Person(String userName) {
        this.userName = userName;
    }
    public Person(int userID, String userName) {
        this.userID = userID;
        this.userName = userName;
    }
    
}
