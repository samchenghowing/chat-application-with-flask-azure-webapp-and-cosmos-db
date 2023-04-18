<template>
    <v-card>
    <v-layout>
        <v-app-bar
        color="primary"
        density="compact"
        >
        <v-app-bar-nav-icon v-on:click.stop="drawer = !drawer"></v-app-bar-nav-icon>

        <v-app-bar-title>COMP3334</v-app-bar-title>

        <template v-slot:append>
            <v-btn icon="mdi-dots-vertical" v-on:click="showSetting"></v-btn>
        </template>
        </v-app-bar>

        <v-navigation-drawer
            v-model="drawer"
            temporary
        >
            <v-list-item
                prepend-icon="mdi-account"
                :title="UserName"
            ></v-list-item>
            <v-divider></v-divider>

            <v-list density="compact" nav>
                <div v-if=isLoggedIn>
                    <v-list-item prepend-icon="mdi-account-box" title="Account" v-on:click="isLoggedIn? $router.push('/account'):dialog=true"></v-list-item>
                    <v-list-item prepend-icon="mdi-chat" title="Chat" v-on:click="isLoggedIn? $router.push('/chatPage'):dialog=true"></v-list-item>
                    <v-list-item prepend-icon="mdi-logout" title="Logout" v-on:click="logout"></v-list-item>
                </div>
                <div v-else>
                    <v-list-item prepend-icon="mdi-account" title="Sign Up" v-on:click="$router.push('/signup')"></v-list-item>
                    <v-list-item prepend-icon="mdi-login" title="Login" v-on:click="$router.push('/login')"></v-list-item>
                </div>
            </v-list>
        </v-navigation-drawer>

        <div class="text-center">
            <v-dialog
            v-model="dialog"
            width="auto"
            >
            <v-card>
                <v-card-text>
                You must login to use this function.
                </v-card-text>
                <v-card-actions>
                <v-btn color="primary" block @click="dialog = false">Close Dialog</v-btn>
                </v-card-actions>
            </v-card>
            </v-dialog>
        </div>

    </v-layout>
    </v-card>
</template>

<script>
export default {
    mounted(){
        window.addEventListener('isAuth-changed', (event) => {
            this.isLoggedIn = event.detail.isAuth;
            var obj = JSON.parse(sessionStorage.user)
            this.UserName = obj["User info"]["name"]
        });
    },
    data() {
        return {
            isLoggedIn: false,
            drawer: null,
            dialog: false,
            UserName: "Guest user",
        }
    },
    methods:{
        logout(){
            sessionStorage.clear()
            this.isLoggedIn = false
            this.UserName = "Guest user"
            this.$router.push('/login')
        }
    },
}
</script>