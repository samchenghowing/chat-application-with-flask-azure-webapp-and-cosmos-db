<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col>
          <h1>
            Chat Room {{chatRoom}}          
            <v-btn
              @click="leftRoom"
            >
              Change chat room
            </v-btn>
          </h1>

          <div v-if="messages.length === 0">
            <h2>No messages yet... be the one to start!</h2>
          </div>
          <div v-else>
            <v-timeline align="start" density="compact">
              <v-timeline-item
                v-for="message in messages"
                :key="message.time"
                :dot-color="message.color"
                size="x-small"
              >
                <div class="mb-4">
                  <div class="font-weight-normal">
                    <strong>{{ message.name }}</strong> @{{ message.time }}
                  </div>
                  <div>{{ message.content }}</div>
                </div>
              </v-timeline-item>
            </v-timeline>
          </div>

          <v-text-field
            v-model="messageText"
            clearable
            label="Message"
            type="text"
            variant="outlined"
          >
            <template v-slot:append>
              <v-menu>
                <template v-slot:activator="{ props }">
                  <v-btn v-bind="props" class="mt-n2" @click="sendMessage">
                    Send
                    <v-icon icon="mdi-send" end></v-icon>
                  </v-btn>
                </template>
              </v-menu>
            </template>
          </v-text-field>
        </v-col>
      </v-row>
    </v-container>
        
    <v-row justify="center">
      <v-dialog
        v-model="dialog"
        persistent
        width="auto"
      >
        <v-card>
          <v-card-title class="text-h5">
            Chatrooms
          </v-card-title>
          <v-card-text>Choose a chatroom to start chatting</v-card-text>

          <v-combobox
            v-model="chatRoom"
            label="chatRoom"
            :items="items"
          >
          </v-combobox>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              v-model="confirmButton"
              :disabled="!items.length"
              @click="joinRoom"
            >
              Confirm
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </v-form>
</template>

<script>
import io from "socket.io-client";

export default {
  name: "ChatPage",
  data() {
    return {
      user: "",
      messages: [],
      messageText: "",
      dialog: true,
      items: [1, 2, 3],
      chatRoom: 1,
      socket: io(process.env.VUE_APP_CHAT_URL),
    };
  },
  created() {
    this.socket.on('message', (data) => {
      var message = data["msg"]["msg"]
      var obj = JSON.parse(message)
      this.messages.push(obj)
    })

    // TO-DO
    // this.socket.on('status', (data) => {})
  },
  methods: {
    joinRoom(){
      var obj = JSON.parse(sessionStorage.user)
      var name = obj["User info"]["name"]
      var userID = obj["User info"]["id"]
      var pwHash = obj["User info"]["pwHash"]
      var currentDate = new Date()

      this.socket.emit('joined', {
        msg: JSON.stringify({ 
          room: this.chatRoom,
          userID: userID,
          name: name,
          pwHash: pwHash,
          content: "joined",
          time: currentDate,
        })
      })
      this.dialog = false
    },

    leftRoom(){
      var obj = JSON.parse(sessionStorage.user)
      var name = obj["User info"]["name"]
      var userID = obj["User info"]["id"]
      var pwHash = obj["User info"]["pwHash"]
      var currentDate = new Date()

      // left current room first
      this.socket.emit('left', {
        msg: JSON.stringify({ 
          room: this.chatRoom,
          userID: userID,
          name: name,
          pwHash: pwHash,
          content: "joined",
          time: currentDate,
        })
      })
      this.dialog = true
    },

    sendMessage() {
      if (this.messageText.trim() === "") {
        return;
      }
      var obj = JSON.parse(sessionStorage.user)
      var name = obj["User info"]["name"]
      var userID = obj["User info"]["id"]
      var pwHash = obj["User info"]["pwHash"]
      var currentDate = new Date()

      this.socket.emit('text', {
        msg: JSON.stringify({ 
          room: this.chatRoom,
          userID: userID,
          name: name,
          pwHash: pwHash,
          content: this.messageText,
          time: currentDate,
        })
      });
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
  padding: 4px;
  margin-bottom: 1rem;
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
  height: 20px;
  /* background-color: #f2f2f2;
  border-top: 1px solid #e2e2e2; */
}

.chat-input input {
  flex-grow: 1;
  margin-right: 1rem;
  margin-left: 8px;
  margin-bottom: 2px;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.25rem;
}

.chat-input button {
  padding: 20px;
  border: none;
  background-color: #333;
  color: white;
  border-radius: 0.25rem;
  cursor: pointer;
}
</style>
  