const searchInput = document.getElementById("searchInput");

if(searchInput){

    searchInput.addEventListener("keyup", function(){

        let filter = searchInput.value.toLowerCase();

        let files = document.querySelectorAll(".file-item");

        files.forEach(function(file){

            let text = file.innerText.toLowerCase();

            if(text.includes(filter)){
                file.style.display = "flex";
            }
            else{
                file.style.display = "none";
            }

        });

    });

}
/* FILE FILTER */

function filterFiles(type){

    const files = document.querySelectorAll(".file-item");

    files.forEach(file => {

        const fileType = file.getAttribute("data-type");

        if(type === "all" || fileType === type){

            file.style.display = "flex";

        }

        else{

            file.style.display = "none";

        }

    });

}