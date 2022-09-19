<template>
    <div>
      <v-card id="payInput">
        <div class="sr-root">
          <div class="sr-main">
            <p> Please enter your credit card below </p>
            <p> Amount : {{amount}} CHF </p>
            <form id="payment-form" class="sr-payment-form">
            <div class="sr-combo-inputs-row">
              <input class="sr-input" type="hidden" name="card-name" id="card-name" :value="name" /> <!-- license plate number -->
              <input class="sr-input" type="hidden" name="card-id" id="card-id" :value="stripe_customer_id" />
              <input class="sr-input" type="hidden" name="card-email" id="card-email" :value="email" />
  
              <input class="sr-input" type="hidden" placeholder="Amount" name="card-pay" id="card-pay" autocomplete="off" :value=amount />
            </div>
            <br/>
            <div class="sr-combo-inputs-row">
              <div class="sr-input sr-card-element" id="card-element"></div>
            </div>
            <div class="sr-field-error" id="card-errors" role="alert" style="color: crimson;"></div>
            <button id="submit" @click.prevent="createPaymentMethod()" :disabled=btnDisabled>
              <div class="spinner hidden" id="spinner"></div>
              <span id="button-text"> Pay </span><span id="order-amount"></span>
            </button>
            </form>
            <p class="footnote"> This payment is processed by Stripe - <a href="https://stripe.com" target="_blank">stripe.com</a></p>
            <p class="footnote"><v-icon>fas fa-lock</v-icon> <span> Your credit card information is encrypted </span></p>
          </div>
        </div>
      </v-card>
    </div>
  </template>
  
  <script>
  import { mapGetters, mapActions } from 'vuex'
  // import { mapActions } from 'vuex'
  // import ApiService from '../services/api.service'
// import axios from 'axios'
  
  export default {
    name: 'paymentPage',
    props: [
    //   'amount',
    //   'name',
    ],
    data () {
      return {
        btnDisabled: false,
        stripe: '',
        elements: null,
        cardElement: null,
        email: '',
        amount: 1000,
        name: 'abc6666',
        stripe_customer_id: '',
        publicKey: '',
      }
    },
    computed: {
      ...mapGetters([
        'getPublicKey'
      ]),
    },
    mounted () {
      this.fetchPublicKey()
      console.log(this.getPublicKey)

      try {
        // this.stripe = Stripe(this.getPublicKey)
        this.publicKey = process.env.VUE_APP_STRIPE_PUBLIC_KEY

        // console.log(this.publicKey);

        /* global Stripe */
        this.stripe = Stripe(this.publicKey)
        this.elements = this.stripe.elements()

      }
      catch(IntegrationError) {
        this.$notify({ 'text': 'Stripe API issue. Please retry.' })
      }
      
      let style = {
        base: {
          color: '#32325d',
          fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
          fontSmoothing: 'antialiased',
          fontSize: '16px',
          '::placeholder': {
            color: '#aab7c4'
          }
        },
        invalid: {
          color: '#fa755a',
          iconColor: '#fa755a'
        }
      }
  
      try {
        this.cardElement = this.elements.create('card', { style: style })
        this.cardElement.mount('#card-element')
      }
      catch(IntegrationError) {
        this.$notify({ 'text': 'Stripe JS is not properly loaded. Please check your network speed and retry.' })
      }
  
    //   this.fetchUserDetails()
    },
    methods: {
      ...mapActions([
        'fetchPublicKey',
        // 'chargeAmount'
      ]),
      createPaymentMethod () {
        this.stripe.createPaymentMethod({
          type: 'card',
          card: this.cardElement,
          billing_details: {
            // Include any additional collected billing details.
            name: document.getElementById('card-name').value,
            email: document.getElementById('card-email').value
          }
        }).then(this.stripePaymentMethodHandler)
      },
      stripePaymentMethodHandler (result) {
        if (result.error) {
          this.showError(result.error.message)
        } else {
          let body = {
            payment_method_id: result.paymentMethod.id,
            amount: document.getElementById('card-pay').value,
            receipt_email: document.getElementById('card-email').value,
            customer: document.getElementById('card-id').value,
          }
          console.log(body)
          this.chargeAmount(body).then(response => {
            this.handleServerResponse(response)
          }).catch(error => {
            this.$notify({ 'text': 'Payment failed' })
            console.log(error)
          })
        }
      },
      showError (errorMsgText) {
        var errorMsg = document.querySelector('.sr-field-error')
        errorMsg.textContent = errorMsgText
        setTimeout(() => { errorMsg.textContent = '' }, 10000)
      },
      handleServerResponse (response) {
  
        if (response.data.error) {
          this.$notify({ 'text': response.data.error })
        } else if (response.requires_action) {
          this.stripe.handleCardAction(
            response.payment_intent_client_secret
          ).then(this.handleStripeJsResult)
        } else {
        //   this.orderComplete(response)
          this.orderComplete()
        }
      },
      handleStripeJsResult (result) {
        if (result.error) {
          this.showError(result.error.message)
        } else {
          let body = {
            payment_intent_id: result.paymentIntent.id,
          }
          console.log(body)
        //   this.chargeAmount(body).then((confirmResult) => {
        //     return confirmResult()
        //   }).then(this.handleServerResponse)
        }
      },
      orderComplete () {
        this.$emit('pay-done')
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
  </style>
  