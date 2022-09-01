<template>
    <v-container>
        <v-row class="text-center" style="margin-top:4%;margin-bottom:2%">
            <v-col sm="12" md="4" offset-md="4" class="">
                <h1 class="my-2 primary--text text-center">Bezahlung Parkvorgang</h1>
                <v-card class="mx-auto px-4 py-4" outlined>
                    <div class="mb-4 details">Parkhaus, Bahnhofstr. 21, 73479 Ellwangen</div>
                    <div class="my-4 details">Kennzeichen <span class="font-weight-bold px-2">SBB6666</span></div>
                    <div class="my-4 details">Einfahrt <span class="font-weight-bold px-2">16.08.2022, 18:31 Uhr</span></div>
                    <div class="mt-4 details">Parkdauer <span class="font-weight-bold px-2">1 Std 45 Min</span></div>
                </v-card>
                <v-card class="mx-auto px-4 py-2 my-2 text-center" outlined>
                    <div>
                        <span class="text-decoration-line-through text-xl-h4 px-4 price">2,45 €</span>
                        <span class="text-xl-h4 font-weight-bold price">2,45 €</span>
                    </div>
                    <div><span>Inkl. 19 % USt</span></div>
                </v-card>
                <p class="pt-3 pb-0 mb-3 green--text">Gutscheincode gültig</p>
            </v-col>
            <v-col sm="12" md="4" offset-md="4" class="text-center">
                <v-btn class="white--text" depressed color="#0068c0" block large style="margin-top:-20px">
                    Jetzt bezahlen
                </v-btn>
                <v-btn class="mt-2" depressed color="#0068c0" block large outlined>
                    Gutscheincode einlösen
                </v-btn>
                <v-btn class="mt-8" text color="#0068c0">
                    -> zurück zur Bezahlung
                </v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
    export default {
        name: 'HomePage',

        data: () => ({}),
    }
</script>

<style>
    .price {
        font-size: 2rem;
    }
</style>