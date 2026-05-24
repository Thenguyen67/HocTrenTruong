const pool = require('../../config/Db');

const loginStaff = (req, res) => {
    const { id } = req.body;

    if (!id || id.length !== 6) {
        return res.status(400).json({ message: 'Mã PIN không hợp lệ' });
    }

    pool.query('SELECT * FROM staff WHERE id = ? AND is_active = 1', [id], (err, results) => {
        if (err) {
            console.error('Lỗi truy vấn MySQL:', err.message);
            return res.status(500).json({ message: 'Lỗi máy chủ' });
        }

        if (results.length > 0) {
            const staff = results[0];
            res.status(200).json({ message: 'Thành công', staff });
        } else {
            res.status(401).json({ message: 'Sai mã PIN!' });
        }
    });
};

module.exports = { loginStaff };