from backend.model.model_loader import gemini_model

def review_code(code: str):
    
    prompt = f"""
    Perform a professional code review on the following Python code.
    Provide short, point-wise feedback highlighting improvements, errors, or best practices.

    Code:
    {code}
    """

    response = gemini_model.generate_content(prompt)

    # Extract response text
    if hasattr(response, "text"):
        return response.text.strip()
    
    return "ERROR: No response received from Gemini API."
