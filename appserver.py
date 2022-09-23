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
    #             ssl_context=('/home/alegra6/ssl/certs/alegralabs_com_c32c2_e8937_1664927999_3e576c3f7d117d5b1a1b378381e6c78f.crt',
    #                 '/home/alegra6/ssl/keys/c32c2_e8937_3765a379194b429f8d85040e0d17bbcb.key')
    #         )

    