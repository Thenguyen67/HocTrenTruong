const express = require('express');
const router = express.Router();
const { loginStaff } = require('../../controller/staff/staffController');

router.post('/login', loginStaff);

module.exports = router;