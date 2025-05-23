# Web-Based Image Outliner

This project converts images into outlines/pencil sketches using a Laplacian filter, now with a user-friendly web interface. The implementation leverages Flask for the web application and OpenCV/NumPy for image processing.

![Demo](demo.gif) *(Example of the web interface in action)*

## Features

- **Drag & Drop Interface**: Easily upload images by dragging or selecting files
- **Image Preview**: See your selected image before processing
- **Outline Generation**: Convert images to outlines with one click
- **Download Results**: Save your outline images with a single click
- **Responsive Design**: Works on both desktop and mobile devices

## Technologies Used

- **Flask**: Python web framework for the backend
- **OpenCV**: For image processing tasks
- **NumPy**: For numerical operations and array handling
- **HTML/CSS/JavaScript**: For the interactive frontend interface

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/image-outliner-web.git
    cd image-outliner-web
    ```

2. Create and activate a virtual environment (recommended):

    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On Mac/Linux:
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install flask opencv-python numpy
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to:

    ```
    http://localhost:5000
    ```

3. Use the interface to:
   - Drag & drop an image or click to select
   - Preview your selected image
   - Click "Generate Outline" to process
   - Download the result with the "Download Outline" button

## Project Structure
