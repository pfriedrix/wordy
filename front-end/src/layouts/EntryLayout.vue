<template>
    <v-app>
        <v-content>
            <div class="form">
                <router-view/>
            </div>
        </v-content>
    </v-app>
</template>

<style lang="scss" scoped>
    .v-content {
        display: flex;
        align-items: center;
        justify-content: center;
        .form {
            display: flex;
            justify-content: center;
        }
    }
    
</style>