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
                <v-text-field class="input-field" id="licensePlate" 
                    v-model="licensePlate" placeholder="z. B. SNXY9999" 
                    outlined height="70"
                    readonly
                ></v-text-field>
                <v-btn class="white--text" depressed color="#0068c0" block x-large style="margin-top:-10px" @click="fetchLicence">
                    Eingabe bestätigen
                </v-btn>
                <v-btn class="mt-6" text color="#0068c0" @click="homepage">
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
    import { mapActions, mapGetters } from 'vuex'

    export default {
        name: 'HomePage',
        components: {
            Footer
         },
        data () {
            return {
                licensePlate : this.getConfirmLicensePlate,
            }
        },
        computed: {
            ...mapGetters([
                'getlicensePlate',
                'getParkingFee',
                'getConfirmLicensePlate',
            ]),
        },
        mounted() {
            this.licensePlate = this.getConfirmLicensePlate
        },
        methods: {
            ...mapActions([
                'fetchLicensePlate',
            ]),
            homepage() {
                this.$router.push('/home')
            },
            fetchLicence() {
                let body = {
                    licensePlate: this.licensePlate,
                }

                this.fetchLicensePlate(body).then(response => {
                    console.log(response)
                    if(this.getParkingFee == '0')
                    {
                        this.$router.push('/page2');
                    }
                    else {
                        this.$router.push('/page3');
                    }
                })
            }
        }
    }
</script>