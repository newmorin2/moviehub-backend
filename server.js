import express from 'express';
import dotenv from 'dotenv';
import mongoose from 'mongoose';
import bookingRoutes from './routes/bookingRoutes.js';

dotenv.config();
const app = express();

app.use(express.json());

// Allow CORS from Vite/dev and other origins during development
app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  if (req.method === 'OPTIONS') return res.sendStatus(204);
  next();
});

// Relax Content Security Policy for local development (prevents devtools/CSP blocks)
app.use((req, res, next) => {
  // Remove any existing CSP header set by other middleware/servers
  res.removeHeader && res.removeHeader('Content-Security-Policy');
  // Set a permissive policy for development only
  res.setHeader('Content-Security-Policy', "default-src * 'unsafe-inline' 'unsafe-eval' data: blob:");
  next();
});

// Simple request logger for debugging
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} - ${req.method} ${req.originalUrl}`);
  next();
});

app.get('/', (req, res) => res.json({ status: 'ok', message: 'Backend is running' }));

app.use('/api/bookings', bookingRoutes);

// Demo bookings route (useful when DB is empty or disconnected)
app.get('/api/bookings/demo', (req, res) => {
  const demo = [
    { id: 'demo1', userId: 'demoUser', serviceName: 'Demo Service A', bookingDate: new Date().toISOString(), status: 'confirmed' },
    { id: 'demo2', userId: 'demoUser', serviceName: 'Demo Service B', bookingDate: new Date().toISOString(), status: 'pending' }
  ];
  res.json(demo);
});

const PORT = process.env.PORT || 3000;
const MONGO_URI = process.env.MONGO_URI || 'mongodb://localhost:27017/mydb';

let mongooseConnected = false;
(async () => {
  try {
    await mongoose.connect(MONGO_URI);
    mongooseConnected = true;
    console.log('MongoDB connected');
  } catch (err) {
    console.error('Warning: Failed to connect to MongoDB', err.message || err);
    console.error('Continuing without DB connection — some endpoints may fail.');
  } finally {
    // Bind to 0.0.0.0 so the server is reachable from other hosts/containers
    const HOST = process.env.HOST || '0.0.0.0';
    app.listen(PORT, HOST, () => console.log(`Server running on ${HOST}:${PORT} (DB connected: ${mongooseConnected})`));
  }
})();

// Graceful error handlers so crashes are visible in logs
process.on('uncaughtException', (err) => {
  console.error('Uncaught Exception:', err);
});
process.on('unhandledRejection', (reason) => {
  console.error('Unhandled Rejection:', reason);
});
