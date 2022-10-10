<template>
    <v-container>
        <v-row class="text-center" style="margin-top:10%;margin-bottom:10%">
            <v-col cols="8" offset="2" class="">
                <h1 class="my-2 primary--text">Willkommen bei BetterPark</h1>
                <p class="my-7 font-weight-regular">
                    Hier können Sie bequem bis zu 24 Std nach Ihrer Ausfahrt bezahlen
                    <br>
                    Suchen Sie einfach nach Ihrem Kfz-Kennzeichen
                </p>
            </v-col>
            <v-col sm="12" md="4" offset-md="4" >
                <v-text-field class="input-field" id="licencePlate" v-model="licencePlate" placeholder="z. B. SNXY9999"  outlined height="70"></v-text-field>
                <v-btn class="white--text" depressed color="#0068c0" block x-large style="margin-top:-10px" @click="nextPage()">
                    suchen
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
    import { mapActions } from 'vuex'

    export default {
        name: 'HomePage',
         components: {
            Footer
         },
        data: () => ({
            licencePlate: '',
        }),
        // computed: {
        //     ...mapGetters([
        //         'getConfirmLicensePlate',
        //     ]),
        // },
        methods: {
            ...mapActions([
                'confirmLicensePlate',
            ]),
            nextPage() {
                if(this.licencePlate) {
                    // this.$router.push('/page1')

                    let body = {
                        licensePlate: this.licencePlate,
                    }

                    this.confirmLicensePlate(body).then(response => {
                        console.log(response)
                        // if(response == this.licencePlate)
                        {
                            this.$router.push('/page1');
                        }
                    })
                }
                else {
                    this.$notify({ 
                        'text': 'Please enter License Plate Number',
                        type: 'error',
                        duration: 10000,
                     })
                }
            }
        }
    }
</script>