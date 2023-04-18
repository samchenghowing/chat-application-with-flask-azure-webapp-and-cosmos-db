<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col>
          <h1>
            Chat Room {{chatRoom}}          
            <v-btn
              @click="dialog = true"
            >
              Change chat room
            </v-btn>
          </h1>

          <div class="message" v-for="message in messages" :key="message.sent">
            <v-card
              :title=message.name
              :subtitle=message.sent
              :text=message.content
            ></v-card>
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
              @click="dialog = false"
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
export default {
  mounted() {
    this.timer = setInterval(() => {
      this.getUpdate()
    }, 2000)
  },
  name: "ChatPage",
  data() {
    return {
      timer: null,
      postID: 1,
      user: "",
      messages: null,
      messageText: "",
      dialog: true,
      items: [1, 2, 3],
      chatRoom: [],
    };
  },
  methods: {
    sendMessage() {
      if (this.messageText.trim() === "") {
        return;
      }
      var obj = JSON.parse(sessionStorage.user)
      var name = obj["User info"]["name"]
      var userID = obj["User info"]["id"]
      var pwHash = obj["User info"]["pwHash"]

      var updateAPI = process.env.VUE_APP_API_URL + "/chat/send"
      fetch(updateAPI, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          postId: this.postID,
          userID: userID,
          name: name,
          pwHash: pwHash,
          content: this.messageText,
        })
      })
      .then((response) => response.json())
      .then((post) => {
        this.getUpdate()
      })
    },

    getUpdate(){
      var updateAPI = process.env.VUE_APP_API_URL + "/chat/getupdate"
      var obj = JSON.parse(sessionStorage.user)
      var name = obj["User info"]["name"]
      var userID = obj["User info"]["id"]
      var pwHash = obj["User info"]["pwHash"]
      this.postID = this.chatRoom

      fetch(updateAPI, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          postId: this.postID,
          userID: userID,
          name: name,
          pwHash: pwHash,
        })
      })
      .then((response) => response.json())
      .then((post) => {
        this.messages = post
        var obj = JSON.parse(sessionStorage.user)
        var name = obj["User info"]["name"]
        this.user = name
      })
    },
  },
  beforeDestroy() {
    clearInterval(this.timer)
  }
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
  