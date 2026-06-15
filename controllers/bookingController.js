// controllers/bookingController.js
import { Booking } from '../models/Booking.js';

// @desc    Create a new booking
// @route   POST /api/bookings
export const createBooking = async (req, res) => {
  try {
    const { userId, serviceName, bookingDate } = req.body;

    // Basic validation
    if (!userId || !serviceName || !bookingDate) {
      return res.status(400).json({ message: 'All fields are required.' });
    }

    const newBooking = new Booking({
      userId,
      serviceName,
      bookingDate
    });

    const savedBooking = await newBooking.save();
    res.status(201).json(savedBooking);
  } catch (error) {
    console.error('createBooking error:', error);
    res.status(500).json({ message: 'Server error while creating booking.', error: error.message });
  }
};

// @desc    Get bookings for a specific user
// @route   GET /api/bookings/user/:userId
export const getUserBookings = async (req, res) => {
  try {
    const { userId } = req.params;

    // If userId is not a valid ObjectId, return empty array (avoid cast errors)
    const mongoose = await import('mongoose');
    if (!mongoose.Types.ObjectId.isValid(userId)) {
      return res.status(200).json([]);
    }

    const bookings = await Booking.find({ userId }).sort({ bookingDate: 1 });

    if (!bookings || bookings.length === 0) {
      return res.status(200).json([]);
    }

    res.status(200).json(bookings);
  } catch (error) {
    res.status(500).json({ message: 'Server error while fetching bookings.', error: error.message });
  }
};