let form = document.querySelector('.form');

document.querySelector('.btn-submit').addEventListener('click', (e) => {
    e.preventDefault();
    document.querySelector('.error').innerHTML = '';

    inputs = form.getElementsByTagName('input');

    let username = encodeURIComponent(inputs[1].value);
    let password1 = inputs[2].value;
    let password2 = inputs[3].value;
    let pass1 = encodeURIComponent(password1),
        pass2 = encodeURIComponent(password2);

    if (password1 != password2) {
        document.querySelector('.error').innerHTML = 'Пароли не совпадают! Попробуйте еще...';
        let xhr = new XMLHttpRequest();

        xhr.open("POST", 'login/');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        xhr.send('username=' + username + "&password1=" + pass1 + '&password2=' + pass2);
    }

})


/* <div class="user__menu">
                            <a href="{% url 'settings' %}">Настройки</a>
                            <form action="{% url 'logout' %}" method="POST">
                                {% csrf_token %}
                                <button type="submit">Выйти</button>
                            </form>
                        </div> */