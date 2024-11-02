# Milestone 2: Brand Voice Integration

## Overview
This milestone refines the AI model to generate alt-text that aligns with Microsoft’s brand tone, ensuring descriptions resonate with brand values.

## Endpoint

### `/brand-voice`
- **Method**: POST
- **Request JSON**:
    ```json
    {
        "image_url": "https://example.com/image.jpg",
        "brand_tone": "professional"
    }
    ``` 