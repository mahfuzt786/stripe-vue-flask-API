<template>
    <v-container>
        <v-row style="margin-top:0%;margin-bottom:2%">
            <v-col sm="12" md="4" offset-md="4" class="">
                <h1 class="my-6 primary--text text-center">Bezahlung Parkvorgang</h1>
                <v-card class="mx-auto px-4 py-4" outlined>
                    <div class="mb-4 details" style="font-size:18px !important">Parkhaus, Bahnhofstr. 21, 73479 Ellwangen</div>
                    <div class="my-4 details" style="font-size:18px !important">Kennzeichen <span
                            class="font-weight-bold px-2">SBB6666</span></div>
                    <div class="my-4 details" style="font-size:18px !important">Einfahrt <span
                            class="font-weight-bold px-2">16.08.2022, 18:31 Uhr</span></div>
                    <div class="mt-4 details" style="font-size:18px !important">Parkdauer <span class="font-weight-bold px-2">1
                            Std 45 Min</span></div>
                </v-card>
                <v-card class="mx-auto px-4 py-2 my-2 text-center" outlined>
                    <div>
                        <span class="text-xl-h4 font-weight-bold price">2,45 €</span>
                    </div>
                    <div><span>Inkl. 19 % USt</span></div>
                </v-card>
            </v-col>
            <v-col sm="12" md="4" offset-md="4" class="text-center my-8">
                <v-btn class="white--text" depressed color="#0068c0" block large style="margin-top:-20px" @click="checkoutpage">
                    Jetzt bezahlen
                </v-btn>
                <v-btn class="mt-2" depressed color="#0068c0" block large outlined @click="discountpage">
                    Gutscheincode einlösen
                </v-btn>
                <v-btn class="mt-8" text color="#0068c0" @click="homepage">
                    -> zurück zur Bezahlung
                </v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
    export default {
        name: 'HomePage',
        data: () => ({

        }),
        methods: {
            homepage() {
                this.$router.push('/home')
            },
            checkoutpage() {
                this.$router.push('/page6')
            },
            discountpage() {
                this.$router.push('/page4')
            },
        }
    }
</script>