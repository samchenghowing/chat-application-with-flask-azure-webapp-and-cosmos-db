<template>
  <div>
    <!-- <router-link to="/Home">Home</router-link> -->
    <p></p>
    <!-- <router-link to="/account">Account</router-link> -->
    <div class="chat-header">
      <h1>Chat</h1>
    </div>
    <div class="chat-messages">
      <div class="message" v-for="message in messages" :key="message.id">
        <div class="message-info">
          <div class="message-author">{{ message.author }}</div>
          <div class="message-timestamp">{{ message.timestamp }}</div>
        </div>
        <div class="message-text">{{ message.text }}</div>
      </div>
    </div>
    <div class="chat-input">
      <input type="text" v-model="messageText" @keyup.enter="sendMessage" />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>
  
<script>
export default {
  name: "ChatPage",
  data() {
    return {
      messages: [
        {
          id: 1,
          author: "Alice",
          timestamp: "12:01 PM",
          text: "Hey, how are you?",
        },
        {
          id: 2,
          author: "Bob",
          timestamp: "12:02 PM",
          text: "I'm doing well, thanks. How about you?",
        },
      ],
      messageText: "",
    };
  },
  methods: {
    sendMessage() {
      if (this.messageText.trim() === "") {
        return;
      }

      const newMessage = {
        id: this.messages.length + 1,
        author: "Alice",
        timestamp: new Date().toLocaleTimeString(),
        text: this.messageText,
      };

      this.messages.push(newMessage);
      this.messageText = "";
    },
  },
};
</script>
  
  <style>
.chat-header {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 5rem;
  background-color: #f2f2f2;
  border-bottom: 1px solid #e2e2e2;
}

.chat-messages {
  height: calc(100vh - 10rem);
  overflow-y: scroll;
  padding: 1rem;
}

.message {
  margin-bottom: 1rem;
}

.message-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.message-author {
  font-weight: bold;
}

.message-timestamp {
  color: #666;
}

.message-text {
  white-space: pre-wrap;
}

.chat-input {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 5rem;
  background-color: #f2f2f2;
  border-top: 1px solid #e2e2e2;
}

.chat-input input {
  flex-grow: 1;
  margin-right: 1rem;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.25rem;
}

.chat-input button {
  padding: 0.5rem;
  border: none;
  background-color: #333;
  color: white;
  border-radius: 0.25rem;
  cursor: pointer;
}
</style>
  