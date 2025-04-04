function openModal() {
    document.getElementById("loginModal").style.display = "block";
}

function closeModal() {
    document.getElementById("loginModal").style.display = "none";
}

function handleLoginClick() {
    const firstName = sessionStorage.getItem('first_name');
    if (!firstName) {
        openModal();
    }
}

window.onclick = function(event) {
    var modal = document.getElementById("loginModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function redirectToCart() {
    window.location.href = "/cart";
}

function addProductToMemory(product) {
    let memoryProducts = JSON.parse(sessionStorage.getItem('memoryProducts')) || [];
    const existingProduct = memoryProducts.find(p => p.id === product.id);

    if (existingProduct) {
        existingProduct.quantity += 1;
    } else {
        product.quantity = 1;
        memoryProducts.push(product);
    }

    sessionStorage.setItem('memoryProducts', JSON.stringify(memoryProducts));
}

function loadMemoryProducts() {
    const memoryProducts = JSON.parse(sessionStorage.getItem('memoryProducts')) || [];
    const memorySection = document.querySelector('.memory-products');
    memoryProducts.forEach(product => {
        const productElement = document.createElement('div');
        productElement.classList.add('product');
        productElement.innerHTML = `
            <h3>${product.name}</h3>
            <p>${product.description}</p>
            <p>Preço: $${product.price}</p>
            <p>Quantidade: ${product.quantity}</p>
            ${product.image_url ? `<img src="${product.image_url}" alt="${product.name}">` : ''}
        `;
        memorySection.appendChild(productElement);
    });
}

function storeUserData(username, firstName) {
    sessionStorage.setItem('username', username);
    sessionStorage.setItem('first_name', firstName);
}

function displayFirstName() {
    const firstName = sessionStorage.getItem('first_name');
    if (firstName) {
        const loginIcon = document.getElementById('login-icon');
        loginIcon.innerHTML = `<div class="first-letter">${firstName.charAt(0)}</div>`;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const products = document.querySelectorAll('.product');
    const memorySection = document.querySelector('.memory-products');

    products.forEach(product => {
        product.addEventListener('click', function() {
            const productData = {
                id: product.getAttribute('data-id'),
                name: product.querySelector('h3').innerText,
                description: product.querySelector('p').innerText,
                price: product.querySelector('p:nth-of-type(2)').innerText.replace('Preço: $', ''),
                image_url: product.querySelector('img') ? product.querySelector('img').src : ''
            };
            addProductToMemory(productData);
            memorySection.innerHTML = '';
            loadMemoryProducts(); 
        });
    });
    loadMemoryProducts();
    displayFirstName();
    const loginForm = document.getElementById('login-form');
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(loginForm);
        const username = formData.get('username');
        const firstName = document.getElementById('first_name').value;
        storeUserData(username, firstName);
        loginForm.submit();
    });
});