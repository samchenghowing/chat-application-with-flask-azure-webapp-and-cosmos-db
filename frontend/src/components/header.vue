<template>
    <v-card>
    <v-layout>
        <v-app-bar
        color="primary"
        density="compact"
    >
        <template v-slot:prepend>
        <v-menu>
            <template v-slot:activator="{ props }">
            <v-app-bar-nav-icon v-bind="props"></v-app-bar-nav-icon>
            </template>
            <v-list color="transparent">
            <v-list-item prepend-icon="mdi-home" title="Home" v-on:click="$router.push('/')"></v-list-item>
            <v-list-item prepend-icon="mdi-account-box" title="Account" v-on:click="$router.push('/account')"></v-list-item>
            <v-list-item prepend-icon="mdi-chat" title="Chat" v-on:click="$router.push('/chatPage')"></v-list-item>
            </v-list>
        </v-menu>
        </template>

        <v-app-bar-title>COMP3334</v-app-bar-title>

        <template v-slot:append>
            <v-btn icon="mdi-dots-vertical"></v-btn>
        </template>
        </v-app-bar>
    </v-layout>
    </v-card>
</template>
