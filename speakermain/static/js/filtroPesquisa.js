document.addEventListener("DOMContentLoaded", function () {
    // Filtro de pesquisa
    const searchBar = document.getElementById("search-bar");
    const listItems = document.querySelectorAll(".list-container li");

    searchBar.addEventListener("input", function () {
        const searchText = searchBar.value.toLowerCase();

        listItems.forEach(function (item) {
            const title = item.querySelector("h2 a").textContent.toLowerCase();
            if (title.includes(searchText)) {
                item.style.display = ""; // Mostra o item
            } else {
                item.style.display = "none"; // Esconde o item
            }
        });
    });
});