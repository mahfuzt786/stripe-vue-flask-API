<template>
    <v-container>
        <v-row  style="margin-top:10px">
            <v-col cols="12" class="text-center mb-0 pb-0">
                <p class="registration-number mb-0 pb-0 details">Parkvorgang: <span class="font-weight-bold"> {{ $store.state.licensePlate }}</span></p>
                <h1 class="my-2 primary--text"> {{ amount }} €</h1>
            </v-col>
            <v-col sm="12" md="4" offset-md="4" class="mt-0 pt-0">
                <v-form
                id="payment-form" class="sr-payment-form form-group"
                >
                <!-- <input class="sr-input" type="hidden" name="licencePlateNumber" id="licencePlateNumber" value={{ $store.state.licensePlate }} /> -->
                    <input class="sr-input" type="hidden" name="licencePlateNumber" id="licencePlateNumber" :value=licencePlateNumber />
                    <input class="sr-input" type="hidden" placeholder="Amount" name="card-pay" id="card-pay" autocomplete="off" :value=amount />
                    <!-- <input class="sr-input" type="hidden" placeholder="Amount" name="card-pay" id="card-pay" autocomplete="off" value={{ $store.state.parkingFee }} /> -->

                    <label style=" color:#595959 !important;">E-Mail</label>
                    <v-text-field class="input" name="card-email" id="card-email" value="" outlined></v-text-field>

                    <!-- <label style=" color:#595959 !important;">Zahlungsmethode</label>
                    <v-chip-group class="mb-2" active-class="deep-purple accent-4 white--text" column >
                        <v-chip  class="ma-1 py-8 px-1" label>
                            <v-img width="75" height="50" :src="require('../assets/1.png')" />
                        </v-chip>
                        <v-chip  class="ma-1 py-8 px-1" label>
                            <v-img width="75" height="50" :src="require('../assets/2.png')" />
                        </v-chip>
                        <v-chip  class="ma-1 py-8 px-1" label>
                            <v-img width="75" height="50" :src="require('../assets/3.png')" />
                        </v-chip>
                        <v-chip  class="ma-1 py-8 px-1" label>
                            <v-img width="75" height="50" :src="require('../assets/4.png')" />
                        </v-chip>

                    </v-chip-group> -->
                    <label style=" color:#595959 !important;">Kartendaten</label>                    
                    <v-text-field class="input-field1 input form-control"
                        name="card-number" id="card-number" 
                        outlined 
                        placeholder="1111 1111 1111 1111"
                        style="margin-bottom:-25px !important;"
                        
                        v-cardformat:formatCardNumber
                    >
                        
                        <!-- <template v-slot:append>
                            <v-img  height="24" v-bind:src="require('../assets/card.png')" style="width:150px !important"/>
                        </template> -->
                    </v-text-field>
                    <v-row>
                        <v-col cols="6">
                            <v-text-field class="input" 
                                name="card-expiry" id="card-expiry" 
                                placeholder="MM/JJ" outlined
                                v-cardformat:formatCardExpiry
                            >
                            </v-text-field>
                        </v-col>
                        <v-col cols="6">
                            <v-text-field class="input" 
                                name="card-cvc" id="card-cvc" 
                                placeholder="CVC" type="text" 
                                outlined
                                v-cardformat:formatCardCVC
                            >
                                <template v-slot:append>
                                    <v-img width="100%" height="24" :src="require('../assets/cvv.png')" />
                                </template>
                            </v-text-field>
                        </v-col>
                    </v-row>
                    <label style=" color:#595959 !important;">Name des Karteninhabers</label>
                    <v-text-field class="input" value="card-name" outlined></v-text-field>
                    <label style=" color:#595959 !important;">Land oder Region</label>
                    <v-select class="input" :items="region" label="Land oder Region" outlined></v-select>

                    <div class="sr-field-error" 
                        id="card-errors" 
                        role="alert" 
                        style="color: crimson; font-size: large; font-weight: bold;"
                    >
                        {{ errorMessage }}
                    </div>

                    <v-col sm="12" md="4" offset-md="4" class="">
                        <v-btn
                            class="white--text"
                            large
                            dark
                            color="indigo" @click="checkoutBetterParks()"
                        >
                            <v-icon dark>
                                mdi-plus
                            </v-icon> Pay
                        </v-btn>
                    </v-col>
                </v-form>
            </v-col>
             <v-col class="text-center" cols="12">
               <Footer style="margin-top:-55px !important"/>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
    import Footer from './footer.vue'
    // import axios from 'axios'
    import { mapGetters, mapActions } from 'vuex'


    export default {
       name: 'checkoutBetterPark',
        components: {
            Footer
        },
       data: function () {
            return {
                // amount: 210,
                // licencePlateNumber: 'asd1234',
                region: ['Deutschland'],
                stripe: '',
                btnDisabled: false,
                errorMessage: '',
            }
        },
        watch: {
            
        },
        computed: {
            ...mapGetters([
                'getPublicKey',
                // 'getlicensePlate',
                // 'getParkingFee',
            ]),
            licencePlateNumber() 
            { 
                return this.$store.state.licensePlate 
            },
            amount() 
            {
                if(this.$store.state.parkingFeeDiscount == '') 
                    return this.$store.state.parkingFee
                else
                    return this.$store.state.parkingFeeDiscount
            },
        },
        mounted () {
            this.fetchPublicKey()

            try {
                /* global Stripe */
                this.stripe = Stripe(this.getPublicKey)
                // this.elements = this.stripe.elements()
            }
            catch(IntegrationError) {
                this.$notify({ 'text': 'Stripe API issue. Please retry.' })
            }
        },
        methods: {
            ...mapActions([
                'fetchPublicKey',
                'chargeAmount'
            ]),
            homepage() {
                this.$router.push('/home')
            },
            setShow() {
                setTimeout(() => this.errorMessage = '', 2000);
                // setTimeout(() => {
                //     this.errorMessage = '';
                // }, 2000);
            },
            checkoutBetterParks() {
                if(document.getElementById('card-email').value == '') {
                    this.errorMessage = 'Email id is required'
                    this.setShow();
                }
                else if(document.getElementById('card-pay').value == '') {
                    this.errorMessage = 'Amount is invalid'
                    this.setShow();
                }
                else if(document.getElementById('licencePlateNumber').value == '') {
                    this.errorMessage = 'licence Plate Number is invalid'
                    this.setShow();
                }
                else if(document.getElementById('card-number').value == '') {
                    this.errorMessage = 'card number is required'
                    this.setShow();
                }
                else if(document.getElementById('card-expiry').value == '') {
                    this.errorMessage = 'card expiry is required'
                    this.setShow();
                }
                else if(document.getElementById('card-cvc').value == '') {
                    this.errorMessage = 'card cvc is required'
                    this.setShow();
                }
                else {
                    let body = {
                        card_amount: document.getElementById('card-pay').value,
                        card_email: document.getElementById('card-email').value,
                        card_name: document.getElementById('licencePlateNumber').value,
                        card_number: document.getElementById('card-number').value,
                        card_expiry: document.getElementById('card-expiry').value,
                        card_cvc: document.getElementById('card-cvc').value
                    }

                    this.chargeAmount(body).then(response => {
                        this.handleServerResponse(response)
                    }).catch(error => {
                        this.$notify({ 'text': 'Payment failed' + error })
                    })
                }
            },
            handleServerResponse (response) {
                if (response.data.error) {
                    this.$notify({ 'text': response.data.error })
                } else if (response.data.requires_action) {
                    console.log(response)
                    this.stripe.handleCardAction(
                        response.data.payment_intent_client_secret
                    ).then(this.handleStripeJsResult)
                } else {
                  this.orderComplete(response)
                    // this.orderComplete()
                    console.log(response)
                }
            },
            handleStripeJsResult (result) {
                if (result.error) {
                    this.showError(result.error.message)
                } else {
                    let body = {
                        payment_intent_id: result.paymentIntent.id,
                    }
                  this.chargeAmount(body).then(confirmResult => {
                    console.log(confirmResult)

                    // return confirmResult
                  }).then(this.handleServerResponse)
                }
            },
            orderComplete (response) {
                this.$notify('pay-done'+ response)
            }
        }
    }
</script>

<style lang="scss">
    @import '../assets/scss/payment-stripe.scss';
  
    #payInput {
      padding-top: 0;
    
      .footnote {
        color: gray;
        text-align: center;
      }
    }
    .registration-number {
        font-size: 1.5rem;
    }
    .input-field1{
        margin-bottom:-15px !important;
    }
</style>