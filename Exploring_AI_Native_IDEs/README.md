Exploring AI-Native IDEs – Simple REST APIs

This repo contains two tiny REST APIs, each exposing two endpoints: `GET /items` and `POST /items`.

- Node.js Express
- Python FastAPI

Both are in-memory (data resets on restart).

Run the Express API

1. Install Node.js 18+.
2. Install dependencies:

   ```bash
   cd node-express
   npm install --silent
   ```

3. Start the server:

   ```bash
   npm run start
   # or hot-reload
   npm run dev
   ```

4. Test endpoints:

   ```bash
   curl http://localhost:3000/items
   curl -X POST http://localhost:3000/items \
     -H "Content-Type: application/json" \
     -d '{"name":"apple"}'
   ```

Run the FastAPI API

1. Install Python 3.10+.
2. Install dependencies (ideally inside a virtualenv):

   ```bash
   cd python-fastapi
   pip install -r requirements.txt
   ```

3. Start the server:

   ```bash
   uvicorn main:app --reload --port 8000
   ```

4. Test endpoints:

   ```bash
   curl http://localhost:8000/items
   curl -X POST http://localhost:8000/items \
     -H "Content-Type: application/json" \
     -d '{"name":"banana"}'
   ```

Notes

- Both implementations store items in memory. Use a database for persistence.
- `POST /items` expects JSON: `{ "name": "<string>" }` and returns created item with an `id`.
