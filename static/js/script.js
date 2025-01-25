function redirectToProductPage(productId) {
  // Редирект на страницу с детальным описанием товара
  window.location.href = `/lamp/${productId}`;
}


function addToCart(lamp_id) {
  $.ajax({
    url: '/add_to_cart/' + lamp_id,
    type: 'GET',
    success: function (response) {
      document.getElementById('popup').style.display = 'block';
    },
    error: function (response) {

    }
  });
}

function deleteFromCart(lamp_id) {
  $.ajax({
    url: '/cart/delete/' + lamp_id,
    type: 'GET',
    success: function (response) {
      document.getElementById('popup').style.display = 'block';
    },
    error: function (response) {

    }
  });
}

// Close the popup when the close button is clicked
document.addEventListener('DOMContentLoaded', function() {
  const closeBtn = document.querySelector('.close-btn');
  const popup = document.getElementById('popup');

  closeBtn.addEventListener('click', function() {
    popup.style.display = 'none';
  });

  // Close the popup when clicking outside of the popup content
  window.addEventListener('click', function(event) {
    if (event.target == popup) {
      popup.style.display = 'none';
    }
  });
});
