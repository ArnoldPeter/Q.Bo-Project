from flask import Flask

app = Flask()
bp = gateway.receiver_blueprint_for('main')  # SMS receiver
app.register_blueprint(bp, url_prefix='/sms/main')  # register it with Flask