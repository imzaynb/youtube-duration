document.addEventListener("DOMContentLoaded", ()=>{ 
    console.log("Hello!");

    const form = document.querySelector("#form");
    const input = document.querySelector("#url-input");

    form.addEventListener("submit", e => {
        let url = input.value;
        console.log(url);
        e.preventDefault();
    });

});