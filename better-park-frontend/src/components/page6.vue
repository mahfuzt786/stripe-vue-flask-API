<template>
    <v-container>
        <v-row style="margin-top:10px">
            <v-col cols="12" class="text-center mb-0 pb-0" id="parkingLicense">
                <p class="registration-number mb-0 pb-0 details">Parkvorgang: <span class="font-weight-bold">
                        {{ $store.state.licensePlate }}</span></p>
                <h1 class="my-2 primary--text"> {{ amount }} €</h1>
            </v-col>
            <v-col sm="12" md="8" offset-md="2" class="mt-0 pt-0">
                <!-- <v-form id="payment-form" class="sr-payment-form form-group">
                    <input class="sr-input" type="hidden" name="licencePlateNumber" id="licencePlateNumber"
                        :value=licencePlateNumber />
                    <input class="sr-input" type="hidden" placeholder="Amount" name="card-pay" id="card-pay"
                        autocomplete="off" :value=amount />

                    <label style=" color:#595959 !important;">E-Mail</label>
                    <v-text-field class="input" name="card-email" id="card-email" value="test@email.in" outlined></v-text-field>

                    <label style=" color:#595959 !important;">Zahlungsmethode</label>
                    <v-chip-group class="mb-2" active-class="deep-purple accent-4 white--text" column
                        v-model="paymentOption" @change="onChange()">
                        <v-chip class="ma-1 py-8 px-1" label>
                            <v-img width="75" height="50" :src="require('../assets/1.png')" />
                        </v-chip>
                        <v-chip class="ma-1 py-8 px-1" label>
                            <v-img width="75" height="50" :src="require('../assets/2.png')" />
                        </v-chip>
                        <v-chip class="ma-1 py-8 px-1" label>
                            <v-img width="75" height="50" :src="require('../assets/3.png')" />
                        </v-chip>
                        <v-chip class="ma-1 py-8 px-1" label>
                            <v-img width="75" height="50" :src="require('../assets/4.png')" />
                        </v-chip>

                    </v-chip-group>
                    <v-row v-if="this.paymentOption == 0">
                        <v-col cols="12">
                            <label style=" color:#595959 !important;">Name des Karteninhabers</label>
                            <v-text-field class="input" placeholder="Name des Karteninhabers" type="text" outlined></v-text-field>
                        
                            <label style=" color:#595959 !important;">Kartendaten</label>
                            <v-text-field class="input-field1 input form-control" name="card-number" id="card-number"
                                outlined placeholder="1111 1111 1111 1111" style="margin-bottom:-25px !important;"
                                v-cardformat:formatCardNumber>

                                
                            </v-text-field>
                        </v-col>
                        <v-col cols="6">
                            <v-text-field class="input" name="card-expiry" id="card-expiry" placeholder="MM/JJ" outlined
                                v-cardformat:formatCardExpiry>
                            </v-text-field>
                        </v-col>
                        <v-col cols="6">
                            <v-text-field class="input" name="card-cvc" id="card-cvc" placeholder="CVC" type="text"
                                outlined v-cardformat:formatCardCVC>
                                <template v-slot:append>
                                    <v-img width="100%" height="24" :src="require('../assets/cvv.png')" />
                                </template>
                            </v-text-field>
                        </v-col>
                    </v-row>

                    <v-row v-if="this.paymentOption == 2">
                        <v-col cols="12">
                            <label style=" color:#595959 !important;">Name</label>
                            <v-text-field class="input" placeholder="Name" type="text" outlined></v-text-field>

                            <label style=" color:#595959 !important;">IBAN</label>
                            <v-text-field class="input-field1 input form-control" name="" id="" outlined
                                placeholder="DE00 0000 0000 0000 0000 00" style="margin-bottom:-25px !important;">
                            </v-text-field>
                        </v-col>
                        <! -- <v-col cols="6" class="my-0 py-0">
                            <label style=" color:#595959 !important;">Name</label>
                            <v-text-field class="input" name="" id="" value="" outlined>
                            </v-text-field>
                        </v-col>
                        <v-col cols="6" class="my-0 py-0">
                            <label style=" color:#595959 !important;">E-Mail</label>
                            <v-text-field class="input" name="" id="" value="" outlined>
                            </v-text-field>
                        </v-col> - ->
                        <v-col cols="12" class="mt-0 pt-0">
                            <p class="text-justify" style="font-size:0.8em !important; color: maroon !important;">
                                Durch Angabe Ihrer Zahlungsinformationen und der Bestätigung der vorliegenden Zahlung ermächtigen Sie (A) 
                                BetterPark und Stripe, unseren Zahlungsdienstleister, bzw. PPRO, den lokalen Bankdienstleister von Stripe, 
                                Ihrem Kreditinstitut Anweisungen zur Belastung Ihres Kontos zu erteilen, und (B) Ihr Kreditinstitut, Ihr Konto 
                                gemäß diesen Anweisungen zu belasten. Im Rahmen Ihrer Rechte haben Sie, entsprechend den Vertragsbedingungen mit 
                                Ihrem Kreditinstitut, Anspruch auf eine Rückerstattung von Ihrem Kreditinstitut. Eine Rückerstattung muss innerhalb 
                                von 8 Wochen ab dem Tag, an dem Ihr Konto belastet wurde, geltend gemacht werden. Eine Erläuterung Ihrer Rechte 
                                können Sie von Ihrem Kreditinstitut anfordern. Sie erklären sich einverstanden, Benachrichtigungen über künftige 
                                Belastungen bis spätestens 2 Tage vor dem Buchungsdatum zu erhalten.
                            </p>
                        </v-col>
                    </v-row>

                    <label style=" color:#595959 !important;">Land oder Region</label>
                    <v-select class="input" :items="region" label="Land oder Region" outlined></v-select>

                    <div class="sr-field-error" id="card-errors" role="alert"
                        style="color: crimson; font-size: large; font-weight: bold;">
                        {{ errorMessage }}
                    </div>

                    <v-col sm="12" md="4" offset-md="4" class="">
                        <v-btn class="white--text" large dark color="indigo" @click="checkoutBetterParks()">
                            <v-icon dark>
                                mdi-plus
                            </v-icon> Pay
                        </v-btn>
                    </v-col>
                </v-form> -->

                <!-- Display a payment form -->
                <form id="payment-form">
                    <input class="sr-input" type="hidden" name="licencePlateNumber" id="licencePlateNumber"
                        :value=licencePlateNumber />
                    <input class="sr-input" type="hidden" placeholder="Amount" name="card-pay" id="card-pay"
                        autocomplete="off" :value=amount />

                    <div id="payment-element">
                        <!--Stripe.js injects the Payment Element-->
                    </div>
                    <button class="payBtn" id="submit">
                        <div class="spinner hidden" id="spinner"></div>
                        <span id="button-text">Pay now</span>
                    </button>
                    <div id="payment-message" class="hidden"></div>
                </form>
            </v-col>
            <v-col class="text-center" cols="12">
                <Footer style="margin-top:-55px !important" />
            </v-col>
        </v-row>

        <v-overlay :value="overlay">
            <v-progress-circular indeterminate size="64"></v-progress-circular>
        </v-overlay>

    </v-container>
