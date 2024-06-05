function showPasswordCriteria() {
    document.getElementById('password-criteria').style.display = 'block';
}

function hidePasswordCriteria() {
    document.getElementById('password-criteria').style.display = 'none';
}

document.getElementById('password').addEventListener('input', function() {
    var password = this.value;

    var lengthCriteria = document.getElementById('length-criteria');
    if (password.length >= 8) {
        lengthCriteria.style.color = 'green';
    } else {
        lengthCriteria.style.color = 'red';
    }

    var numberCriteria = document.getElementById('number-criteria');
    if (/\d/.test(password)) {
        numberCriteria.style.color = 'green';
    } else {
        numberCriteria.style.color = 'red';
    }

    // Kiểm tra có chứa cả chữ hoa và chữ thường
    var caseCriteria = document.getElementById('case-criteria');
    if (/[a-z]/.test(password) && /[A-Z]/.test(password)) {
        caseCriteria.style.color = 'green';
    } else {
        caseCriteria.style.color = 'red';
    }
});

function showUserCriteria() {
    document.getElementById('user-criteria').style.display = 'block';
}

function hideUserCriteria() {
    document.getElementById('user-criteria').style.display = 'none';
}

document.getElementById('username').addEventListener('input', function() {
    var password = this.value;

    // Kiểm tra độ dài mật khẩu
    var lengthCriteria = document.getElementById('user-length-criteria');
    if (password.length >= 5 && password.length <= 10) {
        lengthCriteria.style.color = 'green';
    } else {
        lengthCriteria.style.color = 'red';
    }
});

function showEmailCriteria() {
    document.getElementById('email-criteria').style.display = 'block';
}

function hideEmailCriteria() {
    document.getElementById('email-criteria').style.display = 'none';
}

function isEmailValid(email) {
    const emailRegexp = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegexp.test(email);
}

document.getElementById('email').addEventListener('input', function() {
    var email = this.value;

    var valid = document.getElementById('valid-email-criteria');
    if (isEmailValid(email)) {
        valid.style.color = 'green';
    } else {
        valid.style.color = 'red';
    }
});

function validateForm() {
    var password = document.getElementById('password').value;
    var username = document.getElementById('username').value.trim();
    var email = document.getElementById('email').value.trim();

    var checkEmpty = (password.length != 0 && username.length != 0 && email.length != 0);
    var lengthValid = password.length >= 8;
    var numberValid = /\d/.test(password);
    var caseValid = /[a-z]/.test(password) && /[A-Z]/.test(password);
    var usernameLength = (5 <= username.length && username.length <= 10);
    var validEmail = isEmailValid(email);

    if (lengthValid && numberValid && caseValid && usernameLength && validEmail && checkEmpty) {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/requestSignUp', true);
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                console.log(`ReadyState: ${xhr.readyState}`);
                console.log(`Status: ${xhr.status}`);
                if (xhr.status === 200) {
                    try {
                        const data = JSON.parse(xhr.responseText);
                        console.log('Response Data:', data);
                    } catch (e) {
                        console.error('Error parsing JSON:', e);
                        console.log('Raw response:', xhr.responseText);
                    }
                } else {
                    console.error('Request failed with status:', xhr.status);
                }
            }
        };
    
        const requestData = JSON.stringify({ password, username, email });
        console.log('Request Data:', requestData);
        xhr.send(requestData);
    } else {
        alert("Thông tin người dùng chưa xác thực");
    }
    
}