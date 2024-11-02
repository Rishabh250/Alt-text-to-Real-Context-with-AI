# Milestone 1: Basic Alt-text Generation

## Overview
The goal of Milestone 1 is to build a foundational AI model that generates descriptive alt-text for images. This milestone focuses on creating clear, accessible alt-text that provides a basic description of images.

## Objectives
1. Set up an environment for running AI models.
2. Develop a basic model to generate descriptive alt-text for images.
3. Ensure alt-text adheres to accessibility standards.

## Endpoint

### `/generate-alt-text`
- **Method**: POST
- **Description**: Generates descriptive alt-text for an image provided by URL.
- **Request JSON**:
    ```json
    {
        "image_url": "https://example.com/image.jpg"
    }
    ```
- **Response JSON**:
    ```json
    {
        "alt_text": "A clear and descriptive alt-text for the image."
    }
    ```

## Running the Milestone
1. Navigate to the `milestone_1` folder.
2. Run the Flask app:
    ```bash
    python app.py
    ```
3. Test the endpoint with Postman or `curl`. 