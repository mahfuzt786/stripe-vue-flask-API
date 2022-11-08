"""
appserver.py
- creates an application instance and runs the dev server
"""

if __name__ == '__main__':
    from paymentapi.application import create_app
    app = create_app()
    # app.run(host='0.0.0.0', debug=True, port=8081, ssl_context='adhoc')
    app.run(host='0.0.0.0', debug=True, port=8081)
    # app.run(host='0.0.0.0',
    #             debug=True,
    #             port=8081,
    #             ssl_context=('/home/alegra6/ssl/certs/alegralabs_com_ad91e_f7e3d_1672012799_b5711564dc077e43b4d2bafdb5a145d1.crt',
    #                 '/home/alegra6/ssl/keys/ad91e_f7e3d_0f001f3f05970f4aa7a3cc80f230cb41.key')
    #         )

    