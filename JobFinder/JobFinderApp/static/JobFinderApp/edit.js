// Show only the form which the user is looking for
document.addEventListener('DOMContentLoaded', function () {
    document.querySelector("#btn_desc").onclick = function(e) {
        e.preventDefault();

        document.querySelector("#desc").style.display = "inline";
        document.querySelector("#educ").style.display = "none";
        document.querySelector("#course").style.display = "none";
        document.querySelector("#lang").style.display = "none";
        document.querySelector("#job").style.display = "none";
        document.querySelector("#field").style.display = "none";
    };

    document.querySelector("#btn_educ").onclick = function(e) {
        e.preventDefault();

        document.querySelector("#desc").style.display = "none";
        document.querySelector("#educ").style.display = "inline";
        document.querySelector("#course").style.display = "none";
        document.querySelector("#lang").style.display = "none";
        document.querySelector("#job").style.display = "none";
        document.querySelector("#field").style.display = "none";
    };
    
    document.querySelector("#btn_lang").onclick = function(e) {
        e.preventDefault();

        document.querySelector("#desc").style.display = "none";
        document.querySelector("#educ").style.display = "none";
        document.querySelector("#course").style.display = "none";
        document.querySelector("#lang").style.display = "inline";
        document.querySelector("#job").style.display = "none";
        document.querySelector("#field").style.display = "none";
    };
    
    document.querySelector("#btn_job").onclick = function(e) {
        e.preventDefault();

        document.querySelector("#desc").style.display = "none";
        document.querySelector("#educ").style.display = "none";
        document.querySelector("#course").style.display = "none";
        document.querySelector("#lang").style.display = "none";
        document.querySelector("#job").style.display = "inline";
        document.querySelector("#field").style.display = "none";
    };

    document.querySelector("#btn_course").onclick = function(e) {
        e.preventDefault();

        document.querySelector("#desc").style.display = "none";
        document.querySelector("#educ").style.display = "none";
        document.querySelector("#course").style.display = "inline";
        document.querySelector("#lang").style.display = "none";
        document.querySelector("#job").style.display = "none";
        document.querySelector("#field").style.display = "none";
    };

    document.querySelector("#btn_field").onclick = function(e) {
        e.preventDefault();

        document.querySelector("#desc").style.display = "none";
        document.querySelector("#educ").style.display = "none";
        document.querySelector("#course").style.display = "none";
        document.querySelector("#lang").style.display = "none";
        document.querySelector("#job").style.display = "none";
        document.querySelector("#field").style.display = "inline";
    };
})


// Create dropdown
document.addEventListener('DOMContentLoaded', function() {
    var select = document.getElementById("selectField");
    var options = ["Architecture and engineering", "Arts, culture and entertainment", "Business, management and administration", "Communications", "Community and social services",
        "Education", "Science and technology", "Installation, repair and maintenance", "Farming, fishing and forestry", "Health and medicine", "Law and public policy", "Sales"];

    for(var i = 0; i < options.length; i++) {
        var x = options[i];
        var op = document.createElement("option");
        op.textContent = x;
        op.value = x;
        select.appendChild(op);
    }
})