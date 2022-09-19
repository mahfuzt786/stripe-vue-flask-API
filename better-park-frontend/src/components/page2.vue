<template>
    <v-container>
        <v-row class="text-center" style="margin-top:10%;margin-bottom:8%">
            <v-col cols="8" offset="2" class="" align="center">
                <h1 class="my-2">Sie müssen nicht bezahlen</h1>
                <p class="my-7">
                    Zur Ihrem Kfz-Kennzeichen sind keine Parkgebühren offen
                </p>
                <v-img :src="icon" style="width:10%;margin-top:-22px !important" />
            </v-col>
            <v-col sm="12" md="4" offset-md="4">
                <v-text-field class="input-field" placeholder="z. B. SNXY9999" outlined height="70"></v-text-field>
                <v-btn class="mt-4" text color="#0068c0" @click="homepage">
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
        },
        methods: {
            homepage() {
                this.$router.push('/home')
            }
        }
    }
</script>