const express = require('express');
const path = require('path');
const staffRoutes = require('./routes/staff/staffRoutes');

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Routes API
app.use('/api/staff', staffRoutes);

// Trang mặc định → login staff
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/views/staff/html/Login.html'));
});

app.listen(PORT, () => {
    console.log(`Server đang chay tai http://localhost:${PORT}`);
});