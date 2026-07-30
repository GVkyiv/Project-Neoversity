const loginForm = document.querySelector('.login-form');

loginForm.addEventListener('submit', event => {
  event.preventDefault();

  const { email, password } = event.currentTarget.elements;
  const formData = {
    email: email.value.trim(),
    password: password.value.trim(),
  };

  if (formData.email === '' || formData.password === '') {
    alert('All form fields must be filled in');
    return;
  }

  console.log(formData);
  event.currentTarget.reset();
});
