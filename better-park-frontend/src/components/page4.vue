<template>
    <v-container>
        <v-row class="text-center" style="margin-top:10%;margin-bottom:10%">
            <v-col sm="12" md="4" offset-md="4" class="">
                <h1 class="my-2 primary--text">Bitte Gutscheincode eingeben</h1>
            </v-col>
            <v-col sm="12" md="4" offset-md="4" class="">
                <v-text-field class="input-field" placeholder="XXX-XXX" outlined height="70"></v-text-field>
                <v-btn class="white--text " depressed color="#0068c0" block large style="margin-top:-20px">
                    Eingabe bestätigen
                </v-btn>
                <v-btn class="mt-6" text color="#0068c0" @click="homepage">
                    -> zurück zur Bezahlung
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
    export default {
        name: 'HomePage',
        components: {
            Footer
         },
        data: () => ({}),
        methods: {
            homepage() {
                this.$router.push('/page3')
            }
        }
    }
</script>