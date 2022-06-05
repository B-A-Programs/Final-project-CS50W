document.addEventListener('DOMContentLoaded', function () {
    document.querySelector("#btn_desc").onclick = function(e) {
        e.preventDefault();

        document.querySelector("#desc").style.display = "inline";
        document.querySelector("#educ").style.display = "none";
        document.querySelector("#course").style.display = "none";
        document.querySelector("#lang").style.display = "none";
        document.querySelector("#job").style.display = "none";
    };

    document.querySelector("#btn_educ").onclick = function(e) {
        e.preventDefault();

        document.querySelector("#desc").style.display = "none";
        document.querySelector("#educ").style.display = "inline";
        document.querySelector("#course").style.display = "none";
        document.querySelector("#lang").style.display = "none";
        document.querySelector("#job").style.display = "none";
    };
    
    document.querySelector("#btn_lang").onclick = function(e) {
        e.preventDefault();

        document.querySelector("#desc").style.display = "none";
        document.querySelector("#educ").style.display = "none";
        document.querySelector("#course").style.display = "none";
        document.querySelector("#lang").style.display = "inline";
        document.querySelector("#job").style.display = "none";
    };
    
    document.querySelector("#btn_job").onclick = function(e) {
        e.preventDefault();

        document.querySelector("#desc").style.display = "none";
        document.querySelector("#educ").style.display = "none";
        document.querySelector("#course").style.display = "none";
        document.querySelector("#lang").style.display = "none";
        document.querySelector("#job").style.display = "inline";
    };

    document.querySelector("#btn_course").onclick = function(e) {
        e.preventDefault();

        document.querySelector("#desc").style.display = "none";
        document.querySelector("#educ").style.display = "none";
        document.querySelector("#course").style.display = "inline";
        document.querySelector("#lang").style.display = "none";
        document.querySelector("#job").style.display = "none";
    };
})