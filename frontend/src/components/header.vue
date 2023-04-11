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
            <v-btn icon="mdi-dots-vertical"></v-btn>
        </template>
        </v-app-bar>

        <v-navigation-drawer
            v-model="drawer"
            temporary
        >
            <v-list-item
                prepend-icon="mdi-account"
                title="Guest user"
            ></v-list-item>
            <v-divider></v-divider>

            <v-list density="compact" nav>
                <v-list-item prepend-icon="mdi-home" title="Home" v-on:click="$router.push('/')"></v-list-item>
                <v-list-item v-if="isLoggedIn" prepend-icon="mdi-account-box" title="Account" v-on:click="$router.push('/account')"></v-list-item>
                <v-list-item v-if="isLoggedIn" prepend-icon="mdi-chat" title="Chat" v-on:click="$router.push('/chatPage')"></v-list-item>
                <v-list-item v-if="!isLoggedIn" prepend-icon="mdi-login" title="login" v-on:click="$router.push('/login')"></v-list-item>
                <v-list-item v-if="!isLoggedIn" prepend-icon="mdi-account" title="signup" v-on:click="$router.push('/signup')"></v-list-item>
                <v-list-item v-if="isLoggedIn" prepend-icon="mdi-logout" title="Logout" v-on:click="logout"></v-list-item>
            </v-list>
        </v-navigation-drawer>
    </v-layout>
    </v-card>
</template>

<script>
export default {
    data() {
        return {
            isLoggedIn: false,
            drawer: null,
            UserName: "Guest user",
        }
    },
    created() {
        if (sessionStorage.getItem('isAuth') === 'true') {
            this.isLoggedIn = true;
        }
    },
    methods:{
        logout(){
            sessionStorage.clear();
            this.$router.push('/login');
        }
    },
}
</script>