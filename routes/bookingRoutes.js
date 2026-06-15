// routes/bookingRoutes.js
import express from 'express';
import { createBooking, getUserBookings } from '../controllers/bookingController.js';

const router = express.Router();

// Create booking endpoint
router.post('/', createBooking);

// Get user bookings endpoint
router.get('/user/:userId', getUserBookings);

export default router;