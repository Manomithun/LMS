fetch("/api/method/library_management.api.get_library_status")
    .then(response => response.json())
    .then(response => {

        const data = response.message;

        console.log(data);

        document.getElementById("total-books").innerText =
            data.Total_Books;

        document.getElementById("total-members").innerText =
            data.Total_Members;

        document.getElementById("issued-books").innerText =
            data.Book_Issued;

        document.getElementById("available-books").innerText =
            data.Available_book;
    })
    .catch(error => {
        console.error(error);
    });