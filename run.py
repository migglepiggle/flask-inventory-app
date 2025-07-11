from app import create_app
from flask import redirect, url_for

app = create_app()

# ✅ Valid homepage route defined directly on the app instance
@app.route('/')
def home():
    return redirect(url_for('inventory.index'))

if __name__ == '__main__':
    app.run(debug=True)
