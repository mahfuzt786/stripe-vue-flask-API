<template>
    <v-container>
        <v-row class="text-center" style="margin-top:10%;margin-bottom:8%">
            <v-col cols="8" offset="2" class="">
                <h1 class="my-2">Ist Ihr Kfz-Kennzeichen richtig?</h1>
                <p class="my-7">
                    Bitte bestätigen Sie Ihre Eingabe
                </p>
            </v-col>
            <v-col sm="12" md="4" offset-md="4">
                <v-text-field class="input-field" placeholder="z. B. SNXY9999"  outlined height="70"></v-text-field>
                <v-btn class="white--text" depressed color="#0068c0" block x-large style="margin-top:-10px">
                    Eingabe bestätigen
                </v-btn>
                <v-btn class="mt-6" text color="#0068c0">
                    -> zurück zur Startseite
                </v-btn>
            </v-col>
            <v-col cols="12">
               <Footer />
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
    import Footer from './footer.vue'
    export default {
        name: 'HomePage',
         components: {
            Footer
         },
        data: () => ({

        }),
    }
</script>