document.addEventListener('DOMContentLoaded', () => {
    const pinInputs = document.querySelectorAll('.pin-input');
    const form = document.getElementById('pinForm');
    const messageBox = document.getElementById('message');

    // ── Hiển thị thông báo inline thay vì alert() ──────────
    function showMessage(text, type) {
        messageBox.textContent = text;
        messageBox.className = `message ${type}`;
    }

    function hideMessage() {
        messageBox.className = 'message hidden';
    }

    // ── Xử lý từng ô PIN ───────────────────────────────────
    pinInputs.forEach((input, index) => {

        input.addEventListener('focus', function () {
            this.select();
        });

        // Dán chuỗi số vào nhiều ô cùng lúc
        input.addEventListener('paste', function (e) {
            e.preventDefault();
            const numbers = (e.clipboardData || window.clipboardData)
                .getData('text')
                .replace(/[^0-9]/g, '')
                .split('');

            if (numbers.length > 0) {
                let cur = index;
                numbers.forEach(n => {
                    if (cur < pinInputs.length) {
                        pinInputs[cur].value = n;
                        cur++;
                    }
                });
                pinInputs[Math.min(cur, pinInputs.length - 1)].focus();
            }
        });

        // Chỉ nhận số, tự chuyển ô kế tiếp
        input.addEventListener('input', function () {
            this.value = this.value.replace(/[^0-9]/g, '').slice(-1);
            if (this.value.length === 1 && index < pinInputs.length - 1) {
                pinInputs[index + 1].focus();
            }
        });

        // Backspace xóa từ ô cuối cùng có giá trị
        input.addEventListener('keydown', function (e) {
            if (e.key === 'Backspace') {
                e.preventDefault();
                for (let i = pinInputs.length - 1; i >= 0; i--) {
                    if (pinInputs[i].value !== '') {
                        pinInputs[i].value = '';
                        pinInputs[i].focus();
                        return;
                    }
                }
                pinInputs[0].focus();
            }
        });
    });

    // ── Submit form ────────────────────────────────────────
    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        hideMessage();

        const pin = Array.from(pinInputs).map(i => i.value).join('');

        if (pin.length !== 6) {
            showMessage('Vui lòng nhập đầy đủ 6 số!', 'error');
            return;
        }

        const btn = form.querySelector('.submit-btn');
        btn.disabled = true;
        btn.textContent = 'Đang xác thực...';

        try {
            const response = await fetch('/api/staff/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id: pin })
            });

            const data = await response.json();

            if (response.ok) {
                showMessage(`Xin chào, ${data.staff.name}!`, 'success');
                // TODO: chuyển hướng sang trang thanh toán
                // window.location.href = '/staff/pos';
            } else {
                showMessage(data.message, 'error');
                pinInputs.forEach(i => i.value = '');
                pinInputs[0].focus();
            }
        } catch {
            showMessage('Không thể kết nối đến máy chủ.', 'error');
        } finally {
            btn.disabled = false;
            btn.textContent = 'Đăng Nhập';
        }
    });
});