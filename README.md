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
