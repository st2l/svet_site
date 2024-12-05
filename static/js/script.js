function redirectToProductPage(productId) {
  // Редирект на страницу с детальным описанием товара
  window.location.href = `/lamp/${productId}`;
}


function addToCart(event, productId) {
  // Отменяем действие по умолчанию (редирект)
  event.stopPropagation(); // Останавливаем всплытие события

  fetch('/add-to-cart', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ productId: productId })
  })
  .then(response => response.json())
  .then(data => {
      alert('Товар добавлен в корзину!');
      // Обработать ответ от сервера, например, обновить счетчик товаров в корзине
  })
  .catch(error => {
      console.error('Ошибка при добавлении в корзину:', error);
  });
}
