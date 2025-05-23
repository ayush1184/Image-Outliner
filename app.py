# from flask import Flask, render_template, request, redirect, url_for
# import os
# import cv2
# import filtering

# app = Flask(__name__)

# # Configuration
# app.config['UPLOAD_FOLDER'] = 'static/uploads'
# app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Check if a file was uploaded
#         if 'file' not in request.files:
#             return redirect(request.url)
        
#         file = request.files['file']
        
#         if file.filename == '':
#             return redirect(request.url)
        
#         if file and allowed_file(file.filename):
#             # Save the uploaded file
#             input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#             file.save(input_path)
            
#             # Process the image
#             input_image = cv2.imread(input_path, 0)
#             outline = filtering.Filtering(input_image)
#             an_outline = outline.get_outline()
            
#             # Save the output
#             output_filename = 'outline_' + file.filename
#             output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
#             cv2.imwrite(output_path, an_outline)
            
#             return render_template('index.html', 
#                                  input_image=file.filename,
#                                  output_image=output_filename)
    
#     return render_template('index.html')

# if __name__ == '__main__':
#     os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
#     app.run(debug=True)


# Version 2:
from flask import Flask, render_template, request, send_from_directory
import os
import cv2
import filtering

app = Flask(__name__)

# Configure upload folder (Render allows persistent storage)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400
    
    if file:
        # Save uploaded file
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(input_path)
        
        # Process image
        input_image = cv2.imread(input_path, 0)
        outline = filtering.Filtering(input_image).get_outline()
        
        # Save output
        output_filename = f"outline_{file.filename}"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        cv2.imwrite(output_path, outline)
        
        return {
            "input_image": file.filename,
            "output_image": output_filename
        }

# Static files
@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Explicitly set port
