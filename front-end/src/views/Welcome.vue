<template>
    <v-app>
        <v-app-bar app>
            <div class="logo">W</div>
            <div class="entry">
                <router-link to="login">Entry</router-link>
            </div>
        </v-app-bar>
        <v-content class='overlay'>
            <h1>Let's learn English with us</h1>
            <router-link to='sign-up'>
                 <v-btn outlined>Get Started</v-btn>
            </router-link>
        </v-content>
    </v-app>
</template>

<style lang="scss" scoped>

    .v-application {
        background: #000!important;
    }
    .v-content {
        background-image: url('../assets/images/bg_main.jpg');
        background-size: cover;
        align-items: center;
        text-align: center;
        .v-btn {
            color: white;
            &:active {
                transform: translateY(10px);
            }
        }
        h1 {
            color: white;
        }
    }
    .overlay {
        box-shadow: inset 2000px 0 0 0 rgba(0, 0, 0, 0.6);
    }

    .v-app-bar {
        background-color: transparent!important;
        display: flex;
        justify-content: center;
        .logo {
            width: 45px;
            height: 45px;
            border: 3px solid #fff;
            border-radius: 5px;
            justify-content: center;
            display: flex;
            align-items: center;
            font-size: 35px;
            color: #fff;
        }
        .entry a{
            color: white!important;
            margin-left: 80vw;
        }   
    }

    

</style>