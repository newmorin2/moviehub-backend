# Backend API

Simple Express + Mongoose backend for managing bookings.

**Prerequisites**
- Node.js (v14+ recommended)
- MongoDB running locally or a MongoDB URI

**Install**

```bash
npm install
```

Create a `.env` file (optional — defaults are provided):

```
PORT=3000
MONGO_URI=mongodb://localhost:27017/mydb
```

**Run**

```bash
node server.js
```

Or install `nodemon` for automatic restarts:

```bash
npm install -g nodemon
nodemon server.js
```

**API Endpoints**

- `POST /bookings` — create a booking (JSON body: `name`, `email`, `date`)
- `GET /bookings` — list bookings
- `GET /bookings/:id` — get booking by id
- `DELETE /bookings/:id` — delete a booking

**Example**

Create booking with `curl`:

```bash
curl -X POST http://localhost:3000/bookings \
  -H "Content-Type: application/json" \
  -d '{"name":"Jane Doe","email":"jane@example.com","date":"2026-06-15"}'
```

**Notes**
- The project expects `express`, `mongoose`, and `dotenv` as dependencies.
- Add validation or tests as needed.

**Docker (optional)**

Build and run using Docker Compose (this will also start a MongoDB container):

```bash
docker compose up --build
```

This will expose:
- Backend: http://localhost:3000
- Frontend: http://localhost:8080

If you prefer manual build/run:

```bash
# Build backend image
docker build -t my-backend .

# Build frontend image
docker build -t my-frontend ./frontend

# Run MongoDB (optional if using docker-compose)
docker run -d --name mongo -v mongo_data:/data/db -p 27017:27017 mongo:6.0

# Run backend
docker run -d --name backend -p 3000:3000 -e MONGO_URI=mongodb://host.docker.internal:27017/mydb my-backend

# Run frontend
docker run -d --name frontend -p 8080:80 my-frontend
```

## Running locally (recommended for development)

1) Kill any process listening on port 3000 (if needed):

```bash
# show listener(s)
sudo lsof -nP -iTCP:3000 -sTCP:LISTEN || true
# kill listener(s) if you confirm the PID(s):
sudo lsof -t -iTCP:3000 -sTCP:LISTEN | xargs -r sudo kill -9
```

2) Install Node dependencies and start backend:

```bash
npm install --no-audit --no-fund
node server.js
```

3) Open the frontend dev server (Vite) or the static frontend:

- Vite (dev): `npm run dev` then open http://localhost:5173/
- Static frontend (nginx): http://localhost:8080/ (if using docker-compose frontend)

4) Health checks:

```bash
curl -i http://localhost:3000/
curl -i http://localhost:3000/api/bookings/user/demoUser
```

If you still see "Cannot GET /": make sure the process bound to `:3000` is the Node `server.js` you just started (see step 1).
