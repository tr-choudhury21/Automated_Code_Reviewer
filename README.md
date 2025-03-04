


# 🚀 Automated Code Reviewer  

An AI-powered tool that reviews Python code using **Google Gemini AI** and provides structured feedback on improvements, best practices, and potential issues.  

## 📌 Features  
✔ **AI-Powered Code Review** using Google Gemini API.  
✔ **Modern UI** with Streamlit for easy code submission.   
✔ **FastAPI Backend** for seamless API requests.  
✔ **Scalable & Modular** structure for easy modifications.  

## 🛠️ Tech Stack  
### **Backend:**  
- **FastAPI** → Lightweight Python web framework.  
- **Google Gemini API** → AI-powered code review.  
- **Hugging Face Transformers (Optional)** → Alternative AI model support.  

### **Frontend:**  
- **Streamlit** → Interactive UI for code submission and feedback.  
- **Custom CSS** → For modern UI styling.  

## ⚙️ Installation & Setup  
### **1️⃣ Clone the Repository**  

```bash
git clone https://github.com/yourusername/automated-code-reviewer.git
cd automated-code-reviewer

```

### **2️⃣ Set Up a Virtual Environment** 

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

```

### **3️⃣ Install Dependencies** 

```bash
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt

```

### **4️⃣ Set Up API Keys** 

- Go to **Google AI Studio** and generate an API key.
- Create a ```.env``` file in ```backend/``` and add:



```bash
GEMINI_API_KEY=your_google_gemini_api_key_here

```

### **5️⃣ Run the Backend** 

```bash
uvicorn backend.main:app --reload

```

- The API will be available at: http://127.0.0.1:8000/


### **6️⃣ Run the Frontend** 

```bash
streamlit run frontend/app.py

```

- The UI will be accessible at: http://localhost:8501/
## 📝 How to Use

- 1️⃣ Enter Python code in the Streamlit UI.
- 2️⃣ Click **"Review My Code"** to get AI-generated feedback.
- 3️⃣ The AI will analyze errors, improvements, and best practices.

## Contributing

Contributions are always welcome!

- Fork the project.

- Create a new branch
```bash
    git checkout -b feature/AmazingFeature
```
- Commit your changes
```bash
    git commit -m 'Add some new features'
```
- Push to the branch
```bash
    git push origin feature/AmazingFeature
```
- Open a pull request


Please adhere to this project's `code of conduct`.

## 📜 License

This project is licensed under [MIT](https://choosealicense.com/licenses/mit/) License. Feel free to use and modify.

