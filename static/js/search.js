document.querySelector('.searchBox').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const query = document.querySelector('input[name="q"]').value;
        then(response => response.text())
        then(data => {
            document.body.innerHTML = data;  // Обновляем содержимое страницы
        });
});