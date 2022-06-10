document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[id^="btn_"]').forEach(button => {
        button.onclick = function(e) {
            e.preventDefault()

            let id = this.dataset.id;

            let form = document.querySelector('#form_' + id);

            form.style.display = "block";
        }
    })
})