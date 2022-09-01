<template>
    <v-container>
        <v-row class="text-center" style="margin-top:10%;margin-bottom:8%">
            <v-col cols="8" offset="2" class="" align="center">
                <h1 class="my-2">Zahlung erfolgreich</h1>
                <v-img class="my-6" :src="icon" style="width:10%;" />
            </v-col>
            <v-col cols="4" offset="4" class="">
                <v-text-field class="input-field" value="z. B. SNXY9999" outlined height="70"></v-text-field>
                <v-btn class="mt-4" text color="#0068c0">
                    -> zur Startseite
                </v-btn>
            </v-col>
            <v-col cols="12">
               <Footer />
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
    import Footer from './footer.vue';
    import icon from "@/assets/tick.png";
    export default {
        name: 'HomePage',
         components: {
            Footer
         },
       data: function () {
            return {
                icon: icon
            }
        }
    }
</script>