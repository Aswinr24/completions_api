# Completions API

This API provides an endpoint for text completions using the Groq API.

## API Endpoint

### Complete Text

- **URL:** `/complete-text`
- **Method:** `POST`
- **Description:** Provides text completion based on the given prompt.

#### Example
##### Request Body

```json
{
    "prompt": "I wish I was a"
}
```

##### Response

```json
{
    "completion": "I wish I was a kid again, with no worries and endless summers."
}
```

#### Installation: 

1. Clone the repository:
   
   ```bash
   git clone https://github.com/Aswinr24/completions_api.git
   ```
3. Create a Virtual Environment:
   ```bash
   python3 -m venv .venv
   ```
4. Activate the Virtual Enviroment:
   ```bash
   source .venv/bin/activate
   ```
5. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Set Up Environment Variables:
   Create a ```.env``` file in the root directory and add your environment variables:
   ```bash
   GROQ_API_KEY=your_api_key
   ```
7. Run the API:
   ```bash
   uvicorn api:app --host 0.0.0.0 --port 8000
   ```

