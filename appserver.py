"""
appserver.py
- creates an application instance and runs the dev server
"""

if __name__ == '__main__':
    from paymentapi.application import create_app
    app = create_app()
    # app.run(host='0.0.0.0', debug=True, port=8081, ssl_context='adhoc')
    app.run(host='0.0.0.0', debug=True, port=8081)
    

    