</template>
<script>
    import Footer from './footer.vue'
    // import axios from 'axios'
    import {
        mapGetters,
        mapActions
    } from 'vuex'


    export default {
        name: 'checkoutBetterPark',
        components: {
            Footer
        },
        data: function () {
            return {
                region: ['Deutschland'],
                stripe: '',
                btnDisabled: false,
                errorMessage: '',
                overlay: false,
                paymentOption: 0,

                elementsF: null,
                clientSecretF: null,
            }
        },
        watch: {

        },
        computed: {
            ...mapGetters([
                'getPublicKey',
            ]),
            licencePlateNumber() {
                return this.$store.state.licensePlate
            },
            amount() {
                // return 50
                if (this.$store.state.parkingFeeDiscount == '')
                    return this.$store.state.parkingFee
                else
                    return this.$store.state.parkingFeeDiscount
            },
        },
        mounted() {
            this.fetchPublicKey()

            try {
                /* global Stripe */
                // this.stripe = Stripe(this.getPublicKey)
                // console.log(this.$store.state.publicKey)
                console.log(this.getPublicKey)
                this.stripe = Stripe(this.$store.state.publicKey)
                // this.elements = this.stripe.elements()
            } catch (IntegrationError) {
                this.$notify({
                    'text': 'Stripe API issue. Please reload.'
                })
            }

            this.initialize();
            this.checkStatus();

            document
            .querySelector("#payment-form")
            .addEventListener("submit", this.handleSubmit);
        },
        methods: {
            ...mapActions([
                'fetchPublicKey',
                'chargeAmount',
                'createPaymentIntent',
            ]),
            homepage() {
                this.$router.push('/home')
            },
            setShow() {
                // setTimeout(() => this.errorMessage = '', 200000);
                // setTimeout(() => {
                //     this.errorMessage = '';
                // }, 2000);
            },
            // Fetches a payment intent and captures the client secret
            async initialize() {
                let body = {
                        card_amount: document.getElementById('card-pay').value,
                        card_name: document.getElementById('licencePlateNumber').value,
                    }

                this.createPaymentIntent(body).then(response => {
                    console.log(response);

                    this.clientSecretF = response.data.clientSecret;

                    const appearance = {
                        theme: 'stripe',
                    };

                    const clientSecret = this.clientSecretF
                    this.elementsF = this.stripe.elements({ appearance, clientSecret });

                    const paymentElement = this.elementsF.create("payment");
                    paymentElement.mount("#payment-element");

                }).catch(error => {
                    this.$notify({
                        'text': 'Payment failed' + error
                    })
                })
            },
            async handleSubmit(e) {
                e.preventDefault();
                this.setLoading(true);

                const elements = this.elementsF

                const { error } = await this.stripe.confirmPayment({
                    elements,
                    confirmParams: {
                    // Make sure to change this to your payment completion page
                        // return_url: 'http://localhost:8080/#/page7'
                        return_url: 'https://www.alegralabs.com/syed/park-stripe/better-park-frontend/dist/#/page7'
                    },
                });

                // This point will only be reached if there is an immediate error when
                // confirming the payment. Otherwise, your customer will be redirected to
                // your `return_url`. For some payment methods like iDEAL, your customer will
                // be redirected to an intermediate site first to authorize the payment, then
                // redirected to the `return_url`.
                if (error.type === "card_error" || error.type === "validation_error") {
                    this.showMessage(error.message);
                } else {
                    this.showMessage("An unexpected error occurred.");
                }

                this.setLoading(false);
            },
            // Fetches the payment intent status after payment submission
            async checkStatus() {
                const clientSecret = new URLSearchParams(window.location.search).get(
                    "payment_intent_client_secret"
                );

                if (!this.clientSecret) {
                    return;
                }

                const { paymentIntent } = await this.stripe.retrievePaymentIntent(clientSecret);

                switch (paymentIntent.status) {
                    case "succeeded":
                        this.showMessage("Payment succeeded!");
                        break;
                    case "processing":
                        this.showMessage("Your payment is processing.");
                        break;
                    case "requires_payment_method":
                        this.showMessage("Your payment was not successful, please try again.");
                        break;
                    default:
                        this.showMessage("Something went wrong.");
                        break;
                }
            },
            // ------- UI helpers --------
            showMessage(messageText) {
                const messageContainer = document.querySelector("#payment-message");

                messageContainer.classList.remove("hidden");
                messageContainer.textContent = messageText;

                setTimeout(function () {
                    messageContainer.classList.add("hidden");
                    messageText.textContent = "";
                }, 4000);
            },
            // Show a spinner on payment submission
            setLoading(isLoading) {
                if (isLoading) {
                    // Disable the button and show a spinner
                    document.querySelector("#submit").disabled = true;
                    document.querySelector("#spinner").classList.remove("hidden");
                    document.querySelector("#button-text").classList.add("hidden");
                } else {
                    document.querySelector("#submit").disabled = false;
                    document.querySelector("#spinner").classList.add("hidden");
                    document.querySelector("#button-text").classList.remove("hidden");
                }
            },

            checkoutBetterParks() {
                // if (document.getElementById('card-email').value == '') {
                //     this.errorMessage = 'Email id is required'
                //     this.setShow();
                // } else if (document.getElementById('card-pay').value == '') {
                //     this.errorMessage = 'Amount is invalid'
                //     this.setShow();
                // } else if (document.getElementById('licencePlateNumber').value == '') {
                //     this.errorMessage = 'licence Plate Number is invalid'
                //     this.setShow();
                // } else if (document.getElementById('card-number').value == '') {
                //     this.errorMessage = 'card number is required'
                //     this.setShow();
                // } else if (document.getElementById('card-expiry').value == '') {
                //     this.errorMessage = 'card expiry is required'
                //     this.setShow();
                // } else if (document.getElementById('card-cvc').value == '') {
                //     this.errorMessage = 'card cvc is required'
                //     this.setShow();
                // } else 
                {
                    this.overlay = true

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
                        this.$notify({
                            'text': 'Payment failed' + error
                        })
                    })
                }
            },
            handleServerResponse(response) {
                if (response.data.error) {
                    this.$notify({
                        'text': response.data.error
                    })
                } else if (response.data.requires_action) {
                    console.log(response)
                    // this.stripe.handleCardAction(
                    //     response.data.payment_intent_client_secret
                    // ).then(this.handleStripeJsResult)

                    this.stripe.confirmGiropayPayment(
                        response.data.payment_intent_client_secret,
                        {
                            payment_method: {
                                billing_details: {
                                    name: "Alegra Labs"
                                }
                            },
                            return_url: 'https://example.com/checkout/complete',
                        }
                    ).then(this.handleStripeJsResult)

                    // stripe.confirmSofortPayment(
                    //     '{{PAYMENT_INTENT_CLIENT_SECRET}}',
                    //     {
                    //         payment_method: {
                    //             sofort: {
                    //                 country: "DE"
                    //             }
                    //         },
                    //         return_url: 'https://example.com/checkout/complete',
                    //     }
                    // );

                } else {
                    this.orderComplete(response)
                }
            },
            handleStripeJsResult(result) {
                console.log(result)
                if (result.error) {
                    this.showError(result.error.message)
                } else {
                    let body = {
                        payment_intent_id: result.paymentIntent.id,
                        card_name: document.getElementById('licencePlateNumber').value,
                    }
                    this.chargeAmount(body).then(confirmResult => {
                        this.overlay = false

                        this.orderComplete(confirmResult)

                    }); //.then(this.handleServerResponse)
                }
            },
            orderComplete(response) {
                if (response.data.success == true) {
                    this.$notify('bezahlt für ' + response.data.licence_plate_number)
                    // this.$router.push('/page7')

                    setTimeout(() => {
                        this.$router.push('/page7')
                    }, 4000);
                }
            },
            onChange() {
                // if (this.paymentOption == 0) {
                //     console.log();
                // }
                // else if(this.paymentOption == 1){

                // }
                // else if(this.paymentOption == 2){

                // }
                // else if(this.paymentOption == 3){

                // }

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

    .input-field1 {
        margin-bottom: -15px !important;
    }



    /* Variables */
    * {
    box-sizing: border-box;
    }

// body {
//   font-family: -apple-system, BlinkMacSystemFont, sans-serif;
//   font-size: 16px;
//   -webkit-font-smoothing: antialiased;
//   display: flex;
//   justify-content: center;
//   align-content: center;
//   height: 100vh;
//   width: 100vw;
// }

// form {
//   width: 30vw;
//   min-width: 500px;
//   align-self: center;
//   box-shadow: 0px 0px 0px 0.5px rgba(50, 50, 93, 0.1),
//     0px 2px 5px 0px rgba(50, 50, 93, 0.1), 0px 1px 1.5px 0px rgba(0, 0, 0, 0.07);
//   border-radius: 7px;
//   padding: 40px;
// }

.hidden {
  display: none;
}

#payment-message {
  color: rgb(105, 115, 134);
  font-size: 16px;
  line-height: 20px;
  padding-top: 12px;
  text-align: center;
}

