from app import app
import config

# Only run the app if this script is being executed directly (not imported as a module)
if __name__ == '__main__':
    # Start the app and listen on all available network interfaces on the configured port
    # app.run(host='0.0.0.0', port=8888)
    app.run(host='0.0.0.0', port=config.SERVER_PORT)
    print("Server is listening... ")
