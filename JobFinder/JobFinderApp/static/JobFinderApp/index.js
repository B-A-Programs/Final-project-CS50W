// Create dropdowns
document.addEventListener('DOMContentLoaded', function() {
    var select1 = document.getElementById("dp_people");
    var options = ["Architecture and engineering", "Arts, culture and entertainment", "Business, management and administration", "Communications", "Community and social services",
        "Education", "Science and technology", "Installation, repair and maintenance", "Farming, fishing and forestry", "Health and medicine", "Law and public policy", "Sales"];

    for(var i = 0; i < options.length; i++) {
        var x = options[i];
        var op = document.createElement('a');
        op.textContent = x;
        op.href = `users/${x}`
        op.class = 'dropdown-content'
        select1.appendChild(op);
    }

    var select2 = document.getElementById("dp_jobs")
    for(var i = 0; i < options.length; i++) {
        var x = options[i];
        var op = document.createElement('a');
        op.textContent = x;
        op.href = `posts/${x}/any`
        select2.appendChild(op);
    }
})
