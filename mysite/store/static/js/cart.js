function loadCartProducts() {
    const cartProducts = JSON.parse(sessionStorage.getItem('memoryProducts')) || [];
    const cartTableBody = document.querySelector('#cart-table tbody');

    cartProducts.forEach(product => {
        const productRow = document.createElement('tr');
        productRow.innerHTML = `
            <td>${product.name}</td>
            <td>${product.quantity}</td>
            <td>$${product.price}</td>
            <td>$${(product.price * product.quantity).toFixed(2)}</td>
        `;
        cartTableBody.appendChild(productRow);
    });
}

document.addEventListener('DOMContentLoaded', function() {
    loadCartProducts();
});