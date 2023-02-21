package com.example.demo;

public class User {
    int userID;
    String userName;
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
    public User(int userID, String userName) {
        this.userID = userID;
        this.userName = userName;
    }
    
}
