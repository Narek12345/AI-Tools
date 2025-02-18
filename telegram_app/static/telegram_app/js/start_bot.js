let socket;

function startBot() {
    // Показываем индикатор загрузки
    document.getElementById('loading-indicator').style.display = 'block';

    // Блокируем кнопку "Запустить", пока идет процесс запуска
    const startButton = document.getElementById('start-bot-btn');
    startButton.disabled = true;

    // Инициализация WebSocket соединения
    socket = new WebSocket('ws://' + window.location.host + '/ws/telegram_bot/status/' + botId + '/');

    // Обработчик получения сообщений
    socket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const statusDiv = document.getElementById('status');

        // Обновление статуса на странице
        if (data.status) {
            statusDiv.innerHTML = '<p class="alert alert-info">' + data.status + '</p>';
        }

        // Скрываем индикатор загрузки
        document.getElementById('loading-indicator').style.display = 'none';

        // Включаем кнопку "Запустить" обратно после получения ответа
        startButton.disabled = false;
    };

    // Обработчик закрытия соединения
    socket.onclose = function(e) {
        console.error('WebSocket closed unexpectedly');
        document.getElementById('loading-indicator').style.display = 'none';
        startButton.disabled = false;
    };

    // После того как WebSocket подключен, отправляем команду на запуск бота
    socket.onopen = function() {
        socket.send(JSON.stringify({
            "to_status": "start",
            "bot_id": botId
        }));
    };
}
