from dash import html, Dash
import dash_uploader as du
import os

app = Dash(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'tmp', 'dash_uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok = True)  # Ensure it exists
du.configure_upload(app, UPLOAD_FOLDER)


app.layout = html.Div([
    du.Upload(id = 'test-uploader', text = 'Upload files here', max_files = 15)
])

if __name__ == '__main__':
    app.run_server(debug = True, port = 8051)