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
                <v-list-item prepend-icon="mdi-home" title="Home" v-on:click="$router.push('/')"></v-list-item>
                <v-list-item prepend-icon="mdi-account-box" title="Account" v-on:click="$router.push('/account')"></v-list-item>
                <v-list-item prepend-icon="mdi-chat" title="Chat" v-on:click="$router.push('/chatPage')"></v-list-item>
                <v-list-item prepend-icon="mdi-login" title="login" v-on:click="$router.push('/login')"></v-list-item>
                <v-list-item prepend-icon="mdi-account" title="signup" v-on:click="$router.push('/signup')"></v-list-item>
                <v-list-item prepend-icon="mdi-logout" title="Logout" v-on:click="logout"></v-list-item>
            </v-list>
        </v-navigation-drawer>
    </v-layout>
    </v-card>
</template>

<script>
export default {
    mounted(){
        if (sessionStorage.getItem('isAuth') === 'true') {
            this.isLoggedIn = true;
            var obj = JSON.parse(sessionStorage.user)
            this.UserName = obj["User info"]["name"]
        }
    },
    data() {
        return {
            isLoggedIn: false,
            drawer: null,
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