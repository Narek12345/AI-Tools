let socket;

function startBot() {
	// Показываем индикатор загрузки
	document.getElementById('loading-indicator').style.display = 'block';

	// Инициализация WebSocket соединения
	socket = new WebSocket('ws://' + window.location.host + '/ws/telegram_bot/status/' + botId + '/');

	// Обработчик получения сообщений
	socket.onmessage = function(e) {
		const data = JSON.parse(e.data);
		const statusDiv = document.getElementById('status');

		if (data.message) {
			// Обновление статуса на странице
			statusDiv.innerHTML = '<p class="alert alert-info">' + data.message + '</p>';
		}

		// Скрываем индикатор загрузки, когда получен ответ
		document.getElementById('loading-indicator').style.display = 'none';
	};

	// Обработчик закрытия соединения
	socket.onclose = function(e) {
		console.error('WebSocket closed unexpectedly');

		// Скрываем индикатор загрузки, если соединение было закрыто
		document.getElementById('loading-indicator').style.display = 'none';
	};

	// После того как WebSocket подключен, отправить сообщение
	socket.onopen = function() {
		document.querySelector('#start-bot-btn').onclick = function(e) {
			// Проверяем, что WebSocket открыт
			if (socket.readyState === WebSocket.OPEN) {
				socket.send(JSON.stringify({
					'message': "Start"
				}));
			} else {
				console.error('WebSocket is not open.');
			}
		};
	};
}
