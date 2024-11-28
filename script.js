// Fonction pour gérer l'envoi du formulaire de contact
document.getElementById('contact-form').addEventListener('submit', function (e) {
    e.preventDefault(); // Empêche l'envoi du formulaire

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    if (name && email && message) {
        alert(`Merci ${name}, nous avons bien reçu votre message.`);
    } else {
        alert("Veuillez remplir tous les champs.");
    }
});
