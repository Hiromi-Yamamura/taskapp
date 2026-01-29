// theme-script.js
document.addEventListener('DOMContentLoaded', () => {
    const theme = localStorage.getItem('theme') || 'light'; // 保存されたテーマを取得、無ければlight
    document.documentElement.setAttribute('data-bs-theme', theme);
});

function setTheme(theme) {
    localStorage.setItem('theme', theme);
    document.documentElement.setAttribute('data-bs-theme', theme);
}

// ボタンクリックでテーマ変更
document.getElementById('btn-dark')?.addEventListener('click', () => setTheme('dark'));
document.getElementById('btn-light')?.addEventListener('click', () => setTheme('light'));