#payment-element {
  margin-bottom: 24px;
}

/* Buttons and links */
button.payBtn {
  background: #5469d4;
  font-family: Arial, sans-serif;
  color: #ffffff;
  border-radius: 4px;
  border: 0;
  padding: 12px 16px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  display: block;
  transition: all 0.2s ease;
  box-shadow: 0px 4px 5.5px 0px rgba(0, 0, 0, 0.07);
  width: 100%;
}

button:hover {
  filter: contrast(115%);
}
button:disabled {
  opacity: 0.5;
  cursor: default;
}

/* spinner/processing state, errors */
.spinner,
.spinner:before,
.spinner:after {
  border-radius: 50%;
}
.spinner {
  color: #ffffff;
  font-size: 22px;
  text-indent: -99999px;
  margin: 0px auto;
  position: relative;
  width: 20px;
  height: 20px;
  box-shadow: inset 0 0 0 2px;
  -webkit-transform: translateZ(0);
  -ms-transform: translateZ(0);
  transform: translateZ(0);
}
.spinner:before,
.spinner:after {
  position: absolute;
  content: "";
}
.spinner:before {
  width: 10.4px;
  height: 20.4px;
  background: #5469d4;
  border-radius: 20.4px 0 0 20.4px;
  top: -0.2px;
  left: -0.2px;
  -webkit-transform-origin: 10.4px 10.2px;
  transform-origin: 10.4px 10.2px;
  -webkit-animation: loading 2s infinite ease 1.5s;
  animation: loading 2s infinite ease 1.5s;
}
.spinner:after {
  width: 10.4px;
  height: 10.2px;
  background: #5469d4;
  border-radius: 0 10.2px 10.2px 0;
  top: -0.1px;
  left: 10.2px;
  -webkit-transform-origin: 0px 10.2px;
  transform-origin: 0px 10.2px;
  -webkit-animation: loading 2s infinite ease;
  animation: loading 2s infinite ease;
}

@-webkit-keyframes loading {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes loading {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@media only screen and (max-width: 600px) {
  form {
    width: 80vw;
    min-width: initial;
  }
}
</style>