<template>
    <v-container>
        <v-row  style="margin-top:10px">
            <v-col cols="12" class="text-center mb-0 pb-0">
                <p class="registration-number mb-0 pb-0 details">Parkvorgang: <span class="font-weight-bold">SB 666666</span></p>
                <h1 class="my-2 primary--text">2,45 €</h1>
            </v-col>
            <v-col sm="12" md="4" offset-md="4" class="mt-0 pt-0">
                <label style=" color:#595959 !important;">E-Mail</label>
                <v-text-field class="input" value=""  outlined></v-text-field>
                <label style=" color:#595959 !important;">Zahlungsmethode</label>
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

                </v-chip-group>
                <label style=" color:#595959 !important;">Kartendaten</label>
                <v-text-field class="input-field1 input" type="text" outlined placeholder="1111 1111 1111 1111"
                style="margin-bottom:-25px !important;">
                    <template v-slot:append>
                        <v-img  height="24" v-bind:src="require('../assets/card.png')" style="width:150px !important"/>
                    </template>
                </v-text-field>
                <v-row>
                    <v-col cols="6">
                        <v-text-field class="input" value="" placeholder="MM/JJ" outlined></v-text-field>
                    </v-col>
                    <v-col cols="6">
                        <v-text-field class="input" placeholder="CVC" type="text" outlined>
                            <template v-slot:append>
                                <v-img width="100%" height="24" :src="require('../assets/cvv.png')" />
                            </template>
                        </v-text-field>
                    </v-col>
                </v-row>
                <label style=" color:#595959 !important;">Name des Karteninhabers</label>
                <v-text-field class="input" value="" outlined></v-text-field>
                <label style=" color:#595959 !important;">Land oder Region</label>
                <v-select class="input" :items="region" label="Land oder Region" outlined></v-select>
            </v-col>
             <v-col class="text-center" cols="12">
               <Footer style="margin-top:-55px !important"/>
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
       data: function () {
            return {
                region: ['Deutschland'],
            }
        }
        


    }
</script>

<style>
    .registration-number {
        font-size: 1.5rem;
    }
    .input-field1{
        margin-bottom:-15px !important;
    }
</style>