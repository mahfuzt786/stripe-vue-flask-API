# stripe-vue-flask-API

First, you have to deploy the backend. It is written in Python (Flask)

1) Install all required packages from 'requirements.txt'

2) Then run the backend 'python appserver.py'

3) There is a '.env' file. There you have to modify the Stripe Keys according to your account.

4) Payment API-related files are under 'paymentapi' folder.

5) In paymentapi/api.py, APIs are coded.

6) For fetch and discount some dummy data are also added there. '/Payment.fetch' and '/Payment.discount'
   Later These two definitions are to be deleted.





Secondly, in another window, you have to run the front end. It is in Vue.js.

1) Go inside 'better-park-frontend'.

2) To install the packages: npm install

3) To run the development server: npm run serve and to build for production: npm run build.

4) There is another .env file. Modify the frontend .env also according to you. Like API call URL, Running port no, etc.

5) URL Routes are defined under 'better-park-frontend/src/router/index.js'.

6) API calls are made from 'better-park-frontend/src/store/index.js'. We have used vuex to retrieve the data.

7) Later you have to change the fetch and discount API URLs in the store. that is in the 'better-park-frontend/src/store/index.js'.

